"""Public teaching utility. Select project files via reviewed package-files.txt."""
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import zipfile

from verify_package import verify


def build(root):
    names = [line.strip() for line in (root / 'package-files.txt').read_text().splitlines()
             if line.strip() and not line.lstrip().startswith('#')]
    if len(names) != len(set(names)) or 'SOURCE_MANIFEST.json' in names:
        raise ValueError('Lista duplicada o manifiesto reservado')
    contents = {}
    for name in names:
        parts = PurePosixPath(name).parts
        if (not parts or name.startswith('/') or '\\' in name
                or any(p.startswith('.') or p in {'evidence', 'evidencia', '__pycache__', 'dist'} for p in parts)):
            raise ValueError('Ruta no permitida: ' + name)
        file = root / name
        if any((root.joinpath(*parts[:i])).is_symlink() for i in range(1, len(parts) + 1)):
            raise ValueError('No se permiten symlinks: ' + name)
        if not file.is_file():
            raise ValueError('Falta archivo requerido: ' + name)
        contents[name] = file.read_bytes()
    commit = os.getenv('GITHUB_SHA') or subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    manifest = {'source_commit': commit,
                'files': {n: hashlib.sha256(data).hexdigest() for n, data in contents.items()}}
    dist = root / 'dist'
    dist.mkdir(exist_ok=True)
    target, temporary = dist / 'capstone.zip', dist / 'capstone.partial.zip'
    target.unlink(missing_ok=True)
    try:
        with zipfile.ZipFile(temporary, 'w', zipfile.ZIP_DEFLATED) as archive:
            for name, data in contents.items():
                archive.writestr(name, data)
            archive.writestr('SOURCE_MANIFEST.json', json.dumps(manifest, indent=2))
        result = verify(temporary, commit)
        temporary.replace(target)
        return result
    finally:
        temporary.unlink(missing_ok=True)


if __name__ == '__main__':
    try:
        print(json.dumps(build(Path.cwd()), indent=2))
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        print('No se construyó el paquete: ' + str(exc), file=sys.stderr)
        sys.exit(1)
