# Workflow de ejemplo · contrato conceptual

No es un orquestador ejecutable ni crea subagentes por sí mismo.

1. Validación: entrada perfil + oferta. Salida datos suficientes o pregunta. Si faltan, detenerse.
2. Análisis: entrada datos validados. Salida requisitos, evidencia y brechas.
3. Redacción: entrada análisis. Salida borrador local con tabla afirmación/evidencia.
4. Revisión después de redactar, opcionalmente en paralelo:
   - Revisor de evidencia: identificar afirmaciones sin respaldo. Solo lectura.
   - Revisor de formato: identificar omisiones del formato solicitado. Solo lectura.
5. Consolidación: autor contrasta cada hallazgo con SPEC.md y corrige lo justificado.
6. Verificación: repetir casos, registrar fallos o cumplimiento.
7. Integración: revisión humana del cambio versionado. Ningún envío o despliegue.

## Mensaje del revisor de evidencia
Lee SPEC.md, perfil y borrador. Señala afirmaciones sin evidencia con frase exacta y campo faltante. No reescribas ni publiques. Si no hay hallazgos, explica qué revisaste y qué no puedes verificar.

## Responsabilidades
El autor escribe. Los revisores no modifican los mismos archivos.
Paralelizar solo si existen subagentes habilitados y tareas independientes.
Si no existen, hacer dos pasadas guiadas y registrar que no hubo delegación real.
