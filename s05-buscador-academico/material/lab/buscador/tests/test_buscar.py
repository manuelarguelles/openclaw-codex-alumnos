import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from buscar import citation, consolidate, run_search  # noqa: E402
from fuentes import MissingCredentialError, enrich_unpaywall, search_source  # noqa: E402
import fuentes  # noqa: E402


def row(**overrides):
    value = {
        "title": "AI tutoring",
        "authors": ["Demo A"],
        "year": 2024,
        "doi": "",
        "id": "demo-1",
        "url": "",
        "abstract": "",
        "sources": ["crossref"],
    }
    value.update(overrides)
    return value


class ConsolidateTests(unittest.TestCase):
    def test_duplicate_doi_keeps_both_sources(self):
        rows = [
            row(doi="https://doi.org/10.1000/DEMO", id="a", sources=["crossref"]),
            row(doi="10.1000/demo", id="b", sources=["arxiv"]),
        ]

        result = consolidate(rows, "AI tutoring", 2022, 2026, 3)

        self.assertEqual(len(result), 1)
        self.assertEqual(set(result[0]["sources"]), {"crossref", "arxiv"})
        self.assertEqual(result[0]["doi"], "10.1000/demo")

    def test_duplicate_doi_preserves_first_metadata_and_reports_conflicts(self):
        rows = [
            row(title="First title", authors=["First Author"], year=2023,
                doi="10.1000/demo", sources=["crossref"]),
            row(title="Conflicting title", authors=["Other Author"], year=2024,
                doi="10.1000/demo", sources=["openalex"]),
        ]

        result = consolidate(rows, "title", 2022, 2026, 3)[0]

        self.assertEqual((result["title"], result["authors"], result["year"]),
            ("First title", ["First Author"], 2023))
        self.assertEqual(result["citation"],
            "First Author (2023). First title. https://doi.org/10.1000/demo")
        self.assertEqual({conflict["field"] for conflict in result["conflicts"]},
            {"title", "authors", "year"})
        self.assertIn("conflicting metadata: title, authors, year", result["warnings"])
        self.assertEqual(result["metadata_provenance"]["title"], [
            {"source": "crossref", "value": "First title"},
            {"source": "openalex", "value": "Conflicting title"},
        ])

    def test_duplicate_doi_completion_is_not_a_conflict(self):
        rows = [
            row(title="", authors=[], year=None, doi="10.1000/demo", sources=["crossref"]),
            row(title="Completed title", authors=["Demo Author"], year=2024,
                doi="10.1000/demo", sources=["openalex"]),
        ]

        result = consolidate(rows, "title", 2022, 2026, 3)[0]

        self.assertEqual(result["conflicts"], [])
        self.assertNotIn("conflicting metadata: title, authors, year", result["warnings"])
        self.assertEqual((result["title"], result["authors"], result["year"]),
            ("Completed title", ["Demo Author"], 2024))

    def test_different_dois_with_same_title_stay_separate(self):
        rows = [
            row(doi="10.1000/one", id="a"),
            row(doi="10.1000/two", id="b", sources=["openalex"]),
        ]
        self.assertEqual(len(consolidate(rows, "AI tutoring", 2022, 2026, 3)), 2)

    def test_matching_older_title_ranks_above_unrelated_newer_paper(self):
        rows = [
            row(title="AI tutoring in classrooms", year=2022, id="match"),
            row(title="Recent advances in soil chemistry", year=2026, id="new"),
        ]

        result = consolidate(rows, "AI tutoring", 2022, 2026, 3)

        self.assertEqual(result[0]["id"], "match")
        self.assertEqual(result[0]["rank_reason"], "2/2 query tokens in title/abstract")

    def test_year_filter_excludes_2020(self):
        rows = [row(year=2020, id="old"), row(year=2024, id="current")]
        self.assertEqual(
            [item["id"] for item in consolidate(rows, "AI tutoring", 2022, 2026, 3)],
            ["current"],
        )

    def test_missing_author_and_year_are_not_invented(self):
        result = consolidate(
            [row(authors=[], year=None, id="incomplete")], "AI tutoring", 2022, 2026, 3
        )
        self.assertEqual(result[0]["authors"], [])
        self.assertIsNone(result[0]["year"])
        self.assertEqual(
            set(result[0]["warnings"]), {"missing authors", "missing year", "missing DOI"}
        )

    def test_zero_matches_stays_empty(self):
        self.assertEqual(consolidate([], "AI tutoring", 2022, 2026, 3), [])

    def test_invalid_limit_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "limit must be greater than zero"):
            consolidate([], "AI tutoring", 2022, 2026, 0)

    def test_empty_query_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "query must not be empty"):
            consolidate([], "   ", 2022, 2026, 3)

    def test_citation_uses_only_available_metadata(self):
        self.assertEqual(
            citation(row(doi="10.1000/demo")),
            "Demo A (2024). AI tutoring. https://doi.org/10.1000/demo",
        )
        self.assertEqual(citation(row(authors=[], year=None, doi="")), "AI tutoring.")

    def test_generated_citation_is_explicitly_unverified(self):
        result = consolidate([row(doi="10.1000/demo")], "AI tutoring", 2022, 2026, 3)
        self.assertEqual(result[0]["citation_status"], "unverified")


