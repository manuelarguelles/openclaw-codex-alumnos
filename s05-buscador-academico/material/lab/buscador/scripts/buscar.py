#!/usr/bin/env python3
"""CLI y núcleo reproducible del buscador académico público."""
from __future__ import annotations

import argparse
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from fuentes import SOURCES, canonical_doi, enrich_unpaywall, search_source

FIELDS = ("title", "authors", "year", "doi", "id", "url", "abstract", "sources")

def _tokens(value):
    return set(re.findall(r"[\w]+", (value or "").casefold(), flags=re.UNICODE))

def _validated_limit(limit):
    if limit <= 0:
        raise ValueError("limit must be greater than zero")

def _validated_query(query):
    if not query or not query.strip():
        raise ValueError("query must not be empty")

def citation(record):
    """Build a conservative readable citation from fields that actually exist."""
    item = _normalized_record(record)
    parts = []
    if item["authors"]:
        author_text = ", ".join(item["authors"])
        parts.append(f"{author_text} ({item['year']})." if item["year"] else f"{author_text}.")
    elif item["year"]:
        parts.append(f"({item['year']}).")
    if item["title"]:
        parts.append(f"{item['title']}.")
    if item["doi"]:
        parts.append(f"https://doi.org/{item['doi']}")
    elif item["url"]:
        parts.append(item["url"])
    return " ".join(parts)

def _normalized_record(record):
    if not isinstance(record, dict):
        raise ValueError("record is not an object")
    item = {field: record.get(field) for field in FIELDS}
    item["title"] = str(item["title"] or "").strip()
    item["authors"] = [str(value).strip() for value in (item["authors"] or []) if str(value).strip()]
    item["year"] = int(item["year"]) if str(item["year"] or "").isdigit() else None
    item["doi"] = canonical_doi(item["doi"])
    item["id"] = str(item["id"] or "").strip()
    item["url"] = str(item["url"] or "").strip()
    item["abstract"] = str(item["abstract"] or "").strip()
    item["sources"] = list(dict.fromkeys(str(value).strip() for value in (item["sources"] or []) if str(value).strip()))
    return item

def consolidate(records, query, year_from, year_to, limit):
    """Filter, deduplicate by DOI/source ID, and rank with lexical evidence."""
    _validated_limit(limit)
    _validated_query(query)
    if year_from > year_to:
        raise ValueError("year_from must not exceed year_to")
    query_tokens = _tokens(query)
    consolidated = {}
    for raw in records:
        item = _normalized_record(raw)
        if item["year"] is not None and not year_from <= item["year"] <= year_to:
            continue
        if item["doi"]:
            key = ("doi", item["doi"])
        else:
            source = item["sources"][0] if item["sources"] else "unknown"
            key = (source, item["id"] or f"anonymous-{len(consolidated)}")
        if key in consolidated:
            previous = consolidated[key]
            previous["sources"] = list(dict.fromkeys(previous["sources"] + item["sources"]))
            incoming_source = item["sources"][0] if item["sources"] else "unknown"
            for field in ("title", "authors", "year"):
                value = item[field]
                if value and previous[field] and value != previous[field]:
                    previous["metadata_provenance"][field].append(
                        {"source": incoming_source, "value": value}
                    )
                    previous["conflicts"].append({
                        "field": field,
                        "kept": previous[field],
                        "discarded": value,
                        "source": incoming_source,
                    })
                elif value and not previous[field]:
                    previous["metadata_provenance"][field].append(
                        {"source": incoming_source, "value": value}
                    )
            for field in ("title", "authors", "year", "id", "url", "abstract"):
                if not previous[field] and item[field]:
                    previous[field] = item[field]
        else:
            first_source = item["sources"][0] if item["sources"] else "unknown"
            item["metadata_provenance"] = {
                field: ([{"source": first_source, "value": item[field]}] if item[field] else [])
                for field in ("title", "authors", "year")
            }
            item["conflicts"] = []
            consolidated[key] = item
    ranked = []
    for item in consolidated.values():
        matches = len(query_tokens & _tokens(f"{item['title']} {item['abstract']}"))
        item["rank_reason"] = f"{matches}/{len(query_tokens)} query tokens in title/abstract"
        warnings = []
        if not item["authors"]:
            warnings.append("missing authors")
        if item["year"] is None:
            warnings.append("missing year")
        if not item["doi"]:
            warnings.append("missing DOI")
        conflicting_fields = [field for field in ("title", "authors", "year")
            if any(conflict["field"] == field for conflict in item["conflicts"])]
        if conflicting_fields:
            warnings.append(f"conflicting metadata: {', '.join(conflicting_fields)}")
        item["warnings"] = warnings
        item["citation"] = citation(item)
        item["citation_status"] = "unverified"
        ranked.append((matches, item["year"] or -1, item))
    ranked.sort(key=lambda value: (-value[0], -value[1], value[2]["title"].casefold()))
    return [item for _, _, item in ranked[:limit]]

