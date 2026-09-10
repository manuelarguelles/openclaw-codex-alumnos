# Laboratorio S04 · Ciclo SDD completo con Superpowers
## Resultado
Evoluciona la issue de S03 «Mejorar una regla de mi agente» en mi-agente-infra. Entrega diseño, spec, plan, implementación con pruebas, revisión y tablero actualizado. Usa Telegram cuando el runtime real exponga las skills; si no, usa Codex sobre el mismo snapshot y registra el canal verificado.

## Material
- superpowers-guia.md: instalación y las 14 skills.
- plantillas.md: estructura de brainstorming, spec, plan, review, ROADMAP y entrega.
- starter/: regla vaga, función incompleta y 12 tests.
- github-kanban.md: comandos completos de Projects/issue.
- Guion y solución del instructor se muestran en la demo, no se copian como entrega.
Prerrequisitos: snapshot sanitizado de S03, Git, Node.js 22+, Codex autenticado y gh si usarás Projects. No copiar secretos ni reemplazar el AGENTS.md del workspace activo.

## Checkpoint 0 · Instalar y comprobar
Seguir superpowers-guia.md: Plugins → Superpowers; abrir sesión nueva.
Prompt: «Identifica las skills instaladas de Superpowers, lee brainstorming y dime la ruta. Trabajaremos solo en [RUTA]/mi-agente-infra. No implementes hasta revisar el diseño».
Evidencia: versión, entorno, ruta de skill, respuesta pertinente. Si no se carga, completar recuperación; un archivo descargado no prueba activación.

## Checkpoint 1 · Idea → brainstorming → spec (0:00–1:00)
1. Lee tu issue y conserva el problema observable. Si falta, usa el starter: «Trabaja bien y avísame cuando termines» no define evidencia.
2. Prompt: «Usa brainstorming. ¿Qué significa terminado? Compara regla sola, recordatorio por prompt y regla con reporte verificable. No cambies archivos del agente».
3. Responde las preguntas; guarda decisiones y alternativa elegida en brainstorm.md.
4. Prompt: «Para este ejercicio usa el ciclo documental completo aunque la mejora sea pequeña. Redacta spec.md con objetivo, alcance, entradas/salidas, errores, criterios numerados, pruebas y límites».
5. Revisa y aprueba expresamente la spec antes del plan. No uses la aprobación del ejemplo como si fuera tuya.

Contrato sugerido del caso: evaluarCierre recibe criterios no vacíos/únicos, exactamente una evidencia PASS con referencia por criterio, revisión APROBADA y autorización true. Devuelve Hecho/Revisión y razones; no cierra nada.
CA1: positivo válido; CA2: evidencia incompleta/fallida; CA3: revisión/autorización; CA4: tipos/listas/duplicados; CA5: conducta del agente y evidencia verdadera.

## Checkpoint 2 · Plan → aislamiento → Kanban (1:05–1:40)
Prompt: «Usa writing-plans sobre la spec aprobada. Tareas pequeñas: contrato probado, regla persistente y prueba del agente, revisión/cierre. Indica archivos y comando por tarea».
Conserva plan.md. Cada tarea tiene CA asociados y resultado verificable.
Pide using-git-worktrees: comprobar estado primero, crear rama/carpeta de práctica y repetir pruebas de baseline. Comandos explicados:
```bash
git status --short
git worktree add ../mi-agente-s04 -b s04-regla
```
No ejecutar si la rama/ruta existen: inspeccionar y elegir una nueva ruta. Trabaja desde el nuevo worktree.
Lleva el starter a una subcarpeta nueva de práctica; no sobreescribas tus archivos de S03.

Crea ROADMAP.md con una tarjeta y cuatro etapas. Es la fuente de verdad; Projects es espejo. Aplica WIP=1: antes de pasar a Haciendo, contar tarjetas; si ya hay una, resolverla o devolverla a Por hacer con explicación.
Sigue github-kanban.md para crear Etapa y vincular la issue. Guarda cambios de ROADMAP al pasar Por hacer → Haciendo → Revisión → Hecho; cada transición lleva motivo y evidencia.
No necesitas cuatro tarjetas: es una tarea que cambia de estado.

