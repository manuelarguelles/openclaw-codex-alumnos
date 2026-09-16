# S05 · Glosario inicial

Glosario inicial · 1 / 7

Un artículo se reconoce por sus datos y su identificadorPaper y preprint — Paper = artículo académico. Preprint = versión compartida antes de la revisión por pares; no implica que ya haya sido validada.

Registro y metadatos — Registro = ficha de un trabajo. Cada campo contiene un dato. Metadatos = título, autores, año y otros datos que describen el trabajo.

DOI · Digital Object Identifier — Identificador persistente de un trabajo. El enlace doi.org/… permite localizarlo; tener DOI no demuestra calidad científica.

★Ejemplo real: 10.4230/LIPIcs.ITP.2023.19

S05 · v0.32 / 55

Glosario inicial · 2 / 7

Una API entrega datos que traducimos a un formato comúnAPI · interfaz entre programas — Permite que un programa pida datos a otro. Ejemplo: el buscador pide artículos a Crossref.

GET y parámetros — GET pide información. Los parámetros precisan la petición: query indica qué buscar y rows cuántos registros pedir; %20 representa un espacio.

Adaptador y normalización — El adaptador traduce la respuesta de cada fuente. Normalizar pone sus campos en un formato común, sin inventar datos.

S05 · v0.33 / 55

Glosario inicial · 3 / 7

JSON permite guardar resultados sin confundir ausencia con evidenciaJSON · formato de datos — Organiza claves y valores: {"titulo": "Tutoría con IA", "doi": null}. Ejemplo inventado para leer el formato.

null y esquema — null = sin valor; {} = objeto o ficha; [] = lista. El esquema organiza la salida: registros, fuentes y errores.

Procedencia y cita académica — Procedencia = de dónde salió un dato. Una cita identifica el trabajo para consultarlo. APA es un estilo para presentar esas referencias.

S05 · v0.34 / 55

Glosario inicial · 4 / 7

Consolidar y ordenar permite comparar lo que encontraron las fuentesAgregación y deduplicación — Agregar reúne resultados. Deduplicar une fichas del mismo trabajo y conserva sus fuentes; dos títulos parecidos pueden ser trabajos distintos.

Ranking léxico — Ordena por coincidencias de palabras con la consulta. Ranking = orden por una regla de relevancia; no certifica calidad científica. Bibliometría = medición de publicaciones y citas.

Acceso abierto y enriquecimiento — Acceso abierto permite leer el texto sin pagar. Enriquecer añade datos a una ficha: por ejemplo, localizar una versión abierta desde su DOI.

S05 · v0.35 / 55

Glosario inicial · 5 / 7

Los límites de una fuente deben quedar visibles en la respuestaTimeout · tiempo de espera agotado — La fuente no respondió dentro del plazo. Conservamos las respuestas de las otras fuentes y registramos el fallo.

Rate limit y HTTP 429 — Rate limit = límite de peticiones. HTTP es el protocolo de intercambio web; 429 indica demasiadas peticiones. Esperamos y acotamos los reintentos.

Fixture · recordatorio para la práctica — Dato preparado para probar un caso. Offline usa datos locales; live consulta servicios reales. Una fixture no demuestra acceso a una API.

S05 · v0.36 / 55

Glosario inicial · 6 / 7

La skill indica cuándo actuar y cómo seguir el procedimientoFrontmatter y description/trigger — Frontmatter = bloque inicial con nombre y descripción. Description explica cuándo usar la skill; trigger es la situación que la activa.

Script, asset y CLI — Script = archivo de código ejecutable. Asset = recurso reutilizable. CLI = interfaz de línea de comandos; aquí pedimos al agente ejecutar y explicar.

Capstone y mini-spec — Capstone = tu proyecto integrador. Mini-spec = una página con usuario, función, alcance y criterios observables para aceptar el resultado.

S05 · v0.37 / 55

Glosario inicial · 7 / 7

Buscar por significado no autoriza a inventar una respuestaEmbedding · representación numérica — Representa un texto con números para comparar similitud de significado. Una similitud alta no prueba que dos afirmaciones sean equivalentes.

Búsqueda semántica — Busca por significado, aunque cambien las palabras: «tutoría inteligente» y «AI tutoring». En esta sesión se contrasta con búsqueda literal.

RAG · generación apoyada en recuperación — Primero recupera información; después genera una respuesta apoyada en ella. Hay que comprobar que las fuentes sostienen cada afirmación.

S05 · v0.38 / 55