def _safe_reason(error):
    reason = str(error).replace("\n", " ").strip() or error.__class__.__name__
    return re.sub(r"https?://\S+", "[url omitted]", reason)[:240]

def run_search(query, sources, limit, year_from, year_to, fetcher=None):
    """Query sources independently and retain partial success."""
    _validated_limit(limit)
    _validated_query(query)
    if year_from > year_to:
        raise ValueError("year_from must not exceed year_to")
    selected = list(dict.fromkeys(sources))
    unknown = [source for source in selected if source not in SOURCES]
    if unknown:
        raise ValueError(f"unknown source: {unknown[0]}")
    transport = fetcher or search_source
    records, status, errors = [], {}, []
    with ThreadPoolExecutor(max_workers=max(1, min(5, len(selected)))) as executor:
        futures = {executor.submit(transport, source, query, limit): source for source in selected}
        for future in as_completed(futures):
            source = futures[future]
            try:
                rows = future.result()
                if not isinstance(rows, list):
                    raise ValueError("malformed response: expected a list")
                normalized = []
                for raw in rows:
                    item = _normalized_record(raw)
                    if source not in item["sources"]:
                        item["sources"].append(source)
                    normalized.append(item)
                records.extend(normalized)
                status[source] = {"status": "ok", "count": len(normalized)}
            except Exception as error:
                reason = _safe_reason(error)
                status[source] = {"status": "error", "count": 0, "reason": reason}
                errors.append({"source": source, "reason": reason})
    return {"query": query, "records": consolidate(records, query, year_from, year_to, limit),
        "sources": {source: status[source] for source in selected},
        "errors": sorted(errors, key=lambda value: value["source"]), "mode": "live"}

def _offline_search(path, query, sources, limit, year_from, year_to):
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"offline fixture could not be read: {_safe_reason(error)}") from error
    rows = payload.get("records") if isinstance(payload, dict) else payload
    if not isinstance(rows, list):
        raise ValueError("offline fixture must contain a records list")
    selected = set(sources)
    rows = [row for row in rows if selected.intersection(row.get("sources") or [])]
    counts = {source: sum(source in (row.get("sources") or []) for row in rows) for source in sources}
    return {"query": query, "records": consolidate(rows, query, year_from, year_to, limit),
        "sources": {source: {"status": "offline", "count": counts[source]} for source in sources},
        "errors": [], "mode": "offline"}

def main(argv=None):
    parser = argparse.ArgumentParser(description="Buscador académico público y reproducible")
    parser.add_argument("query", nargs="?")
    parser.add_argument("--sources", nargs="+", choices=SOURCES, default=list(SOURCES))
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--year-from", type=int, default=1900)
    parser.add_argument("--year-to", type=int, default=2100)
    parser.add_argument("--offline", metavar="FIXTURE")
    parser.add_argument("--enrich-doi", metavar="DOI", help="Enriquece un DOI con Unpaywall; requiere UNPAYWALL_EMAIL")
    args = parser.parse_args(argv)
    try:
        _validated_limit(args.limit)
        if args.enrich_doi:
            try:
                record = enrich_unpaywall(args.enrich_doi)
                result = {"query": args.enrich_doi, "records": [record], "sources": {"unpaywall": {"status": "ok", "count": 1}}, "errors": [], "mode": "enrichment"}
            except Exception as error:
                reason = _safe_reason(error)
                result = {"query": args.enrich_doi, "records": [], "sources": {"unpaywall": {"status": "error", "count": 0, "reason": reason}}, "errors": [{"source": "unpaywall", "reason": reason}], "mode": "enrichment"}
        else:
            _validated_query(args.query)
            result = (_offline_search(args.offline, args.query, args.sources, args.limit, args.year_from, args.year_to)
                if args.offline else run_search(args.query, args.sources, args.limit, args.year_from, args.year_to))
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