class SearchTests(unittest.TestCase):
    def test_partial_timeout_retains_success_and_reports_source(self):
        def fetcher(source, query, limit):
            if source == "arxiv":
                raise TimeoutError("request timed out after 10 seconds")
            return [row(id="crossref-1", sources=[source])]

        result = run_search("AI tutoring", ["crossref", "arxiv"], 3, 2022, 2026, fetcher)

        self.assertEqual(len(result["records"]), 1)
        self.assertEqual(result["sources"]["crossref"], {"status": "ok", "count": 1})
        self.assertEqual(result["sources"]["arxiv"]["status"], "error")
        self.assertEqual(result["errors"][0]["source"], "arxiv")

    def test_malformed_source_response_is_reported(self):
        result = run_search(
            "AI tutoring", ["crossref"], 3, 2022, 2026, lambda *_: {"not": "a list"}
        )
        self.assertEqual(result["records"], [])
        self.assertEqual(result["errors"][0]["reason"], "malformed response: expected a list")

    def test_fetcher_receives_each_source_contract(self):
        calls = []

        def fetcher(source, query, limit):
            calls.append((source, query, limit))
            return []

        run_search("AI tutoring", ["crossref", "arxiv"], 3, 2022, 2026, fetcher)
        self.assertEqual(
            set(calls),
            {("crossref", "AI tutoring", 3), ("arxiv", "AI tutoring", 3)},
        )


