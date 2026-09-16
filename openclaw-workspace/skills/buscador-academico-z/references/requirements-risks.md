# Requisitos y riesgos
P0: consulta/periodo/límite; fuentes con estado individual; degradación parcial; deduplicación segura; procedencia/conflictos; ranking explicable; no invención; citation_status; offline determinista; no filtración de secretos.
P1: schema JSON versionado; DataCite/CORE/OpenAIRE/OAI-PMH; ejecución desde cualquier cwd; observabilidad sin PII; contract tests 200/429/503/timeout/payload inválido; integración real reproducible; harness OpenClaw separado; versionado de evidencia.
Riesgos críticos: DOI mal asociado, cita híbrida, secretos en logs, prompt injection en abstract, fixture sintética usada como fuente real, interpretar OA como licencia, rate limits como ausencia de resultados.
Mitigaciones: validar contra fuentes registrales, conservar conflictos, redaction tests, tratar contenido externo como datos, marcar offline, conservar licencia, backoff y errors por fuente.
