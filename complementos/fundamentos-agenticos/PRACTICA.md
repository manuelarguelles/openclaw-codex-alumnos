# Práctica · Diseña una solución que puedas explicar

No requiere instalar modelos ni enviar mensajes a servicios.

1. Elige una petición: «encuentra y guarda tres estudios sobre tutoría con IA».
2. Dibuja canal → Gateway → agente y sesión → modelo → herramientas → resultado.
3. Marca pasos fijos: consultar, unificar formatos, quitar duplicados. Marca una decisión variable: reformular consulta si falta evidencia.
4. Incluye una revisión humana: confirmar población objetivo antes de guardar.
5. Si delegas, escribe encargo, entrada, salida y límite para dos revisores. No les permitas escribir el mismo archivo simultáneamente.
6. Especifica cuándo termina, pregunta o se detiene.
7. Diseña una prueba de respaldo de modelo: qué fallo provocarías en un entorno separado y qué evidencia demostraría que Gemini se usó.

## Criterio de aceptación

Un compañero puede identificar quién decide, quién ejecuta, dónde se conserva el estado y qué cambio observable acepta. Puede explicar por qué dos llamadas API no son necesariamente dos agentes. Distingue autenticación probada de failover probado.

## Recuperación

Si no puedes señalar una decisión dinámica del modelo, representa tu núcleo como workflow. Si no puedes separar entradas/salidas de subagentes, comienza con un solo agente. Si no tienes credencial o cuota, conserva el plan de prueba Gemini como pendiente, sin marcarlo ejecutado.