class ProviderContractTests(unittest.TestCase):
    def test_semantic_documented_envelope_is_normalized(self):
        payload = {"total": 1, "offset": 0, "data": [{
            "paperId": "S2-1", "title": "AI tutoring", "year": 2024,
            "authors": [{"authorId": "A1", "name": "Demo Author"}],
            "externalIds": {"DOI": "10.1000/DEMO"},
            "url": "https://example.invalid/s2", "abstract": "Study"
        }]}
        with patch.object(fuentes, "_request", return_value=json.dumps(payload).encode()):
            result = search_source("semantic", "AI tutoring", 1)
        self.assertEqual(result[0]["id"], "S2-1")
        self.assertEqual(result[0]["doi"], "10.1000/demo")

    def test_semantic_malformed_envelope_is_rejected(self):
        with patch.object(fuentes, "_request", return_value=b'{"data": {}}'):
            with self.assertRaisesRegex(RuntimeError, "data is not a list"):
                search_source("semantic", "AI tutoring", 1)

    def test_core_documented_envelope_is_normalized(self):
        payload = {"totalHits": 1, "results": [{
            "id": 7, "title": "AI tutoring", "yearPublished": 2024,
            "authors": [{"name": "Demo Author"}], "doi": "10.1000/DEMO",
            "downloadUrl": "https://example.invalid/core.pdf", "abstract": "Study"
        }]}
        with patch.dict(os.environ, {"CORE_API_KEY": "fixture-key"}, clear=True):
            with patch.object(fuentes, "_request", return_value=json.dumps(payload).encode()):
                result = search_source("core", "AI tutoring", 1)
        self.assertEqual(result[0]["id"], "7")
        self.assertEqual(result[0]["authors"], ["Demo Author"])

    def test_core_malformed_envelope_is_rejected(self):
        with patch.dict(os.environ, {"CORE_API_KEY": "fixture-key"}, clear=True):
            with patch.object(fuentes, "_request", return_value=b'{"results": {}}'):
                with self.assertRaisesRegex(RuntimeError, "results is not a list"):
                    search_source("core", "AI tutoring", 1)

    def test_crossref_documented_envelope_is_normalized(self):
        payload = {"message": {"items": [{
            "title": ["AI tutoring"], "abstract": "<jats:p>Study</jats:p>",
            "author": [{"given": "Demo", "family": "Author"}],
            "published": {"date-parts": [[2024, 1, 2]]},
            "DOI": "https://doi.org/10.1000/DEMO", "URL": "https://example.invalid/work"
        }]}}
        with patch.object(fuentes, "_request", return_value=json.dumps(payload).encode()):
            result = search_source("crossref", "AI tutoring", 1)
        self.assertEqual(result[0]["doi"], "10.1000/demo")
        self.assertEqual(result[0]["authors"], ["Demo Author"])

    def test_arxiv_documented_atom_entry_is_normalized(self):
        payload = b'''<feed xmlns="http://www.w3.org/2005/Atom">
          <entry><id>https://arxiv.org/abs/2401.00001</id><published>2024-01-01T00:00:00Z</published>
          <title>AI tutoring</title><summary>Study</summary><author><name>Demo Author</name></author></entry>
        </feed>'''
        with patch.object(fuentes, "_request", return_value=payload):
            result = search_source("arxiv", "AI tutoring", 1)
        self.assertEqual(result[0]["id"], "2401.00001")
        self.assertEqual(result[0]["year"], 2024)

    def test_openalex_documented_envelope_rebuilds_abstract(self):
        payload = {"results": [{
            "id": "https://openalex.org/W1", "title": "AI tutoring", "publication_year": 2024,
            "doi": None, "authorships": [{"author": {"display_name": "Demo Author"}}],
            "primary_location": {"landing_page_url": "https://example.invalid/work"},
            "abstract_inverted_index": {"AI": [0], "tutoring": [1]}
        }]}
        with patch.object(fuentes, "_request", return_value=json.dumps(payload).encode()):
            result = search_source("openalex", "AI tutoring", 1)
        self.assertEqual(result[0]["abstract"], "AI tutoring")
        self.assertEqual(result[0]["sources"], ["openalex"])

    def test_core_missing_credential_is_explicit_without_network(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(MissingCredentialError, "CORE_API_KEY is not set"):
                search_source("core", "AI tutoring", 2)

    def test_unpaywall_missing_credential_is_explicit(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(MissingCredentialError, "UNPAYWALL_EMAIL is not set"):
                enrich_unpaywall("10.1000/demo")

    def test_cli_invalid_limit_exits_nonzero_with_no_json_result(self):
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS / "buscar.py"), "AI tutoring", "--limit", "0"],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("greater than zero", proc.stderr)
        with self.assertRaises(json.JSONDecodeError):
            json.loads(proc.stdout)

    def test_cli_unpaywall_missing_email_returns_explicit_json_error(self):
        env = os.environ.copy()
        env.pop("UNPAYWALL_EMAIL", None)
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS / "buscar.py"), "--enrich-doi", "10.1000/demo"],
            text=True, capture_output=True, check=False, env=env,
        )
        payload = json.loads(proc.stdout)
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(payload["mode"], "enrichment")
        self.assertEqual(payload["errors"][0]["reason"], "UNPAYWALL_EMAIL is not set")


if __name__ == "__main__":
    unittest.main()
