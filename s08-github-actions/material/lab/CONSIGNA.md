# S08 · Un cambio, una comprobación verificable

Trabaja sobre **tu capstone de S07**, con sus datos sintéticos y pruebas. Conversa con el agente desde Telegram; revisa archivos, diff y resultados. No necesitas la solución privada del instructor. La clase dura 180 minutos con pausas de 5 minutos en 85–90 y 130–135.

## Recursos proporcionados y salidas por crear

Proporcionados: esta consigna; `plantillas/capstone-ci.yml.template`, `plantillas/contrato-paquete.md`, `plantillas/entrega.md`, `plantillas/notificaciones.md` y [kit público de empaquetado](package-kit/README.md); de S07, [starter](../../../s07-web-capstone/material/lab/starter/README.md), [SPEC](../../../s07-web-capstone/material/lab/SPEC.md) y [datos sintéticos](../../../s07-web-capstone/material/lab/datos/perfil-oferta.json). Estas rutas son del repositorio del curso; no una implementación terminada.

Por crear con el agente en **tu repo**: implementación S07, `mapa-ci.md`, `.github/workflows/capstone-ci.yml`, herramientas/configuración de lint, pruebas pertinentes, `capstone/package-files.txt` adaptado, scripts del kit copiados, `capstone/dist/capstone.zip` generado, README con badge y `entrega-s08.md`. La plantilla se conserva inactiva en el curso; copiarla y completarla solo en tu repo. No activar un workflow que apunte a carpetas que no existen. El ZIP y resultados privados no se versionan.

Preflight: repo propio con permiso de escritura/Actions, app S07 terminada en carpeta `capstone/` o ruta declarada equivalente, instalación limpia y pruebas locales. Si falta app, termina S07 con starter y SPEC; el primer servidor `/health` no es la entrega completa. Usa Python 3.12 y el intérprete del entorno virtual. En Windows cambia `.venv/bin/python` por `.\.venv\Scripts\python.exe`. Para otro stack conserva el método y documenta comandos equivalentes, sin fingir React en HTML nativo.

## 8A

**Entrada:** web S07 y README. Pide: «Lee mi capstone. Crea mapa-ci.md con raíz de trabajo, stack, instalación, lint, test y build real. Para cada comando explica qué verifica, qué error lo haría fallar y qué no demuestra». Ejecuta esos comandos localmente con el agente. **Salida:** mapa y logs con versión. **Aceptación:** distingues CI de entrega/despliegue; cada chequeo tiene una condición real, no `echo OK`. **Recuperación:** si no existe lint o empaquetado, anótalo como trabajo de 8C. No llamar lint a compileall ni navegador a un GET del HTML.

## 8B

**Entrada:** mapa y plantilla. Pide: «Explícame on, jobs, steps, run, uses y runner; señala qué se ejecuta primero y por qué un segundo job requiere needs y descarga». Identifica dos rutas: `defaults.run.working-directory` para comandos y `with.path` desde raíz del repo para artefactos. **Salida:** anotación del YAML y mapa de dependencias. **Aceptación:** explicas por qué checkout y pip son necesarios y por qué jobs no comparten automáticamente archivos. **Recuperación:** espacios en vez de tabs, estructura antes que nuevos triggers.

## 8C

**Entrada:** app completa y contrato de paquete. Pide: «Copia las utilidades genéricas de package-kit a mi capstone. Completa package-files.txt desde imports y recursos reales; valida el contrato de plantillas/contrato-paquete.md y añade solo comprobaciones propias faltantes. Configura Ruff y fíjalo en requirements-dev.txt; conserva las dependencias existentes. Completa plantilla CI con mis rutas y comandos. Comprueba localmente, revisa diff y explícame permisos antes de subir al repo propio. No uses la solución del instructor». Para el espejo Python, ejecutar dentro de capstone:

```sh
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m ruff check .
node --check static/app.js
.venv/bin/python -m playwright install chromium
.venv/bin/python -m pytest -q --junitxml=dist/tests.xml
.venv/bin/python scripts/package.py
```

`package.py` y `verify_package.py` están proporcionados en package-kit; static y tests completos son la implementación S07 previa. La lista permitida debe adaptarse a tus módulos. En runner Ubuntu, instalar navegador con `--with-deps`. Si no usas Playwright, añade una comprobación real de tu UI y documenta el equivalente. Añade `.venv/`, `.data/`, `.env`, cachés y `dist/` al ignore del repo. El workflow debe estar en `.github/workflows/`, desde la raíz, con extensión yml. Revisa que ningún `TODO` quede activo, haz commit y push al repo de tu capstone. **Salida:** YAML y primer run URL/SHA. **Aceptación:** un push ejecuta instalación, lint, tests y build; inspecciona steps, no solo círculo verde. **Recuperación:** si no hay run revisa commit, ruta del archivo, Actions habilitado y trigger. Si no hay archivos, revisa checkout y rutas.

