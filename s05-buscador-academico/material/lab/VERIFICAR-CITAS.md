# Ejemplo desarrollado: verificar un identificador antes de citar

## Hallazgo observado el 11-sep-2026

Una respuesta de OpenAlex asociaba el título «Exploiting Generative AI to Scale up Intelligent Tutoring Systems» con el DOI `10.4230/LIPIcs.ITP.2023.19`.

Al abrir [la página del editor](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITP.2023.19), el título es **MizAR 60 for Mizar 50**. Los metadatos de esa página indican publicación el 26 de julio de 2023 y una contribución al congreso ITP2023 sobre demostración automática de teoremas. Esa discrepancia obliga a revisar el candidato antes de usar su cita.

El JSON observado permanece en el repo docente, sin corregirlo silenciosamente. Que una API entregue un registro y nuestro programa lo procese no demuestra que sus campos sean consistentes. La causa de la discrepancia se investiga por separado; este ejercicio no atribuye mala intención al proveedor.

## Resultado de la revisión

- DOI: coincide con una obra real.
- Título devuelto por el índice: no coincide con el editor.
- Decisión para la búsqueda de tutoría con IA: no usar ese registro como evidencia de tutoría; revisar pertinencia de la obra original.
- Estado: candidato con discrepancia, no referencia académica verificada de tutoría.

## Referencia de la obra identificada

Jakubův, J., Chvalovský, K., Goertzel, Z., Kaliszyk, C., Olšák, M., Piotrowski, B., Schulz, S., Suda, M., y Urban, J. (2023). *MizAR 60 for Mizar 50*. En *14th International Conference on Interactive Theorem Proving (ITP 2023)*, LIPIcs, 268, 19:1–19:22. https://doi.org/10.4230/LIPIcs.ITP.2023.19

Referencia construida a partir de los metadatos del editor. Ajusta convenciones de estilo según el formato requerido. No la presentes como el resultado correcto de la búsqueda de tutoría: sirve para mostrar la verificación y el rechazo de una asociación incorrecta.

## Tu comprobación

Abre un DOI de tu salida. Compara título, autoría, año y tema con el editor. Registra URL, fecha de consulta y decisión: aceptar, revisar o descartar. Si no puedes acceder, marca «no verificado»; no sustituyas la comprobación por una conjetura.
# Caso positivo · metadatos contrastados con la editorial

La consulta concreta a Crossref por DOI produjo la [respuesta original conservada](capturas/crossref-raw-verified.json). El adaptador y la consolidación produjeron la [salida normalizada](capturas/crossref-normalized-verified.json) al reproducir esa captura, sin una segunda petición de red.

```text
GET https://api.crossref.org/works?filter=doi:10.1038/s41598-025-97652-6&select=title,author,published,DOI,URL&rows=1
```

Es una recuperación dirigida por DOI conocido, no un resultado atribuido a la búsqueda temática inicial. Compara `message.items[0].title[0]` → `records[0].title`, `author[].given/family` → `authors[]`, `published.date-parts` → `year` y `DOI` → `doi`. La consulta real y la reproducción terminaron con exit 0.

Referencia revisada: Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting. *Scientific Reports, 15*, 17458. https://doi.org/10.1038/s41598-025-97652-6

Contraste realizado con [la página de la editorial](https://www.nature.com/articles/s41598-025-97652-6): título, cinco autores y publicación del 3-jun-2025 coinciden. El artículo estudia tutoría con IA en física universitaria: es pertinente al tema, pero no demuestra que cualquier tutor de IA sirva igual en cualquier población.

La salida automática conserva `citation_status: unverified`: el script no abrió la editorial. La verificación humana documentada aquí es una capa posterior y no debe atribuirse al programa. Ejercicio: marca qué campos vinieron de la API y cuáles se completaron desde la editorial (revista, volumen y número de artículo).
