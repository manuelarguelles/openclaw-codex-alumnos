# Plan SDD del laboratorio

1. **Spec:** fijar interfaz, normalización, ranking, errores y límites de confianza.
2. **RED:** escribir casos literales y observar que fallen por funciones ausentes.
3. **GREEN:** implementar núcleo Python estándar y adaptadores mínimos según documentación oficial.
4. **Refactor:** separar transporte (`fuentes.py`) de orquestación/CLI (`buscar.py`) y conservar las pruebas verdes.
5. **Verify:** suite offline, CLI fixture y consulta pública de volumen bajo; registrar exit codes reales.

| Regla | Prueba |
|---|---|
| DOI canónico y procedencia | `test_duplicate_doi_keeps_both_sources` |
| No fusionar por título | `test_different_dois_with_same_title_stay_separate` |
| Ranking léxico antes que fecha | `test_matching_older_title_ranks_above_unrelated_newer_paper` |
| Periodo inclusivo | `test_year_filter_excludes_2020` |
| Éxito parcial | `test_partial_timeout_retains_success_and_reports_source` |
| Vacío honesto | `test_zero_matches_stays_empty` |
| Metadatos incompletos | `test_missing_author_and_year_are_not_invented` |
| Entrada y proveedor inválidos | pruebas de límite y respuesta malformada |
| Credencial explícita | pruebas CORE y Unpaywall |
