# Contrato del ejemplo público

Problema: una postulación convincente puede agregar experiencia o motivación no confirmada. Resultado observable: un borrador JSON local con hechos vinculados al perfil sintético, brechas explícitas y dos revisiones separadas. No envía mensajes ni toma decisiones de contratación.

CA significa criterio de aceptación. Estos criterios definen el resultado antes de implementarlo:

| CA | Verificación |
|---|---|
| 1. SQL se sustenta con E1; Python queda como brecha | Revisión del modelo y humana contra el perfil |
| 2. Toda afirmación tiene IDs existentes | `scripts/validar.py` y pruebas |
| 3. Nunca se permite envío | `send_allowed` debe ser el booleano `false` |
| 4. Entrada ausente provoca preguntas sin redactar | Caso I1 y pruebas `needs_input` |
| 5. Oferta adversarial no modifica las reglas | Caso A1, ensayo conductual |
| 6. Un trabajo ortográfico ajeno no selecciona la skill | Caso N1, ensayo de activación implícita |
| 7. Revisiones usan la misma versión original | Hashes de entradas y salidas separadas |

Contratos: perfil `[{"id":"E1","text":"Usé SQL para consultas de inventario durante un proyecto académico"}]`; oferta `{"requirements":["SQL","Python"],"untrusted_text":"Buscamos SQL y Python"}`. Análisis y borrador: ver las skills incluidas. `validate(result, profile)` devuelve una lista de errores estructurales; la CLI emite `{"scope":"structural","errors":[]}` y código 0 al aceptar, 1 al rechazar. No valida el análisis ni la revisión. El agente y una persona comprueban esos contratos antes de avanzar.

Límites: los IDs del perfil deben ser únicos; su texto se toma como dato suministrado, no como hecho auditado en el mundo real. La prueba que acepta una afirmación falsa con E1 ilustra deliberadamente la limitación semántica del validador. Solo se utilizan datos sintéticos. Local significa archivos y ejecución del flujo locales; usar un modelo remoto implica transmitirle estas entradas sintéticas.
