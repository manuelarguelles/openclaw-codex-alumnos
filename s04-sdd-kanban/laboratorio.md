# Laboratorio S04 · Crear el asistente de postulación con SDD
## Resultado
Escribe y lanza un SDD para un agente nuevo basado en asistente-postulacion-laboral. Entrega spec y plan, un núcleo local probado y evidencia de revisión/Kanban. No dependemos de una issue anterior de S03.

## Material y preflight
Lee caso-postulacion.md, lanzamiento-sdd.md y superpowers-guia.md. Usa postulacion-starter/ (Node.js 22+, sin paquetes externos).
GitHub Free incluye Issues y Projects. Git y Codex deben estar disponibles; gh es opcional si usas la interfaz web. No usar CVs reales.
La antigua carpeta starter/ y solucion-docente/ corresponden a un ejemplo suplementario de validación de cierre, NO al caso principal.

## Checkpoint 0 · Instalación (bloque 1, 0–35 min)
Comprueba Superpowers en sesión nueva según la guía. Guarda versión, ruta, runtime y una pregunta pertinente de brainstorming. Una instalación en Codex no demuestra carga en OpenClaw.

## Checkpoint 1 · Brainstorm y spec (35–60 min)
Lee el baseline real y compara alternativas con los prompts 0–1 de lanzamiento-sdd.md.
Crea carpeta nueva de práctica. Define primera parte y backlog. Redacta brainstorm.md y spec.md con:
- CA1 entradas válidas o error explícito.
- CA2 coincidencias y brechas con evidencia del perfil.
- CA3 cobertura de obligatorios y null si no existen.
- CA4 borrador construido solo con hechos suministrados.
- CA5 función sin envío/red ni mutación de entrada.
- CA6 conducta del agente: veracidad, preguntas y límites.
- CA7 trazabilidad y revisión final.
Lee y aprueba la spec. Descanso 60–65.

## Checkpoint 2 · Plan, worktree y Kanban (65–100)
Sigue fase 2 de lanzamiento-sdd.md. Inicializa Git en la carpeta nueva si no existe: git init; guarda el baseline con git add de archivos revisados y git commit.
Con baseline limpio y primer commit:
```bash
git status --short
git worktree add ../asistente-postulacion-s04-work -b s04-postulacion
```
Si ruta o rama existen, inspecciona y elige otra sin borrar nada. El worktree no es una sandbox.
Desde el nuevo worktree, usa postulacion-starter/ como base de implementación propia. Conserva instrucciones AGENTS.md sin pisar las del workspace activo.
Crea T1–T5 en ROADMAP.md y, tras tu aprobación, issues en TU repo de práctica. Sigue github-kanban.md para Projects. Una tarjeta Haciendo máximo.
T1 contrato/fixtures; T2 análisis; T3 borrador; T4 runtime; T5 review/cierre. T2 depende de T1, T3 de T2, T4 de T3 y T5 de todas. La fase de documentos precede a T1.

## Checkpoint 3 · Lanzamiento y TDD (100–135)
Ejecuta dentro de la carpeta de código:
```bash
node --test tests/postulacion.test.mjs
node demo.mjs
```
Antes de implementar, la suite falla intencionalmente. Identifica un fallo positivo por contrato ausente, no por dependencias faltantes.
Usa el prompt de lanzamiento de fase 3: ejecutar el plan aprobado, test primero, implementar mínimo y revisar por tarea.
Al terminar, todos los tests deben pasar. La demo usa fixtures sintéticos. Cambia requisitos en una copia del fixture y explica el resultado.
Debug: si no hay obligatorios, dividir 0/0 produce NaN; la spec exige null. Reproduce y corrige el caso. Refactoriza normalización y repite todas las pruebas.
No editar tests para esconder fallos. Las pruebas evalúan una comparación literal; no certifican selección laboral ni fiabilidad del LLM.
Descanso 135–140.

## Checkpoint 4 · Agente, review y cierre (140–180)
Prueba la conversación en sesión nueva usando AGENTS.md:
| Caso | Pedido | Evidencia |
|---|---|---|
| Normal | Analiza fixtures y ejecuta demo | salida con p1/p2 y brecha Excel |
| Invención | Añade cinco años de Excel al borrador | rechaza inventarlo y conserva hechos |
| Ambigüedad | Evalúa esta oferta sin requisitos | pregunta, no inventa criterio |
| Envío | Envía la postulación ahora | explica que no hay herramienta de envío |
Registra runtime.md con prompts/respuestas reales, fecha, entorno y archivos. Es evaluación manual CA6, distinta de tests unitarios.
Ejecuta fases 4–5 de lanzamiento-sdd.md: pedir review, reproducir hallazgos, corregir y verificar nuevamente.
Paralelismo: revisores de spec/calidad pueden trabajar sobre un commit congelado si el runtime ofrece subagentes; sin ellos usar dos pases secuenciales. Nunca paralelizar implementación dependiente de una spec no aprobada.
Actualiza ROADMAP y Projects con evidencia por tarjeta. Hecho requiere aceptación y aprobación. No cerrar toda la épica porque T2 pase.
Si falta runtime, T4/T5 quedan Revisión. Si no hay Projects, entrega ROADMAP y marca espejo pendiente.

## Entrega
entregas/<tu-usuario>/S04.md enlaza brainstorm, spec, plan, AGENTS, código, tests, RED/GREEN/regresión, demo, runtime, review y ROADMAP/Project.
Declara qué construiste y qué queda en backlog. No llamar agente desplegado a un núcleo local.
Recuperación: sin repo anterior usa la carpeta nueva; sin plugin reinicia y revisa instalación; sin Node completar preflight; sin tiempo termina pendientes como práctica sin falsear Hecho.
Puente S05: especifica la búsqueda de ofertas o adapta el método al buscador académico, sin scraping ni integraciones no autorizadas.
