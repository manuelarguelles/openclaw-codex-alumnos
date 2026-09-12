"""Contratos con datos literales; cada caso detecta una omisión del validador."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'validar.py'
if SCRIPT.exists():
    spec = importlib.util.spec_from_file_location('validar', SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    validate = module.validate
else:
    def validate(result, profile):
        raise AssertionError('Falta implementar scripts/validar.py')


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.profile = [{'id': 'E1', 'text': 'Usé SQL'}]
        self.draft = {'status': 'draft', 'claims': [{'text': 'Usé SQL', 'evidence_ids': ['E1']}],
                      'gaps': ['Python'], 'questions': [], 'send_allowed': False}

    def test_supported_draft_is_accepted(self):
        self.assertEqual(validate(self.draft, self.profile), [])

    def test_unknown_evidence_is_rejected(self):
        self.draft['claims'][0]['evidence_ids'] = ['E9']
        self.assertTrue(validate(self.draft, self.profile))

    def test_missing_or_empty_evidence_is_rejected(self):
        for ids in (None, [], 'E1', [3]):
            with self.subTest(ids=ids):
                self.draft['claims'][0]['evidence_ids'] = ids
                self.assertTrue(validate(self.draft, self.profile))
        del self.draft['claims'][0]['evidence_ids']
        self.assertTrue(validate(self.draft, self.profile))

    def test_empty_draft_is_rejected(self):
        self.draft['claims'] = []
        self.assertTrue(validate(self.draft, self.profile))

    def test_send_permission_must_be_literal_false(self):
        for permission in (True, None, 0, 'false'):
            with self.subTest(permission=permission):
                self.draft['send_allowed'] = permission
                self.assertTrue(validate(self.draft, self.profile))

    def test_unknown_status_is_rejected(self):
        self.draft['status'] = 'sent'
        self.assertTrue(validate(self.draft, self.profile))

    def test_needs_input_requires_questions_and_no_claims(self):
        self.assertEqual(validate({'status': 'needs_input', 'questions': ['¿Cuál es el perfil?'],
                                   'send_allowed': False}, []), [])
        for changes in ({'questions': []}, {'claims': []}, {'claims': [{'text': 'SQL'}]},
                        {'questions': ['']}):
            with self.subTest(changes=changes):
                result = {'status': 'needs_input', 'questions': ['¿Perfil?'], 'send_allowed': False}
                result.update(changes)
                self.assertTrue(validate(result, []))

    def test_malformed_containers_are_reported_without_crash(self):
        for result, profile in (([], []), (None, []), (self.draft, {}),
                                (self.draft, [None]), (self.draft, [{'id': 'E1'}])):
            with self.subTest(result=result, profile=profile):
                self.assertTrue(validate(result, profile))

    def test_invalid_claim_and_required_lists_are_rejected(self):
        for changes in ({'claims': [None]}, {'claims': [{'text': '', 'evidence_ids': ['E1']}]},
                        {'gaps': 'Python'}, {'questions': None}):
            with self.subTest(changes=changes):
                result = dict(self.draft, **changes)
                self.assertTrue(validate(result, self.profile))

    def test_existing_id_does_not_prove_semantic_truth(self):
        self.draft['claims'][0]['text'] = 'Tengo diez años de Python'
        self.assertEqual(validate(self.draft, self.profile), [])

    def test_cli_exit_and_json_errors(self):
        self.assertTrue(SCRIPT.exists(), 'Falta implementar CLI')
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / 'profile.json'
            result = Path(directory) / 'result.json'
            profile.write_text(json.dumps(self.profile), encoding='utf-8')
            for valid in (True, False):
                result.write_text(json.dumps(self.draft if valid else {'status': 'sent'}), encoding='utf-8')
                process = subprocess.run([sys.executable, str(SCRIPT), str(result), str(profile)],
                                         capture_output=True, text=True)
                self.assertEqual(process.returncode, 0 if valid else 1)
                self.assertEqual(bool(json.loads(process.stdout)['errors']), not valid)
                self.assertEqual(process.stderr, '')
            result.write_text('{bad json', encoding='utf-8')
            process = subprocess.run([sys.executable, str(SCRIPT), str(result), str(profile)],
                                     capture_output=True, text=True)
            self.assertEqual(process.returncode, 1)
            self.assertTrue(json.loads(process.stdout)['errors'])


if __name__ == '__main__':
    unittest.main()
