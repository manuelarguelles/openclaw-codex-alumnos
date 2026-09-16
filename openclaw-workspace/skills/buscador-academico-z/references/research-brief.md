# Research brief — buscador-academico-z
Fecha de consulta: 2026-09-15.
Fuentes y hechos principales:
- OpenAlex: índice multidisciplinar central, filtros, entidades, citas y locations OA; datos CC0; endpoint comprobado HTTP 200. https://docs.openalex.org/
- Crossref: DOI/metadatos editoriales; polite pool con mailto opcional; HTTP 200. https://api.crossref.org/
- DataCite: tesis, datasets, software, informes y objetos DOI de repositorios. https://api.datacite.org/
- Unpaywall: DOI → ubicaciones OA; requiere email; HTTP 200. https://unpaywall.org/products/api
- CORE/OpenAIRE/OAI-PMH: tesis, repositorios y cosecha; licencia depende de cada objeto. https://core.ac.uk/documentation/api ; https://graph.openaire.eu/develop/api.html ; https://www.openarchives.org/OAI/openarchivesprotocol.html
- arXiv: preprints y texto completo; límites estrictos; HTTP 200. https://info.arxiv.org/help/api/index.html
- Europe PMC/PubMed: biomédica y texto completo estructurado en PMC. https://europepmc.org/RestfulWebService
- Semantic Scholar: enriquecimiento semántico/citas; consulta anónima observada HTTP 429; usar caché/backoff. https://www.semanticscholar.org/product/api
- APA 7: séptima edición (2020); autor-fecha, DOI como enlace, et al. desde primera cita para 3+ autores, hasta 20 autores listados, sin ciudad editorial. APA.org bloqueó acceso directo en esta consulta; contrastar con guía institucional y consultar siempre reglas de universidad/revista. https://apastyle.apa.org/style-grammar-guidelines/citations
Soluciones existentes evaluadas: GROBID (Apache-2.0) para PDF→TEI; Citation.js (MIT) y CSL para render; PyAlex (MIT); Pyserini/Vespa para ranking; RapidFuzz/Splink para similitud/linkage; skill local recuperar-papers para OA/verificación. No existe una solución única; conviene arquitectura modular.
Límites: APIs, licencias, cobertura y cuotas cambian; Google Scholar no ofrece API pública general; Scopus/WoS/Dimensions/ProQuest/WorldCat/Lens requieren licencia o acceso restringido. Separar hecho, inferencia y decisión; conservar URL, fecha y versión.
