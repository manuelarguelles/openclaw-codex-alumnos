"""Adaptadores HTTP públicos para cinco índices y enriquecimiento Unpaywall."""
from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

SOURCES = ("crossref", "arxiv", "semantic", "openalex", "core")
TIMEOUT_SECONDS = 10
MAX_RETRY_AFTER_SECONDS = 2

class MissingCredentialError(RuntimeError):
    """A provider cannot be called without its named environment variable."""

class MalformedResponseError(RuntimeError):
    """A provider returned a payload outside its documented schema."""

def canonical_doi(value):
    doi = (value or "").strip()
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.I)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.I)
    return doi.lower()

def _record(title="", authors=None, year=None, doi="", identifier="", url="", abstract="", source=""):
    return {
        "title": (title or "").strip(),
        "authors": [str(author).strip() for author in (authors or []) if str(author).strip()],
        "year": int(year) if str(year or "").isdigit() else None,
        "doi": canonical_doi(doi), "id": str(identifier or "").strip(),
        "url": str(url or "").strip(),
        "abstract": re.sub(r"<[^>]+>", " ", abstract or "").strip(),
        "sources": [source],
    }

def _request(url, headers=None):
    request_headers = {"Accept": "application/json, application/atom+xml;q=0.9", "User-Agent": "buscador-academico-course/1.0"}
    request_headers.update(headers or {})
    request = urllib.request.Request(url, headers=request_headers)
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code not in (429, 503) or attempt == 1:
                raise RuntimeError(f"HTTP {error.code}") from error
            raw_retry_after = str((error.headers or {}).get("Retry-After", "1")).strip()
            # Retry-After is a minimum wait, not a duration we may truncate.
            # This small teaching client defers dates/long waits to the caller.
            if not raw_retry_after.isascii() or not raw_retry_after.isdigit():
                raise RuntimeError(f"HTTP {error.code}; retry deferred: non-second Retry-After") from error
            retry_after = int(raw_retry_after)
            if retry_after > MAX_RETRY_AFTER_SECONDS:
                raise RuntimeError(f"HTTP {error.code}; retry deferred: wait at least {retry_after}s") from error
            time.sleep(retry_after)
        except (TimeoutError, urllib.error.URLError) as error:
            raise RuntimeError(f"network error: {getattr(error, 'reason', error)}") from error
    raise RuntimeError("request failed")

