# Kit público de empaquetado · Andamiaje S08

Estas utilidades genéricas no contienen la solución S07. Copia `scripts/package.py`, `scripts/verify_package.py` y `package-files.txt` dentro de tu capstone S07 terminado; conserva archivos preexistentes y pide al agente integrar si coinciden nombres.

El agente debe completar **la lista permitida**, revisando imports y recursos HTML/CSS, y añadir comprobación de referencias estáticas propias. El kit comprueba nombres mínimos, rutas, ausencia de symlinks, inventario y hashes; no deduce dependencias ni demuestra arranque o comportamiento. `package-files.txt` inicial aún no conoce los módulos de tu app.

Desde tu capstone con Git, `python scripts/package.py` produce `dist/capstone.zip`; `python scripts/verify_package.py dist/capstone.zip` inspecciona sin extraer ni ejecutar. En CI usa GITHUB_SHA; local usa HEAD (los cambios sin commit no quedan identificados por ese SHA: hacer commit antes del build que entregarás). No requiere instalar librerías adicionales.

Para adaptar otro stack, declarar contrato mínimo equivalente en el verificador. Antes del push, inspecciona archivo por archivo y excluye datos privados; una lista permitida necesita revisión humana. Contrato completo: `../plantillas/contrato-paquete.md`.
