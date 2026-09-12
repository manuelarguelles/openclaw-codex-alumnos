# S06 · Crear, componer y evaluar una skill de tu capstone
Usa la mini-spec de S05. El [workflow laboral desarrollado](workflow/README.md) es un espejo, no reemplaza tu proyecto. Entregarás skills propias, casos, salidas y evidencia versionada. Consulta los registros de la sesión para distinguir ensayos observados y pendientes.

## Checkpoint 1 · contrato y RED (bloque 1)
Lee [SPEC](workflow/SPEC.md), [PLAN](workflow/PLAN.md) y [casos](workflow/casos.json). Relaciona entrada, salida y criterio con tu mini-spec de S05.
Pide al agente resolver un caso sin cargar la nueva skill. Guarda la salida real.
Si ya cumple, registra que no hubo RED y diseña un caso significativo más exigente. No simules un fallo.

## Checkpoint 2 · autoría y activación (bloque 2)
Escribe tu SKILL.md desde cero: nombre, description, entradas, instrucciones, salida y límites. Compara después con las tres skills en [workflow/skills](workflow/skills/).
Sigue la instalación por proyecto del [README](workflow/README.md). Si una carpeta ya existe, inspecciónala y elige otro nombre o respáldala antes de reemplazar.
Verifica el nombre y ruta disponibles en la sesión. La documentación oficial explica el descubrimiento local: https://learn.chatgpt.com/docs/build-skills
Selecciona la skill con el selector de la interfaz para probar comportamiento. Luego usa una sesión de prueba sin nombrarla para evaluar activación implícita.
Por Telegram, confirma primero qué runtime expone OpenClaw. Una instalación local en otra aplicación no demuestra disponibilidad en el canal.
Completa EVALUACION.md con positivos, negativos, datos ausentes e instrucciones externas maliciosas. Compara description amplia y acotada con los mismos casos, conserva trazas de selección y repite después del refactor. Guarda dos casos inéditos. Una buena respuesta sin traza no demuestra selección implícita.

## Checkpoint 3 · composición (bloque 3)
Lee [WORKFLOW](workflow/WORKFLOW.md). Ejecuta analizar → redactar → revisar: guarda cada JSON original y pasa la salida de análisis a redacción. Marca dependencias y revisiones independientes.
Ejecuta el validador según README y comprueba además el significado de cada afirmación con el perfil. Estructura correcta no prueba veracidad. Retira el perfil y verifica que se pide información sin redactar.
Haz una revisión de evidencia y otra de formato. Registra si fueron pasadas del mismo agente o subagentes reales.
No otorgues permisos de escritura a dos revisores sobre el mismo archivo.
Consolida hallazgos; corrige o refuta con evidencia. Aplica el patrón a dos o más skills propias de tu capstone.
Recuperación: si no se activa la skill, verifica ruta y selección explícita antes de cambiar su contenido. Si se activa demasiado, acota descripción y repite negativos.

## Checkpoint 4 · autonomía y cierre (bloque 4)
Compara dos tareas: un test de borde local puede ser autónomo; decidir qué experiencia personal incluir requiere información y control humano.
Revisa [GOAL-ENSAYO](workflow/GOAL-ENSAYO.md). Solo inicia /goal después de autorizar el objetivo concreto en una sesión compatible. Conserva comandos, cambio de código, fallo si ocurrió, tests, consumo visible y cierre o pausa. Si falta función o permiso, la ejecución guiada permite practicar, pero no acredita /goal.
Al cierre, guarda en tu repo entregas/s06/: SPEC.md, skill propia/SKILL.md, WORKFLOW.md, CASOS.md y EVALUACION.md con salidas reales.
Aceptación: casos evaluados con razones, entradas faltantes tratadas, cero afirmaciones inventadas y ninguna acción externa.
Marca pendiente toda prueba no realizada. Una plantilla válida no equivale a un workflow funcionando desde Telegram.
Revisa diff y secretos, añade solo rutas elegidas y crea un commit en tu repo. Publica tras revisar su contenido. Repite el README desde un proyecto limpio con un caso conocido y otro inédito. GitHub no despliega automáticamente el agente.
Puente a S07: identificar qué entrada y salida del workflow necesitarán una interfaz.

## Antes de la clase completa
Ensayar activación, RED/GREEN/REFACTOR observado, subagentes, límites y parada real de /goal, recuperación y flujo Telegram. No convertir este checklist en PASS sin ejecución.
