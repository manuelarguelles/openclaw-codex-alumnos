"""Validación estructural de borradores; no demuestra veracidad semántica."""
import json
from pathlib import Path
import sys


def validate(result, profile):
    """Devuelve errores de contrato. No modifica las entradas ni permite envíos."""
    errors = []
    if not isinstance(result, dict):
        return ['result debe ser un objeto JSON']
    if not isinstance(profile, list):
        return ['profile debe ser una lista']
    known = set()
    for index, item in enumerate(profile):
        if (not isinstance(item, dict) or not isinstance(item.get('id'), str)
                or not item['id'].strip() or not isinstance(item.get('text'), str)
                or not item['text'].strip()):
            errors.append(f'profile[{index}] requiere id y text no vacíos')
        elif item['id'] in known:
            errors.append(f'profile[{index}] tiene id duplicado')
        else:
            known.add(item['id'])
    if result.get('send_allowed') is not False:
        errors.append('send_allowed debe ser false')
    status = result.get('status')
    if status not in ('draft', 'needs_input'):
        errors.append('status debe ser draft o needs_input')
        return errors
    questions = result.get('questions')
    if (not isinstance(questions, list)
            or any(not isinstance(q, str) or not q.strip() for q in questions)):
        errors.append('questions debe ser una lista de preguntas no vacías')
    if status == 'needs_input':
        if not questions:
            errors.append('needs_input requiere preguntas')
        if 'claims' in result:
            errors.append('needs_input no permite claims')
        return errors
    gaps = result.get('gaps')
    if (not isinstance(gaps, list)
            or any(not isinstance(gap, str) or not gap.strip() for gap in gaps)):
        errors.append('gaps debe ser una lista de textos no vacíos')
    claims = result.get('claims')
    if not isinstance(claims, list) or not claims:
        errors.append('draft requiere claims no vacíos')
        return errors
    for index, claim in enumerate(claims):
        if not isinstance(claim, dict):
            errors.append(f'claims[{index}] debe ser objeto')
            continue
        if not isinstance(claim.get('text'), str) or not claim['text'].strip():
            errors.append(f'claims[{index}].text debe ser texto no vacío')
        ids = claim.get('evidence_ids')
        if not isinstance(ids, list) or not ids:
            errors.append(f'claims[{index}].evidence_ids requiere una lista no vacía')
        else:
            for evidence_id in ids:
                if not isinstance(evidence_id, str) or evidence_id not in known:
                    errors.append(f'claims[{index}] referencia evidencia desconocida: {evidence_id!r}')
    return errors


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 2:
        errors = ['Uso: python3 scripts/validar.py result.json profile.json']
    else:
        try:
            result = json.loads(Path(args[0]).read_text(encoding='utf-8'))
            profile = json.loads(Path(args[1]).read_text(encoding='utf-8'))
            errors = validate(result, profile)
        except (OSError, ValueError) as exc:
            errors = [f'No se pudo leer JSON: {exc}']
    print(json.dumps({'scope': 'structural', 'errors': errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
