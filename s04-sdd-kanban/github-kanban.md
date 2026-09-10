# GitHub Kanban · Projects gratuito y tareas del asistente

GitHub Free incluye Issues y Projects: https://github.com/pricing (verificado 10-sep-2026). No exige GitHub Team para este tablero. Actions, Codespaces, APIs LLM y Railway tienen condiciones/cuotas propias; no se deduce que sean ilimitados.

Una issue es una ficha de tarea. Un Project organiza varias fichas, incluso de distintos repositorios. Un repositorio guarda archivos. No son la misma cosa.

## Referencia visual
La slide del tablero contiene una captura oficial: https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/changing-the-layout-of-a-view
Sus columnas pertenecen al ejemplo de GitHub, no son las etapas por defecto ni el tablero de nuestra clase.
Nuestra vista se llama Asistente de postulación S04 y se agrupa por Etapa: Por hacer, Haciendo, Revisión, Hecho.

## Crear tareas desde el plan
En TU repositorio nuevo de práctica, Issues → New issue. Para T2:
- Título: [T2] Comparar oferta con perfil y citar evidencia.
- Descripción: implementar analizarOferta en analizar-oferta.mjs, según spec.md.
- Aceptación: CA1–CA3 y CA5; tests de coincidencias, brechas, tipos y cobertura.
- Dependencia: T1. Evidencia: comando, salida y commit revisado.
Crear T1–T5 según plan.md. Guardar los números reales. No escribir en el repo de Manu desde cuentas de alumnos.
Alternativa CLI (solo después de aprobar título, repo y contenido):
```bash
gh issue create --repo TU_USUARIO/asistente-postulacion-s04 --title "[T2] Comparar oferta con perfil" --body "Contrato: spec.md CA1-CA3 y CA5. Depende de T1. Evidencia: tests/postulacion.test.mjs."
```
Antes de usar gh project, comprobar autenticación y habilitar scope si falta:
```bash
gh auth status
gh auth refresh -s project
```
Alternativa web: perfil → Projects → New project → Board. Agrega las issues, crea Etapa de selección única y usa Group by → Etapa. Guarda la vista. WIP=1 se controla revisando cuántas tarjetas están en Haciendo.

# Comandos y evidencia

Referencia operativa. Ejecuta dentro del repositorio de práctica. Sustituye usuario, N y los IDs por valores observados; no pegues los placeholders literalmente.
ROADMAP.md es la fuente de verdad de S04; Projects es espejo. WIP de Haciendo: 1. Sin autorización, no cerrar ni publicar.

## Checkpoint 2 · Ordenar

> Crea un proyecto a mi nombre llamado "Asistente de postulación S04". Añade un campo de selección `Etapa` con Por hacer, Haciendo, Revisión y Hecho. Agrega la issue #N como tarjeta y déjala en Por hacer.

```bash
gh project create --owner @me --title "Asistente de postulación S04" --format json
gh project field-create <numero-proyecto> --owner @me --name Etapa --data-type SINGLE_SELECT --single-select-options "Por hacer,Haciendo,Revisión,Hecho" --format json
gh project item-add <numero-proyecto> --owner @me --url https://github.com/TU_USUARIO/asistente-postulacion-s04/issues/N --format json
gh project field-list <numero-proyecto> --owner @me --format json
```

Un proyecto nuevo trae `Todo`, `In Progress` y `Done` en el campo `Status`; no trae las cuatro etapas del curso. Por eso el segundo comando es obligatorio.

Guarda el ID del proyecto (`PVT_ID`), el ID devuelto por `item-add` (`ITEM_ID`), el ID del campo `Etapa` y el ID de cada opción. Primero mueve la tarjeta a Por hacer:

```bash
gh project item-edit --project-id <PVT_ID> --id <ITEM_ID> \
  --field-id <FIELD_ID_ETAPA> --single-select-option-id <OPTION_ID_POR_HACER>
```

Antes de empezar el primer paso, mueve la tarjeta:

> Mueve la tarjeta de la issue #N a la columna Haciendo.

```bash
gh project item-edit --project-id <PVT_ID> --id <ITEM_ID> \
  --field-id <FIELD_ID> --single-select-option-id <OPTION_ID_HACIENDO>
```

También puedes abrir el proyecto, crear una vista de tablero, agruparla por `Etapa` y arrastrar la tarjeta a mano; ambas formas son válidas.

## Checkpoint 3 · Ejecutar con evidencia

> Ejecuta el primer paso pequeño de la especificación. Antes de guardar cualquier cambio, muéstrame qué vas a modificar y por qué cumple ese paso. Después de aplicarlo, compara el resultado con el criterio de aceptación y dime si ya se cumple o falta otro paso.

```bash
gh issue comment N --repo TU_USUARIO/asistente-postulacion-s04 --body "Paso 1: <qué cambió> · Evidencia: <diff o comparación> · Falta: <si aplica>"
```

Repite el paso pequeño → chequeo → evidencia tantas veces como haga falta hasta cubrir el criterio completo. Cuando la evidencia esté completa, mueve la tarjeta a Revisión:

```bash
gh project item-edit --project-id <PVT_ID> --id <ITEM_ID> \
  --field-id <FIELD_ID> --single-select-option-id <OPTION_ID_REVISION>
```

Si algún paso toca credenciales, datos personales, otro repositorio o un criterio poco claro, el agente debe detenerse y preguntar. Verifica que eso haya pasado al menos una vez durante la práctica; si nunca pasó, pide un paso que sí lo dispare a modo de prueba.

## Checkpoint 4 · Cerrar con evidencia

> Compara la especificación de la issue #N contra los comentarios de evidencia. Dime si el criterio de aceptación se cumple completo, parcial o no se cumple, y por qué.

Si el criterio se cumple completo:

```bash
gh project item-edit --project-id <PVT_ID> --id <ITEM_ID> \
  --field-id <FIELD_ID> --single-select-option-id <OPTION_ID_HECHO>
gh issue close N --repo TU_USUARIO/asistente-postulacion-s04 --reason completed \
  --comment "Criterio de aceptación cumplido: <evidencia final>"
```

Si el criterio queda parcial, la tarjeta se queda en Revisión y anotas el paso pendiente como comentario; no se cierra la issue.
