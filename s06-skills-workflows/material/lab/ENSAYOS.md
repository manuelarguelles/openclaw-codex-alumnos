# Ensayos del recorrido docente · 12-sep-2026

Estos resultados corresponden a datos sintéticos y al entorno docente. Cada estudiante debe conservar sus propias salidas y comprobaciones.

## Selección y recuperación

La comparación de descripciones A/B conservó los mismos prompts: A abrió una skill laboral para corregir ortografía; B excluyó ese caso y conservó el positivo laboral. Es una observación por combinación, no una estimación estadística de eficacia.

El control sin la skill objetivo produjo una carta, sin el contrato JSON exigido por el ejercicio. Una copia de las skills bajo `not-installed/skills` tampoco se descubrió en ese caso. Al colocar los mismos archivos en `.agents/skills`, una sesión nueva sí cargó las skills y produjo el contrato. Esto demuestra un fallo de ruta; no exige cambiar de modelo.

Para reproducir el diagnóstico usa carpetas nuevas, guarda el prompt idéntico y compara los registros de lectura. Ver un archivo en el explorador no prueba que forme parte del catálogo del agente.

## Datos ausentes y formato

El caso I1 detiene la redacción y pide el perfil. Una salida histórica añadió explicación fuera del JSON y el validador la rechazó. En esta ronda, original, versión de desarrollo y refactor produjeron JSON válido en cinco repeticiones cada una. Ese resultado no borra el fallo histórico ni garantiza futuras respuestas.

Conserva la respuesta íntegra: pasa el archivo completo por `scripts/validar.py`. Si falla, guarda el error y solicita una nueva versión, con esta precisión:

> La respuesta final es un único objeto JSON del contrato. Las preguntas y explicaciones necesarias van dentro de sus campos. Si falta el perfil, termina con needs_input y preguntas; no redactes.

No recortes el primer objeto JSON para simular que la respuesta original era válida. Una respuesta needs_input, aunque sea válida, detiene el flujo antes de redactar.

## Composición y revisión

Se guardó un análisis P1 y la etapa de redacción consumió exactamente esa versión. Ante I1, el análisis devolvió needs_input y no se abrió la etapa de redacción.

Dos revisores independientes examinaron una misma versión de borrador con focos de evidencia y formato. Sus intervalos tuvieron 25,021 segundos de solapamiento y los hashes de las entradas permanecieron iguales. Ambos aprobaron su foco; un PASS estructural no acredita veracidad por sí solo.

## Objetivo autónomo

El instructor inició un objetivo nativo autorizado y ejecutó el ejemplo de [GOAL-ENSAYO](workflow/GOAL-ENSAYO.md) en una copia. Una nueva prueba detectó la repetición de un ID de evidencia: 12 pruebas, un fallo. Tras una corrección mínima, las 12 pasaron y se detuvieron los cambios del ejercicio en la primera ronda, dentro del límite de tres.

La solución y las trazas completas permanecen en el material docente. El objetivo general de preparación continuó con otras tareas; su estado no se confunde con la parada del ejercicio. No se ensayó el botón de pausa de la interfaz.

## Comprobaciones independientes

Las pruebas anteriores no acreditan por sí mismas recepción y respuesta desde Telegram ni disponibilidad de todas las cuentas y canales del alumnado. Antes de clase, comprueba el canal y el acceso a la copia que usarás. Los estados de preparación y los registros del docente deben indicar esa comprobación por separado.
