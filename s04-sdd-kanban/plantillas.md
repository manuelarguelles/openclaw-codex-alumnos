# Plantillas de trabajo S04
Crea estos archivos en tu carpeta de práctica; sustituye las consignas por decisiones reales.

## brainstorm.md
Problema observable / pregunta principal / respuestas de la persona / 2–3 alternativas con tradeoffs / alternativa elegida y motivo / quién aprobó y qué aprobó.

## spec.md
Objetivo y audiencia.
Incluye / excluye.
Arquitectura y flujo de datos.
Contrato: entradas, salidas y errores.
Criterios CA1…CAn: condición observable y evidencia que la prueba.
Restricciones, riesgos, recuperación y límites.
Decisión de aprobación (no rellenar en nombre de la persona).

## plan.md
Objetivo / arquitectura / stack / enlace a spec.
Por tarea: CA cubiertos / archivos exactos / interfaz / pasos / prueba RED / resultado GREEN / revisión.
Casillas pendientes hasta ejecutar cada paso; no tratar una lista marcada como evidencia suficiente.

## review.md
Versión revisada y alcance.
Cumplimiento por CA, después calidad.
Hallazgo / severidad / archivo / reproducción / respuesta / prueba posterior.
Dictamen: aprobado o cambios requeridos. Quién revisó.

## ROADMAP.md
Fuente de verdad: este archivo. Projects se sincroniza en cada checkpoint.
WIP Haciendo = 1.

| Tarjeta | Etapa | Criterios | Evidencia | Bloqueo |
|---|---|---|---|---|
| Mejorar una regla de mi agente | Por hacer | CA1–CA5 | Spec aprobada cuando corresponda | Registrar si existe |

Historial: fecha / de → a / motivo / evidencia.
No cambiar a Hecho hasta completar criterios, review y autorización.

## reporte-cierre.json (ejemplo de formato; no evidencia real)
```json
{
  "criterios": ["CA1"],
  "evidencias": [
    {"criterio": "CA1", "resultado": "PASS", "referencia": "evidencias/prueba-real.txt"}
  ],
  "revision": "PENDIENTE",
  "autorizacion": false
}
```
La referencia es ilustrativa: debe reemplazarse por una salida real. Una ruta escrita no demuestra que el archivo exista.

## evidencias/runtime.md
Runtime y versión / usuario de ejecución sin datos sensibles / skill y ruta.
Por caso: prompt, respuesta real, comandos, resultados, revisión humana.
Separar resultado esperado y resultado observado. No registrar PASS hasta ejecutar.

## S04.md
Enlaces a los artefactos, hash revisado, canal probado, versiones, checklist CA, aprobación y estado final.
Si faltan pruebas de Telegram, declarar qué sí se verificó y qué no.
