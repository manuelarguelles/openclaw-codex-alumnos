# Escritura y lanzamiento del SDD · prompts por fase

Usa una carpeta NUEVA llamada asistente-postulacion-s04 dentro de tu workspace de práctica. No modificar el repositorio original ni sobrescribir una carpeta existente. Todo el contenido usado aquí es sintético. Sustituye [RUTA] por la ruta real verificada.

## 0. Preparar el entorno
Sigue superpowers-guia.md e identifica runtime, versión y ruta de la skill cargada.
> Lee using-superpowers y brainstorming. Trabaja exclusivamente en [RUTA]/asistente-postulacion-s04. El repo manuelarguelles/asistente-postulacion-laboral es referencia de requisitos, no destino de escrituras. Comprueba que la carpeta sea nueva o inspecciona su estado antes de actuar. No uses datos personales, red ni herramientas de envío.

## 1. Escribir el diseño, todavía sin implementar
> Quiero crear desde cero un asistente que compare un perfil con una oferta y prepare un borrador veraz. Lee caso-postulacion.md. Usa brainstorming para aclarar usuario, entradas, evidencia, errores y límites. Compara construir toda la web, una integración LLM completa o empezar por un núcleo local comprobable. Haz las preguntas necesarias y guarda las decisiones en brainstorm.md. No escribas código aún.

Preguntas para el alumno: ¿cuál es el usuario?, ¿qué es obligatorio?, ¿se permite inferir experiencia?, ¿qué hacemos si falta un dato?, ¿qué se podrá demostrar hoy?
> Con las decisiones confirmadas, redacta spec.md del MVP. Distingue la primera parte ejecutable S04 del backlog. Incluye arquitectura, contrato exacto, criterios CA1–CA7, riesgos, pruebas y recuperación. Muestra supuestos pendientes y espera mi revisión.

La aprobación debe ser real, por ejemplo: «Apruebo esta spec para la práctica local con datos ficticios; no autorizo publicación ni despliegue». No pegar aprobación antes de leer el archivo.

## 2. Planificar y convertir el plan en Kanban
> Usa writing-plans sobre la spec aprobada. Descompón en T1 contrato/fixtures, T2 análisis, T3 borrador, T4 ensayo conversacional y T5 revisión. Cada tarea debe indicar archivos, CA, dependencias, comando, resultado esperado y punto de revisión. Guarda plan.md. No implementes todavía.

> Usa using-git-worktrees para aislar una rama de práctica después de verificar estado y baseline. Crea ROADMAP.md como fuente de verdad. Prepara cinco fichas de issue con descripción y aceptación. Muéstramelas antes de publicarlas en MI repositorio de práctica. GitHub Projects será el espejo y Haciendo tendrá WIP=1.

Consulta github-kanban.md. No crear cinco proyectos: un tablero, cinco tareas.

## 3. Lanzar la ejecución del plan
Esta es la orden de lanzamiento, NO un prompt que salta el diseño:
> La spec y el plan revisados están en [RUTA]. Usa executing-plans y test-driven-development. Ejecuta solamente T1, luego T2 y T3 según dependencias, una tarjeta en Haciendo. Antes de implementar ejecuta tests/postulacion.test.mjs y explica un fallo de comportamiento. Implementa analizarOferta sin cambiar tests para ocultar fallos. Tras cada tarea muestra diff, comando, salida y CA cubiertos. Detente ante cambio de alcance. No publicar, desplegar ni enviar postulaciones.

> Usa systematic-debugging para reproducir la división por cero cuando no hay requisitos obligatorios. Explica la causa. El contrato exige null, no 0 ni 100. Agrega o conserva la regresión y repite la suite. Refactoriza normalización sin cambiar comportamiento; vuelve a probar.

## 4. Conectar la conversación con el núcleo
> Lee AGENTS.md de la práctica. Usa datos sintéticos de fixtures.json y ejecuta demo.mjs. Explica coincidencias y brechas citando sus IDs. Si te pido inventar experiencia, rechaza esa afirmación. Si pego una oferta incompleta, pregunta. Si pido enviar, informa que esta versión no tiene herramienta de envío. Registra prompt, respuesta, comando y resultado reales en runtime.md.

Los tests locales no prueban por sí solos el modelo. Completa los cuatro casos de laboratorio.md en la sesión real. Si falla la carga en OpenClaw, usa Codex e informa el canal probado.

## 5. Revisar, verificar y decidir entrega
> Usa requesting-code-review para contrastar spec, plan, diff y evidencias. Separa cumplimiento de criterios y calidad. Usa receiving-code-review para reproducir hallazgos y corregir los confirmados. Guarda review.md con archivo, problema y prueba de resolución.
> Usa verification-before-completion: ejecuta la suite y demo nuevamente, revisa CA1–CA7 y el inventario de herramientas. Usa finishing-a-development-branch para presentar opciones de integración. Si falta el ensayo runtime, deja T4/T5 en Revisión. Espera autorización explícita para commit/push/PR y para cerrar las issues.

## Lanzar el desarrollo no equivale a desplegar
S04 lanza un plan y produce un núcleo local. Desplegar el MVP web requiere decisiones de proveedor/autenticación, presupuesto, pruebas de aislamiento y una aprobación separada. Esos criterios están en la spec docente; no activar servicios pagados como parte implícita de esta práctica.
