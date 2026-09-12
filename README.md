# Agentes AI con OpenClaw + Codex — alumnos

Repositorio público del curso. Aquí están las consignas, recursos y espacios de entrega. El laboratorio se realiza por conversación con el agente desde Telegram; no necesitas partir escribiendo código.

## Ruta de 10 sesiones

1. OpenClaw + Codex + Telegram
2. Identidad, reglas y memoria
3. GitHub como columna vertebral
4. SDD + superpowers + Kanban
5. Buscador académico
6. Skills y workflows
7. Plataforma web
8. Automatización con GitHub Actions
9. Publicación con Vercel
10. Demo day

## Adelantos de las sesiones 5 y 6

- [S05 · Buscador académico](s05-buscador-academico/): 48 slides, buscador ejecutable, tests, ejemplos de citas y mini-spec propia.
- [S06 · Skills y workflows](s06-skills-workflows/): 48 slides, tres skills, validador, casos y objetivo acotado con código y tests.

Preparación S05/S06 verificada el 12-sep-2026: pruebas locales, selección, refactor, concurrencia, `/goal` y recorrido real por Telegram. Cada consigna distingue ejecución real, captura y resultado esperado. Cada alumno verifica su propia instalación y acceso.

## Entregas

Crea una carpeta con tu usuario dentro de `sXX-.../entregas/`. Nunca subas tokens, claves, `.env`, credenciales ni capturas que los muestren.

## Workspace de referencia

La carpeta [`openclaw-workspace/`](openclaw-workspace/) contiene plantillas sanitizadas de identidad, reglas, memoria operativa y configuración. Úsala para comprender la estructura; reemplaza los placeholders únicamente en tu máquina y nunca publiques credenciales reales.

## Material de la sesión 2

- [Cuestionario de configuración del workspace](s02-primer-agente/cuestionario-configuracion-workspace.md): 50 preguntas de alternativa múltiple. El agente las realiza, interpreta las respuestas y propone la configuración de los archivos `.md`.

## Material de la sesión 3

- [Guía web desde cero · GitHub + OpenClaw](s03-github/guia-github.html): crea tu cuenta, instala las herramientas y conecta GitHub desde el navegador sin copiar tokens.
- [Deck · GitHub como columna vertebral](s03-github/S03-deck.html): 36 slides sobre preparación desde cero, historial, seguridad, publicación y recuperación.
- [Laboratorio versionado y recuperable](s03-github/laboratorio.md): ruta cero para crear cuenta e instalar herramientas, más el ejercicio vivo `mi-primer-proyecto` y cuatro checkpoints ejecutados desde Telegram con revisión humana antes del push.
- [`.gitignore` de referencia](s03-github/gitignore-openclaw.example): base conservadora para excluir secretos y estado operativo de OpenClaw.

## Material de la sesión 4

- [Deck · SDD + Superpowers + Kanban](s04-sdd-kanban/S04-deck.html): 51 slides para crear desde cero el asistente de postulación laboral, con referencia visual de Projects.
- [Laboratorio · ciclo SDD completo](s04-sdd-kanban/laboratorio.md): brainstorming, spec, plan, TDD, debugging, review y cierre; ROADMAP con WIP=1 y Projects como espejo.
- [Caso y comparación antes/después](s04-sdd-kanban/caso-postulacion.md), [escritura y lanzamiento del SDD](s04-sdd-kanban/lanzamiento-sdd.md), [starter de postulación con 15 tests](s04-sdd-kanban/postulacion-starter/).
- [Superpowers: instalación y 14 skills](s04-sdd-kanban/superpowers-guia.md), [plantillas](s04-sdd-kanban/plantillas.md) y [GitHub Projects gratuito y Kanban](s04-sdd-kanban/github-kanban.md).
- [Apéndice · conexiones y comandos desde OpenClaw](s04-append/guia-conexiones.html): MCP, APIs REST, CLI, OAuth, autenticación, tokens y ejemplos con GitHub, Gmail, Vercel, Railway y APIs de LLM.
