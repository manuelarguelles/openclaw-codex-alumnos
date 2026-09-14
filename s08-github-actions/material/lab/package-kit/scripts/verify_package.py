"""Public teaching utility: verify an archive without extracting or executing it."""
import hashlib
import json
import os
from pathlib import PurePosixPath
import sys
import zipfile


def verify(path, expected_sha=None):
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise ValueError('Entradas duplicadas')
        for name in names:
            parts = PurePosixPath(name).parts
            if (not parts or name.startswith('/') or '\\' in name
                    or any(p.startswith('.') or p in {'evidence', 'evidencia', '__pycache__', 'dist'} for p in parts)):
                raise ValueError('Ruta no permitida: ' + name)
        manifest = json.loads(archive.read('SOURCE_MANIFEST.json'))
        commit = manifest['source_commit']
        if len(commit) != 40 or any(c not in '0123456789abcdef' for c in commit):
            raise ValueError('SHA de origen inválido')
        if expected_sha and commit != expected_sha:
            raise ValueError('SHA no coincide con run')
        if set(manifest['files']) != set(names) - {'SOURCE_MANIFEST.json'}:
            raise ValueError('Inventario no coincide')
        if not {'app.py', 'requirements.txt', 'README.md', 'static/index.html', 'static/app.css', 'static/app.js'} <= set(names):
            raise ValueError('Faltan archivos mínimos del capstone FastAPI/HTML')
        for name, digest in manifest['files'].items():
            if hashlib.sha256(archive.read(name)).hexdigest() != digest:
                raise ValueError('Hash no coincide: ' + name)
        return {'source_commit': commit, 'files': sorted(names), 'hashes_verified': True}


if __name__ == '__main__':
    try:
        print(json.dumps(verify(sys.argv[1], os.getenv('EXPECTED_SHA')), indent=2))
    except (OSError, ValueError, KeyError, IndexError, zipfile.BadZipFile) as exc:
        print('No se verificó el paquete: ' + str(exc), file=sys.stderr)
        sys.exit(1)
