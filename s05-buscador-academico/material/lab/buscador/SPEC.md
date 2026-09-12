# Especificación del laboratorio

## Contrato

Entrada: tema no vacío, fuentes públicas, límite positivo y periodo inclusivo. Salida JSON: `query`, `records`, `sources`, `errors`, `mode`. Cada registro expone `title`, `authors`, `year`, `doi`, `id`, `url`, `abstract`, `sources`, explicación de ranking y advertencias.

## Reglas observables

- DOI canónico: quitar resolver/prefijo y pasar a minúsculas; ese es el único cruce entre fuentes.
- Un DOI duplicado preserva coherentemente los metadatos del primer registro; diferencias materiales de título, autores o año se guardan en `conflicts`, con valores y fuentes en `metadata_provenance`. Nunca se construye silenciosamente una cita híbrida.
- Sin DOI: conservar separados salvo ID exacto dentro de la misma fuente. Nunca fusionar por título.
- Periodo: excluir años conocidos fuera del rango; conservar año ausente con advertencia.
- Ranking: cantidad de tokens de consulta presentes en título/abstract; el año solo desempata.
- Resiliencia: timeout, HTTP, credencial o formato inválido afectan solo su fuente.
- Privacidad: credenciales solo por variables nombradas; no loggear valores ni URL con secretos.
- Unpaywall: enriquecimiento por DOI posterior, opcional, no descubrimiento temático.

## Criterios de aceptación

Los casos literales del fixture y las pruebas cubren DOI duplicado, títulos iguales con DOI distintos, ranking, periodo, parcial, cero resultados, campos ausentes, límite inválido, respuesta malformada y credenciales. La red y Telegram requieren evidencia separada.
