"""Controlled transport cases, not evidence of live provider access."""
import io
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import fuentes


class HttpPolicyTests(unittest.TestCase):
    def error(self, retry_after, code=429):
        return urllib.error.HTTPError('https://example.invalid', code, 'limit',
                                      {'Retry-After': retry_after}, None)

    def test_long_retry_after_defers_without_early_retry(self):
        with patch.object(fuentes.urllib.request, 'urlopen', side_effect=self.error('60')) as call, \
             patch.object(fuentes.time, 'sleep') as sleep:
            with self.assertRaisesRegex(RuntimeError, 'deferred'):
                fuentes._request('https://example.invalid')
            self.assertEqual(call.call_count, 1)
            sleep.assert_not_called()

    def test_date_retry_after_defers_without_guessing(self):
        with patch.object(fuentes.urllib.request, 'urlopen', side_effect=self.error('Wed, 21 Oct 2037 07:28:00 GMT')) as call, \
             patch.object(fuentes.time, 'sleep') as sleep:
            with self.assertRaisesRegex(RuntimeError, 'deferred'):
                fuentes._request('https://example.invalid')
            self.assertEqual(call.call_count, 1)
            sleep.assert_not_called()

    def test_short_retry_after_waits_then_succeeds(self):
        with patch.object(fuentes.urllib.request, 'urlopen', side_effect=[self.error('1'), io.BytesIO(b'{}')]) as call, \
             patch.object(fuentes.time, 'sleep') as sleep:
            self.assertEqual(fuentes._request('https://example.invalid'), b'{}')
            self.assertEqual(call.call_count, 2)
            sleep.assert_called_once_with(1)

    def test_repeated_limit_stops_after_one_retry(self):
        with patch.object(fuentes.urllib.request, 'urlopen', side_effect=self.error('1')) as call, \
             patch.object(fuentes.time, 'sleep'):
            with self.assertRaisesRegex(RuntimeError, 'HTTP 429'):
                fuentes._request('https://example.invalid')
            self.assertEqual(call.call_count, 2)

    def test_unpaywall_contract_enriches_doi_not_query(self):
        payload = {'is_oa': True, 'best_oa_location': {'url_for_pdf': 'https://example.invalid/paper.pdf'}}
        with patch.dict(fuentes.os.environ, {'UNPAYWALL_EMAIL': 'synthetic@example.invalid'}), \
             patch.object(fuentes, '_get_json', return_value=payload) as request:
            result = fuentes.enrich_unpaywall('https://doi.org/10.1000/DEMO')
        self.assertEqual(result, {'doi':'10.1000/demo', 'is_oa':True,
                                  'oa_url':'https://example.invalid/paper.pdf'})
        self.assertIn('/v2/10.1000%2Fdemo?', request.call_args.args[0])


if __name__ == '__main__':
    unittest.main()
