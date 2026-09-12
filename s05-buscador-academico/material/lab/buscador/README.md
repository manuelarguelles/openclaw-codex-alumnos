# Buscador académico reproducible

Ejemplo docente en Python estándar. Consulta cinco índices independientes (Crossref, arXiv, Semantic Scholar, OpenAlex y CORE), normaliza metadatos, deduplica solo por DOI o ID exacto de fuente y ordena por coincidencia léxica explicable. Unpaywall es enriquecimiento posterior por DOI.

## Recuperación offline

Desde esta carpeta:

```bash
python3 scripts/buscar.py "AI tutoring" --sources crossref arxiv --limit 3 --year-from 2022 --year-to 2026 --offline fixtures/registros.json
```

El DOI `10.1000/demo` y todos los registros del fixture son sintéticos; no deben citarse como bibliografía real.

`citation` usa solo los metadatos disponibles. `citation_status=unverified` exige comprobar DOI, título y autores en la página oficial antes de citar; no se promete APA perfecta.

## Consulta pública

```bash
python3 scripts/buscar.py "AI tutoring" --sources crossref arxiv semantic openalex core --limit 2 --year-from 2022 --year-to 2026
```

Variables reconocidas: `CORE_API_KEY` (obligatoria para CORE), `SEMANTIC_SCHOLAR_API_KEY` y `OPENALEX_API_KEY` (opcionales), `CROSSREF_EMAIL` (opcional) y `UNPAYWALL_EMAIL` (solo enriquecimiento). No se guardan ni imprimen. Un fallo queda en `errors` y no elimina filas de otras fuentes.

Enriquecimiento separado por DOI (no es búsqueda temática):

```bash
UNPAYWALL_EMAIL=tu-email python3 scripts/buscar.py --enrich-doi 10.1234/doi-real
```

Sin `UNPAYWALL_EMAIL`, el JSON conserva `mode=enrichment` y reporta la credencial ausente en `errors`; no intenta una búsqueda alternativa.

## Instalar en un proyecto

El alumno controla la copia; no instales globalmente:

```bash
mkdir -p /ruta/al/proyecto/.agents/skills/buscador-academico
cp -R SKILL.md scripts fixtures README.md /ruta/al/proyecto/.agents/skills/buscador-academico/
```

Reinicia o solicita al agente que enumere skills del proyecto y verifica que aparezca `buscador-academico`. Luego invócala explícitamente: “Usa buscador-academico para buscar…”. La presencia de archivos no acredita activación; compruébala en el entorno objetivo.

## Pruebas

Desde la raíz del repositorio:

```bash
python3 -m unittest discover -s s05-buscador-academico/material/lab/buscador/tests -v
```

Las pruebas son offline. No acreditan red, activación de skill ni Telegram.

## Límites y recuperación HTTP

Ante 429 o 503, se permite un solo reintento si la espera indicada es de hasta dos segundos. Si el servidor pide más tiempo o indica una fecha, no se adelanta el reintento: se devuelve `retry deferred` y se conservan otras fuentes. Revisa la espera requerida antes de repetir manualmente. Esto sigue la semántica de [Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#name-retry-after); no garantiza acceso al proveedor.