## Checkpoint 3 · Build con TDD, debugging y prueba del agente (1:40–2:15)
Desde la carpeta starter de práctica:
```bash
node --test tests/cierre.test.mjs
```
Prompt: «Usa test-driven-development. Ejecuta el test antes de implementar. Explica por qué falla el caso positivo. Implementa el contrato de la spec sin cambiar los tests para hacerlos pasar».
RED esperado del starter: 11 PASS/1 FAIL; GREEN esperado de implementación correcta: 12 PASS.
El agente escribe JavaScript; tú debes explicar qué condición rechaza cada caso.
Refactor: pedir simplificar la validación sin cambiar contrato; ejecutar la suite otra vez.
Debugging: «Usa systematic-debugging: reproduce qué ocurre con una lista vacía y every(). Formula una hipótesis, compruébala y demuestra que nuestra implementación rechaza el caso».
El error reproducible enseña causa raíz; no introducirlo en tu agente activo.

Pide mejorar únicamente la regla de finalización de AGENTS.md del snapshot. Debe exigir criterio, comando, salida real, referencia, estado parcial y autorización de cierre.
Prueba la conducta en sesión nueva del runtime y registra:
| Caso | Pedido | Evidencia requerida |
|---|---|---|
| Permitido | Ejecuta los tests locales y reporta | Comando, salida, conteo y ruta |
| Fallo | Con un test fallido, indica si puede cerrarse | PARCIAL/Revisión, sin cierre |
| Ambiguo | «Mejora todo» sin criterio | Pregunta de alcance antes de cambiar |
| Sin permiso | Prepara cierre; no autorizo publicar | Espera y no publica |
El validador no verifica que las referencias sean verdaderas ni que el modelo obedezca. Abre las fuentes y compara; registrar prompts/respuestas reales es obligatorio para CA5.

## Checkpoint 4 · Review → verificación → cierre (2:20–3:00)
1. Prompt: «Usa requesting-code-review. Revisa spec, plan, diff y evidencia: primero cumplimiento de CA1–CA5, después calidad. Indica archivo y problema».
2. Prompt: «Usa receiving-code-review. Reproduce cada hallazgo, corrige lo confirmado y explica los cambios fuera de alcance que no corresponden».
3. Guarda review.md: hallazgo, severidad, decisión, prueba de resolución.
4. Prompt: «Usa verification-before-completion; ejecuta las pruebas ahora, abre referencias y compara cada criterio». No aprobar con evidencia anterior a la última edición.
5. Si hay subagentes reales, demostración de implementador + revisor de spec + revisor de calidad. Si no, checkpoints secuenciales; no inventar agentes.
6. Usa finishing-a-development-branch para proponer integrar, PR o conservar rama. Revisa antes de autorizar efectos externos.
7. Solo después de aprobación, sincroniza ROADMAP/Projects a Hecho y cierra la issue con evidencia. Si falta CA5 u otro criterio, permanece en Revisión.

## Entrega
Crea entregas/<tu-usuario>/S04.md con enlaces a brainstorm.md, spec.md, plan.md, regla modificada, tests, evidencias RED/GREEN/regresión/runtime, review.md y ROADMAP.md.
Incluye versión/ruta de Superpowers, canal comprobado, issue, estado final, aprobación y límites pendientes.
Puedes entregar una tarea en Revisión con bloqueo explicado; no representa una tarea cerrada ni permite afirmar criterios cumplidos.

## Puente S05
Especifica una segunda mejora del asistente/buscador académico antes de pedir ejecución. Reutiliza el método; en S06 profundizarás en creación de skills y workflows.

## Recuperación
Sin repo S03: usar starter en carpeta nueva y documentar recuperación.
Sin plugin en sesión: reiniciar sesión y comprobar instalación/usuario efectivo.
Sin Projects: conservar ROADMAP como fuente de verdad, registrar espejo pendiente.
Sin Node: completar instalación previa; no marcar TDD probado.
Si el tiempo se agota, terminar checkpoints pendientes como práctica; no omitir spec, plan, TDD ni review para declarar completitud.
