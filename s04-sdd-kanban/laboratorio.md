# Laboratorio S04 · Especificar, ordenar y cerrar con evidencia

## Resultado

Convertirás la issue `Mejorar una regla de mi agente` (de S03) en una especificación breve, la llevarás a un tablero con columnas, y la cerrarás mostrando evidencia de cada paso. Todo lo pedirás desde OpenClaw; no necesitas trabajar por terminal.

## Tres logros de hoy

- Convertir una idea en objetivo, alcance y criterio de aceptación.
- Ordenar la tarea en un tablero con estado visible.
- Cerrar la tarea citando evidencia, no una sensación de «ya quedó».

## Ejercicio vivo · Mi primera tarea con método

Usaremos toda la clase la issue creada al final de S03 en `mi-agente-infra`. Envía un pedido, observa la evidencia y espera antes de autorizar cualquier paso irreversible (cerrar, publicar).

| Momento | Pídeselo a OpenClaw | Qué debe devolverte |
|---|---|---|
| Especificar | «Reescribe la issue #N como especificación breve: objetivo, alcance, criterio de aceptación. Muéstrame el texto antes de guardarlo» | Las tres partes, claras y separadas |
| Ordenar | «Crea el tablero del curso, agrega la issue como tarjeta y muéstrame sus columnas» | El tablero con la tarjeta visible en «Por hacer» |
| Ejecutar | «Ejecuta el primer paso, compáralo con el criterio y deja la evidencia como comentario» | Un comentario con qué cambió y cómo se comprobó |
| Cerrar | «Compara la especificación contra la evidencia, muéstrame el dictamen y espera mi autorización» | Primero el dictamen; solo después de tu autorización, la tarjeta en «Hecho» y la issue cerrada |

La misma secuencia sirve para cualquier tarea futura del curso: cambia el tema, no el método.

## Requisito previo

Necesitas el scope `project` en tu autenticación de GitHub CLI:

```bash
gh auth refresh -s project
```

Se abre en el navegador, igual que la autenticación de S03. Nunca pegues un token en Telegram.

## Checkpoint 1 · Especificar

Si no completaste la tarea de S03, primero crea la issue mínima:

> Crea en `mi-agente-infra` una issue titulada con el problema, describiendo qué pasa hoy y qué debería pasar.

Con la issue lista:

> Lee la issue #N y resúmela en una oración. Reescríbela como especificación breve con tres secciones: Objetivo, Alcance (qué sí, qué no) y Criterio de aceptación observable. No la guardes todavía; muéstrame el texto.

Cuando apruebes el texto, pide:

> Guarda exactamente el texto aprobado como `especificacion.md` en la raíz de `mi-agente-infra`. Muéstrame la ruta y solo entonces actualiza la issue con ese archivo.

El agente ejecuta desde la raíz de `mi-agente-infra`:

```bash
gh issue edit N --repo TU_USUARIO/mi-agente-infra --body-file ./especificacion.md
gh issue view N --repo TU_USUARIO/mi-agente-infra
```

`especificacion.md` se crea en este checkpoint con tu texto aprobado; no es un archivo previo del material. Verifica que puedes señalar las tres partes sin releer todo el texto.

## Checkpoint 2 · Ordenar

> Crea un proyecto a mi nombre llamado "Curso OpenClaw+Codex". Añade un campo de selección `Etapa` con Por hacer, Haciendo, Revisión y Hecho. Agrega la issue #N como tarjeta y déjala en Por hacer.

```bash
gh project create --owner @me --title "Curso OpenClaw+Codex" --format json
gh project field-create <numero-proyecto> --owner @me --name Etapa --data-type SINGLE_SELECT --single-select-options "Por hacer,Haciendo,Revisión,Hecho" --format json
gh project item-add <numero-proyecto> --owner @me --url https://github.com/TU_USUARIO/mi-agente-infra/issues/N --format json
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
gh issue comment N --repo TU_USUARIO/mi-agente-infra --body "Paso 1: <qué cambió> · Evidencia: <diff o comparación> · Falta: <si aplica>"
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
gh issue close N --repo TU_USUARIO/mi-agente-infra --reason completed \
  --comment "Criterio de aceptación cumplido: <evidencia final>"
```

Si el criterio queda parcial, la tarjeta se queda en Revisión y anotas el paso pendiente como comentario; no se cierra la issue.

## Entrega

Crea `entregas/<tu-usuario>/S04.md` con:

- número de la issue y su especificación final (objetivo, alcance, criterio);
- URL del tablero y columna final de la tarjeta;
- al menos dos comentarios de evidencia citados o resumidos;
- confirmación de si la issue quedó cerrada o por qué sigue en Revisión;
- una frase: «cerré esta tarea con método porque…».

No pegues tokens ni credenciales.

## Puente a S05

Elige una segunda mejora real del agente o del workspace y escribe su especificación breve **antes** de pedirle a OpenClaw que la ejecute. La llevarás por el mismo ciclo en S05, mientras aprendes a construir un buscador académico.
