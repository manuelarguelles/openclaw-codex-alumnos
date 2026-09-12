# S05 · Búsqueda reproducible y mini-spec de tu capstone

## Qué entregarás

En tu repositorio, `entregas/s05/`: petición o comando usado, `resultados.json`, `revision.md`, evidencia de pruebas y `MINI-SPEC.md` de una página. La skill pública está en [buscador](buscador/README.md). No presentes fixtures como una búsqueda en internet.

## Preparación y privacidad

Abre el repo de alumnos, esta consigna y el deck. Puedes pedir ayuda desde Telegram si el proceso tiene acceso al proyecto y reconoce la skill. Si trabajas en Codex CLI, registra ese canal: no acredita Telegram.

Sigue la instalación por proyecto en [README del buscador](buscador/README.md). No instales la skill privada `tesis-buscador`. Usa consultas públicas; no envíes CV, claves ni datos personales a APIs académicas. Comprueba Python 3 y la carpeta actual.

## Checkpoint 1 · pregunta, spec y skill

1. Cambia «Busca papers de IA» por una pregunta con tema, periodo, número máximo y salida esperada.
2. Lee [SPEC.md](buscador/SPEC.md) y [PLAN.md](buscador/PLAN.md). Elige un criterio y escribe una entrada que podría romperlo.
3. Abre [SKILL.md](buscador/SKILL.md). Localiza nombre, descripción, instrucciones y comando. Explica qué parte orienta la selección.
4. Comprueba descubrimiento e invocación explícita en tu proceso. Conserva el resultado observado, incluso si falla.

Aceptación: distingues archivo presente, skill seleccionada y script ejecutado. Recuperación: comprobar `.agents/skills`, directorio de arranque y frontmatter antes de editar la lógica.

## Checkpoint 2 · ejecutar e inspeccionar fuentes

Desde `s05-buscador-academico/material/lab/buscador/`, comienza con el caso controlado:

```bash
python3 scripts/buscar.py "AI tutoring" --sources crossref arxiv --limit 3 --year-from 2022 --year-to 2026 --offline fixtures/registros.json
```

Luego consulta fuentes accesibles con volumen bajo:

```bash
python3 scripts/buscar.py "AI tutoring" --sources crossref openalex --limit 3 --year-from 2022 --year-to 2026
```

Petición por chat: «Usa buscador-academico con AI tutoring, 2022–2026 y hasta tres resultados. Conserva procedencias y errores. No uses archivos privados ni publiques nada». Confirma el comando y copia la salida en `resultados.json` de tu entrega.

Inspecciona `records`, `sources`, `errors` y `mode`. Las cinco búsquedas de descubrimiento son Crossref, arXiv, Semantic Scholar, OpenAlex y CORE. Consulta README para credenciales; no inventes valores ni insistas ante límites.

Unpaywall es otro paso, cuando ya existe un DOI:

```bash
python3 scripts/buscar.py --enrich-doi DOI_REAL_DEL_RESULTADO
```

Sustituye el marcador por un DOI observado. Configura tu propio `UNPAYWALL_EMAIL` según README sin guardarlo en Git. Si falta acceso, registra el error; no acredita enriquecimiento exitoso.

Aceptación: cada fuente consultada tiene estado explícito y sabes qué datos salieron a internet. Recuperación: modo offline si falla acceso; anota qué quedó pendiente de red.

## Checkpoint 3 · calidad y recuperación

1. Predice la fixture antes de ejecutar: un DOI canónico y ambas procedencias. Son datos sintéticos, no papers citables.
2. Compara ranking por términos del tema con ordenar solo por año. Explica por qué un trabajo reciente ajeno al tema puede quedar después.
3. Ejecuta pruebas desde la raíz del repo:

```bash
python3 -m unittest discover -s s05-buscador-academico/material/lab/buscador/tests -v
```

4. Localiza los tests de duplicado y fuente caída. Explica qué comprobaron y qué no: no acreditan selección del modelo ni Telegram.
5. Abre al menos un DOI real y compara título, autores y año. Si difieren, marca «requiere revisión» y no cites el candidato como verificado. HTTP exitoso no garantiza metadatos correctos.
6. En `revision.md`, incluye una referencia legible con metadatos comprobados o declara por qué ninguna pudo verificarse. Esa brecha no equivale al cumplimiento completo del entregable bibliográfico.

Aceptación: sin duplicados indebidos, ranking explicado, errores visibles y ninguna referencia inventada. Recuperación: separa fallo de dato, núcleo, configuración y red antes de corregir.

## Checkpoint 4 · proyecto propio y revisión

Completa [MINI-SPEC.md](MINI-SPEC.md) en una página: qué hace, para quién, entradas, salida, exclusiones y criterios de aceptación. Elige tu dominio. El asistente laboral es un ejemplo; no reemplaza el buscador académico de esta sesión.

Intercambia la mini-spec con un compañero. Debe poder nombrar una entrada válida, una inválida y la evidencia de aceptación. Corrige un criterio ambiguo antes de ampliar funciones.

Registra canal usado, ejecución offline, fuentes que respondieron, errores y pendientes. En S06 crearás y evaluarás una skill/workflow propia sobre esta mini-spec. No publiques credenciales ni datos privados.
