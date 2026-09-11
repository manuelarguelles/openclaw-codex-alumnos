# S05 · Práctica del adelanto
Estado: ejercicios de diseño y datos sintéticos disponibles. No incluye un buscador multifuente ejecutable.

## Preparación
Abre el deck HTML y estos archivos desde el repo de alumnos. Puedes pedir al agente por Telegram que te ayude a leerlos y escribir tu entrega. Si el canal no está disponible, trabaja con los mismos archivos en Codex y anota esa diferencia. No instales la skill privada tesis-buscador.

## Checkpoint 1 · pregunta y contrato (bloque 1)
Reescribe «Busca papers de IA» con tema, periodo, límite y evidencia requerida.
Completa entradas, salida y exclusiones de MINI-SPEC.md.
Aceptación: un compañero puede decir cuándo termina la búsqueda.

## Checkpoint 2 · fuentes y formato (bloque 2)
Dibuja cinco ramas de descubrimiento: arXiv, Crossref, Semantic Scholar, OpenAlex y CORE.
Sitúa Unpaywall después de disponer de DOI.
Explica qué datos salen del proceso local y cuáles deben quedarse.
Define campos comunes: título, autores, año, DOI/identificador, fuentes, errores.
No presupongas credenciales. Esta actividad diseña el contrato, no llama APIs.

## Checkpoint 3 · consolidación y pruebas (bloque 3)
Abre REGISTROS-DEMO.json. Son tres filas sintéticas, no papers reales.
Consolida por id y conserva procedencias. Escribe el resultado en consolidacion.json.
Ordena por año descendente y explica por qué esa regla no mide calidad científica.
Escribe tres tests en pruebas.md: duplicado, fuente caída y cero resultados.
Para simular una caída, declara fuente-B no disponible y especifica el resultado parcial y el error.
Cita incompleta: explica por qué no puedes convertir estos registros en bibliografía académica real.
Aceptación: una fila por id, procedencias sin pérdida, error visible y ninguna cita inventada.

## Checkpoint 4 · transferencia y entrega (bloque 4)
Elige capstone y completa MINI-SPEC.md. Si eliges postulación, sustituye procedencia del paper por evidencia del perfil, sin buscar ni enviar postulaciones.
Guarda en tu repo, entregas/s05/: MINI-SPEC.md, consolidacion.json, pruebas.md y notas.md.
En notas.md registra qué hiciste manualmente, qué hizo el agente y qué falta probar con red.
Recuperación: si te bloqueas, resuelve primero dos filas del mismo id. Luego añade el segundo id.

## Contrato de la sesión completa, todavía pendiente
Adaptación pública de tesis-buscador, adaptadores reales, tratamiento de límites por API, resultado con citas verificadas, pruebas automatizadas y ensayo del flujo desde Telegram. No presentar este ejercicio como sustituto de esos entregables.