def _get_json(url, headers=None):
    try:
        value = json.loads(_request(url, headers).decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise MalformedResponseError("invalid JSON") from error
    if not isinstance(value, dict):
        raise MalformedResponseError("JSON root must be an object")
    return value

def _query_url(base, params):
    return f"{base}?{urllib.parse.urlencode(params)}"

def _crossref(query, limit):
    params = {"query": query, "rows": limit, "select": "title,abstract,author,published,DOI,URL"}
    if os.environ.get("CROSSREF_EMAIL"):
        params["mailto"] = os.environ["CROSSREF_EMAIL"]
    payload = _get_json(_query_url("https://api.crossref.org/works", params))
    try:
        items = payload["message"]["items"]
    except (KeyError, TypeError) as error:
        raise MalformedResponseError("Crossref message.items missing") from error
    if not isinstance(items, list):
        raise MalformedResponseError("Crossref message.items is not a list")
    records = []
    for item in items:
        titles = item.get("title") or []
        parts = (item.get("published") or {}).get("date-parts") or []
        year = parts[0][0] if parts and parts[0] else None
        authors = [" ".join(filter(None, (a.get("given"), a.get("family")))) for a in item.get("author") or []]
        records.append(_record(title=titles[0] if titles else "", authors=authors, year=year,
            doi=item.get("DOI"), identifier=item.get("DOI"), url=item.get("URL"), abstract=item.get("abstract"), source="crossref"))
    return records

def _arxiv(query, limit):
    params = {"search_query": f"all:{query}", "start": 0, "max_results": limit, "sortBy": "relevance"}
    raw = _request(_query_url("https://export.arxiv.org/api/query", params))
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as error:
        raise MalformedResponseError("invalid arXiv Atom XML") from error
    ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    records = []
    for entry in root.findall("a:entry", ns):
        identifier = entry.findtext("a:id", default="", namespaces=ns)
        published = entry.findtext("a:published", default="", namespaces=ns)
        records.append(_record(title=entry.findtext("a:title", default="", namespaces=ns).replace("\n", " "),
            authors=[node.findtext("a:name", default="", namespaces=ns) for node in entry.findall("a:author", ns)],
            year=published[:4], doi=entry.findtext("arxiv:doi", default="", namespaces=ns),
            identifier=identifier.rsplit("/", 1)[-1], url=identifier,
            abstract=entry.findtext("a:summary", default="", namespaces=ns).replace("\n", " "), source="arxiv"))
    return records

def _semantic(query, limit):
    params = {"query": query, "limit": limit, "fields": "paperId,title,authors,year,externalIds,url,abstract"}
    headers = {"x-api-key": os.environ["SEMANTIC_SCHOLAR_API_KEY"]} if os.environ.get("SEMANTIC_SCHOLAR_API_KEY") else {}
    payload = _get_json(_query_url("https://api.semanticscholar.org/graph/v1/paper/search", params), headers)
    items = payload.get("data")
    if not isinstance(items, list):
        raise MalformedResponseError("Semantic Scholar data is not a list")
    return [_record(title=item.get("title"), authors=[a.get("name", "") for a in item.get("authors") or []],
        year=item.get("year"), doi=(item.get("externalIds") or {}).get("DOI"), identifier=item.get("paperId"),
        url=item.get("url"), abstract=item.get("abstract"), source="semantic") for item in items]

def _inverted_abstract(index):
    if not index:
        return ""
    try:
        words = sorted((position, word) for word, positions in index.items() for position in positions)
    except (AttributeError, TypeError) as error:
        raise MalformedResponseError("OpenAlex abstract_inverted_index is malformed") from error
    return " ".join(word for _, word in words)

def _openalex(query, limit):
    params = {"search": query, "per_page": limit,
        "select": "id,title,authorships,publication_year,doi,primary_location,abstract_inverted_index"}
    if os.environ.get("OPENALEX_API_KEY"):
        params["api_key"] = os.environ["OPENALEX_API_KEY"]
    payload = _get_json(_query_url("https://api.openalex.org/works", params))
    items = payload.get("results")
    if not isinstance(items, list):
        raise MalformedResponseError("OpenAlex results is not a list")
    records = []
    for item in items:
        location = item.get("primary_location") or {}
        authors = [(entry.get("author") or {}).get("display_name", "") for entry in item.get("authorships") or []]
        records.append(_record(title=item.get("title"), authors=authors, year=item.get("publication_year"),
            doi=item.get("doi"), identifier=item.get("id"), url=location.get("landing_page_url"),
            abstract=_inverted_abstract(item.get("abstract_inverted_index")), source="openalex"))
    return records

def _core(query, limit):
    key = os.environ.get("CORE_API_KEY")
    if not key:
        raise MissingCredentialError("CORE_API_KEY is not set")
    payload = _get_json(_query_url("https://api.core.ac.uk/v3/search/works/", {"q": query, "limit": limit}),
        {"Authorization": f"Bearer {key}"})
    items = payload.get("results")
    if not isinstance(items, list):
        raise MalformedResponseError("CORE results is not a list")
    records = []
    for item in items:
        authors = [a.get("name", "") if isinstance(a, dict) else str(a) for a in item.get("authors") or []]
        urls = item.get("sourceFulltextUrls") or []
        records.append(_record(title=item.get("title"), authors=authors, year=item.get("yearPublished"), doi=item.get("doi"),
            identifier=item.get("id"), url=item.get("downloadUrl") or (urls[0] if urls else ""),
            abstract=item.get("abstract"), source="core"))
    return records

def search_source(source, query, limit):
    adapters = {"crossref": _crossref, "arxiv": _arxiv, "semantic": _semantic, "openalex": _openalex, "core": _core}
    if source not in adapters:
        raise ValueError(f"unknown source: {source}")
    return adapters[source](query, limit)

def enrich_unpaywall(doi):
    email = os.environ.get("UNPAYWALL_EMAIL")
    if not email:
        raise MissingCredentialError("UNPAYWALL_EMAIL is not set")
    canonical = canonical_doi(doi)
    if not canonical:
        raise ValueError("DOI is required for Unpaywall enrichment")
    url = _query_url(f"https://api.unpaywall.org/v2/{urllib.parse.quote(canonical, safe='')}", {"email": email})
    payload = _get_json(url)
    location = payload.get("best_oa_location") or {}
    return {"doi": canonical, "is_oa": bool(payload.get("is_oa")),
        "oa_url": location.get("url_for_pdf") or location.get("url") or ""}
