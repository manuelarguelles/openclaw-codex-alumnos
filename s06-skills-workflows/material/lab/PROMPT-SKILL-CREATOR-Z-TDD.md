# Prompt · Endurecer una skill con skill-creator-z, Fase 3 (RED→GREEN→REFACTOR)

Qué demuestra: que `skill-creator-z` (la skill que forjaron en la sesión anterior) ya trae integrado
el ciclo TDD como su Fase 3 — "Validación híbrida RED → GREEN → REFACTOR". No se agrega nada nuevo:
se usa la fase que ya existe, sobre la skill que están construyendo hoy en el capstone de postulación
laboral (o sobre `skill-creator-z` misma, si prefieren endurecer al forjador en vez de lo forjado).

Cómo usarlo en clase: copiar el bloque de abajo, reemplazar `[NOMBRE_SKILL]` por la skill real que
están trabajando, y pegarlo en el chat de OpenClaw (Telegram). Correr primero SIN aplicar nada — el
RED tiene que fallar de verdad antes de escribir instrucciones nuevas.

```text
Usá la skill skill-creator-z para endurecer [NOMBRE_SKILL] aplicando específicamente su Fase 3
(Validación híbrida RED → GREEN → REFACTOR). Seguí el orden exacto, sin saltarte fases:

1. RED — baseline: ejecutá los evals de [NOMBRE_SKILL] SIN la skill activa (o con la versión
   anterior si ya existe una). Registrá salidas, decisiones, errores, omisiones y cualquier
   racionalización literal que aparezca. Incluí al menos un pressure scenario (información
   incompleta, urgencia o tentación de inventar datos).
2. GREEN — corrección mínima: escribí SOLO las instrucciones y recursos que corrigen los fallos
   que acabas de observar en el RED. Nada de reglas genéricas "por las dudas". Si un fallo es de
   forma, dame una receta concreta, no una prohibición vaga.
3. REFACTOR — generalización: repetí la evaluación con casos nuevos y variaciones (no los mismos
   del RED). Buscá sobreajuste, redundancia o pérdida de contexto. Si algo se rompe, decímelo antes
   de darlo por cerrado.

Guardame la evidencia de las tres fases por separado (qué falló en RED, qué cambiaste en GREEN, qué
confirmaste en REFACTOR) — no me des solo el resultado final como si ya estuviera validado.
```

Recordatorio para el docente: si el alumno pega esto sobre una skill que todavía no existe, el RED
va a fallar por "la skill no existe" — es la version más simple del mismo caso que vieron en las
slides 8-12 (el starter de postulación con 15 FAIL). Es el mismo ciclo, otra superficie.