## 8D

**Entrada:** versión GREEN. Crea rama de ensayo. Pide: «Introduce una regresión pequeña en código que viole un criterio existente, sin editar el test». En el espejo: `/health` devuelve `broken` en vez de `ok`. Haz commit/push, abre run RED y guarda primer error, step, SHA y URL. Pide: «Diagnostica este log, corrige la implementación conservando el test, explica diff, repite local y remoto». Guarda nuevo GREEN.

Después, **segundo ciclo independiente**: pide cambiar solo `defaults.run.working-directory` a una carpeta inexistente en esa rama. Es YAML válido, configuración equivocada. Push, observa fallo y pide al agente corregir el YAML. Nuevo push y GREEN. **Salida:** dos pares de runs/diffs, uno de contrato y otro de YAML. **Aceptación:** explicas causas distintas; pruebas conservadas, sin `continue-on-error`, sin borrar chequeos. **Recuperación:** no cambies varios factores simultáneamente. Error sintáctico puede rechazarse antes de crear logs normales; no confundirlo con ruta equivocada. No llevar regresiones a rama principal.

## 8E

**Entrada:** acceso a Settings del repo y valor inocuo. En Settings → Secrets and variables → Actions → New repository secret configura `COURSE_PRACTICE_SECRET`. No uses token real de bot/modelo ni compartas el valor por chat. Pide al agente añadir el step de presencia de la plantilla y hacer push. **Salida:** log que solo dice presente o ausente. **Aceptación:** valor ausente en código/capturas/logs y núcleo CI independiente de credenciales. **Recuperación:** revisa nombre y evento; en PR de fork los secrets normalmente no están disponibles, también existen restricciones Dependabot. No usar pull_request_target para probar código externo con privilegios.

## 8F

**Entrada:** GREEN y artefacto `capstone-SHA`. Abre Actions → run → Artifacts y descarga. Pide: «En carpeta vacía inspecciona ZIP, SOURCE_MANIFEST.json, SHA, lista exacta y hashes según contrato; registra resultado sin alterar paquete». **Salida:** nombre del artefacto, URL run, SHA e inventario verificado. **Aceptación:** backend, static y dependencias requeridos presentes; `.data`, `.env`, credenciales, cachés y trazas ausentes. Si falta algo, corrige empaquetador y produce nuevo run; no edites el ZIP descargado. Explica que build de HTML nativo empaqueta; no publica ni compila React.

## 8G

**Entrada:** workflow en rama predeterminada mediante integración revisada de versión GREEN. Abre PR de rama propia y observa `pull_request`; registra head SHA y contexto del run (puede comprobar merge). En Actions → workflow → Run workflow elige ref y observa `workflow_dispatch`. Configura cron con zona IANA y explica cinco campos. Ejemplo: `17 8 * * 1-5`, `timezone: America/Lima`: 08:17 lunes a viernes. Sin timezone usa UTC. **Salida:** tabla evento/ref/SHA/URL/conclusión. **Aceptación:** push, PR y manual observados; cron configurado y observado solo cuando metadatos digan `schedule`. **Recuperación:** manual debe existir en default branch para habilitarse, aunque permite elegir otra ref; schedule corre default branch y puede retrasarse o descartarse por carga. No esperar cron durante clase. Repos públicos inactivos 60 días deshabilitan schedule. Mínimo 5 minutos.

## 8H

**Entrada:** resultados anteriores y plantilla entrega. Pide: «Completa entrega-s08.md con evidencia real, añade badge con OWNER/REPO reales y conserva pendientes». Otro lector abre badge y llega al workflow, relaciona un cambio con un run, explica ambos fallos y verifica ZIP. **Salida:** repo con CI en cada push, tabla de evidencias y tarea-puente. **Aceptación:** no confundir GREEN con despliegue, test determinista con modelo ni plantilla de notificación con envío. [Notificaciones](plantillas/notificaciones.md) es extensión opcional inactiva: prepara Telegram/Slack sin enviar.

Tarea S09: describir comando de arranque del paquete, entorno objetivo, variables sin valores, persistencia, versión a publicar, recuperación a versión anterior y responsable de aprobar. Todavía no desplegar.
