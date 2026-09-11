# S06 · Práctica del adelanto
Entregables disponibles: spec de ejemplo, plantilla de skill, workflow, casos y registro vacío.
No hay una evaluación del runtime ni una ejecución autónoma certificadas.

## Checkpoint 1 · contrato y RED (bloque 1)
Lee SPEC.md y CASOS.md. Elige el ejemplo o adapta ambos a tu mini-spec de S05.
Pide al agente resolver un caso sin cargar la nueva skill. Guarda la salida real.
Si ya cumple, registra que no hubo RED y diseña un caso significativo más exigente. No simules un fallo.

## Checkpoint 2 · autoría y activación (bloque 2)
Lee skill-ejemplo/SKILL.md: la cabecera describe cuándo se usa y el cuerpo cómo actuar.
Para una prueba en Codex, pide al agente copiar esa carpeta como .agents/skills/borrador-postulacion dentro de tu repo de práctica. Si ya existe, inspeccionarla y elegir otro nombre o respaldarla antes de reemplazar.
Verifica el nombre y ruta disponibles en la sesión. La documentación oficial explica el descubrimiento local: https://learn.chatgpt.com/docs/build-skills
Selecciona la skill con el selector de la interfaz para probar comportamiento. Luego usa una sesión de prueba sin nombrarla para evaluar activación implícita.
Por Telegram, confirma primero qué runtime expone OpenClaw. Una instalación local en otra aplicación no demuestra disponibilidad en el canal.
Completa EVALUACION.md con los casos positivos, negativos y de límites. Cambia la descripción y repite. Guarda dos casos inéditos para validación.

## Checkpoint 3 · composición (bloque 3)
Lee WORKFLOW.md. Marca las dependencias y las revisiones independientes.
Haz una revisión de evidencia y otra de formato. Registra si fueron pasadas del mismo agente o subagentes reales.
No otorgues permisos de escritura a dos revisores sobre el mismo archivo.
Recuperación: si no se activa la skill, verifica ruta y selección explícita antes de cambiar su contenido. Si se activa demasiado, acota descripción y repite negativos.

## Checkpoint 4 · autonomía y cierre (bloque 4)
Revisa OBJETIVO.md. Solo inicia /goal si el instructor ha verificado disponibilidad y alcance. Si no, usa ejecución guiada por etapas.
Al cierre, guarda en tu repo entregas/s06/: SPEC.md, skill propia/SKILL.md, WORKFLOW.md, CASOS.md y EVALUACION.md con salidas reales.
Aceptación: casos evaluados con razones, entradas faltantes tratadas, cero afirmaciones inventadas y ninguna acción externa.
Marca pendiente toda prueba no realizada. Una plantilla válida no equivale a un workflow funcionando desde Telegram.
Puente a S07: identificar qué entrada y salida del workflow necesitarán una interfaz.

## Antes de la clase completa
Ensayar activación, RED/GREEN/REFACTOR observado, subagentes, límites y parada real de /goal, recuperación y flujo Telegram. No convertir este checklist en PASS sin ejecución.
