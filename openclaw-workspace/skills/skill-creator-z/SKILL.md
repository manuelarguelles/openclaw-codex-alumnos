---
name: "skill-creator-z"
description: "Use when creating or improving a reusable skill that needs domain research, source comparison, repository discovery, evaluation, and iterative hardening."
---

# Skill Creator Z

## Propósito

Crear o mejorar skills reutilizables con evidencia del dominio, evaluación reproducible y protección contra errores de comportamiento. Investigar primero la materia; después diseñar, probar y endurecer la skill.

## Contrato de salida

Entregar:

- skill final con SKILL.md conciso y recursos solo cuando aporten valor;
- research brief con fuentes, fecha, cobertura, límites y decisiones;
- matriz de requisitos y riesgos;
- eval set, baselines, resultados y benchmark;
- registro de iteraciones, cambios y evidencia;
- estado explícito: provisional, validada o lista para producción.

No presentar una skill como validada si solo fue redactada o probada con ejemplos favorables.

## Fase 0 — Definir intención

Extraer del pedido, antes de preguntar:

- capacidad que debe habilitar;
- frases y contextos que deben activarla;
- entradas, salidas y formatos;
- usuarios, runtime y herramientas;
- criterios de éxito, límites, permisos y acciones prohibidas;
- ejemplos positivos, negativos y casos límite.

Preguntar solo por vacíos que cambien el diseño. Registrar supuestos.

## Fase 1 — Investigación obligatoria del dominio

No redactar la skill todavía. Construir un brief desde varias aristas:

1. **Capacidad y fuentes primarias:** estándares, documentación oficial, APIs, políticas, especificaciones y versiones vigentes.
2. **Ecosistema:** plataformas, proveedores, repositorios, bases de datos, herramientas, formatos, licencias, límites, costos y autenticación.
3. **Alternativas existentes:** skills, plugins, repositorios y proyectos que resuelvan una parte o todo el problema. Compararlos por madurez, mantenimiento, extensibilidad, pruebas y licencia.
4. **Riesgos y calidad:** errores frecuentes, sesgos, datos faltantes, seguridad, privacidad, trazabilidad, reproducibilidad y condiciones de no uso.
5. **Evaluación:** qué puede verificarse automáticamente, qué requiere revisión humana y qué evidencia distingue una mejora real de una respuesta plausible.
6. **Actualidad:** comprobar fecha de actualización, versión y vigencia. No tratar snippets, blogs o README antiguos como autoridad si existe fuente primaria.

Buscar en paralelo cuando las aristas sean independientes. Usar herramientas y skills de investigación disponibles. Cada afirmación importante conserva URL o ruta, fecha de consulta, versión y confianza. Separar hecho, inferencia y decisión. Declarar búsquedas fallidas y cobertura no verificada; no sustituirlas silenciosamente por fixtures.

### Ejemplo: buscador-academico-z

Investigar antes de diseñar:

- APIs y plataformas para papers, tesis, libros, capítulos, repositorios institucionales y material académico;
- cobertura, filtros, texto completo, metadatos, DOI, rate limits, autenticación, licencia, idioma y estabilidad;
- estándares de citación y versión vigente de APA —comprobar oficialmente APA 7 y sus reglas relevantes—;
- repositorios o proyectos que ya hagan búsqueda académica, ranking, deduplicación, recuperación o citas;
- oportunidades de construir sobre ellos, integrarlos o personalizarlos en vez de reinventar la rueda.

El resultado propone una arquitectura de fuentes y política de citación/atribución; no afirma que una fuente sea mejor sin criterios comparables.

### Ejemplo: skill para mejorar CVs

Investigar mercado y buenas prácticas de CV, ATS, sesgos, privacidad, evidencia profesional, formatos y fuentes actuales. Comparar herramientas y repositorios existentes. Separar optimización legítima de inventar experiencia, títulos, métricas o competencias.

## Fase 1.5 — Decisión de alcance

Convertir el brief en:

- mapa de capacidades;
- requisitos funcionales y no funcionales;
- matriz fuente → afirmación → decisión;
- dependencias y recursos reutilizables;
- amenazas, límites y criterios de no aplicación;
- plan de evaluación.

Preferir integración o adaptación de soluciones maduras. Crear desde cero solo con razón documentada.

## Fase 2 — Diseño

Diseñar progressive disclosure:

- SKILL.md: activación, contrato, flujo esencial, decisiones y enlaces directos;
- references/: conocimiento pesado o variantes;
- scripts/: operaciones deterministas y repetitivas;
- assets/templates/: archivos usados por el resultado;
- agents/openai.yaml: metadatos UI si el runtime los soporta.

Usar imperativo, ejemplos mínimos y explicar el porqué. La descripción prioriza cuándo activar la skill y síntomas concretos; no esconder el proceso esencial en metadata ni hacerla tan amplia que compita con todo. Mantener SKILL.md bajo 500 líneas y separar detalles pesados.

## Fase 3 — Validación híbrida RED → GREEN → REFACTOR

### RED — baseline

Antes de editar, ejecutar cada eval sin la skill; al mejorar una existente, usar snapshot original. Registrar salidas, decisiones, errores, omisiones y racionalizaciones literales.

Incluir pressure scenarios combinando, cuando proceda, urgencia, información incompleta, coste hundido, autoridad, cansancio, permisos y tentación de inventar datos.

### GREEN — mínima corrección

Escribir solo instrucciones y recursos que corrigen fallos observados. Las reglas de disciplina tienen señales de parada, respuesta ante presión y contraejemplos. Para fallos de forma, usar recetas; no acumular prohibiciones genéricas.

### REFACTOR — generalización

Repetir con casos nuevos, variaciones y casi-errores. Buscar sobreajuste, redundancia, conflictos, pérdida de contexto y consumo innecesario. Cada cambio sustantivo requiere revalidación.

## Fase 4 — Evaluación

Ejecutar baseline y versión con skill en el mismo ciclo y, si se itera, comparar contra snapshot estable. Guardar por eval:

- prompt, archivos, configuración y versión;
- salida bruta, errores, tiempo, tokens y herramientas;
- assertions objetivas y evidencia;
- revisión cualitativa humana;
- pass rate, media, desviación y delta.

Las assertions deben discriminar entre configuraciones; marcar las que siempre pasan como no discriminantes. Usar viewer para revisión cuando exista; en headless usar salida estática. Comparación ciega opcional para decisiones sensibles.

Evaluar:

1. comportamiento y exactitud;
2. triggering: true positives, false positives, false negatives y under-triggering;
3. coste: tokens, latencia, herramientas y complejidad.

## Fase 5 — Hardening y entrega

Construir tabla de fallos → causa → corrección → prueba. Revisar seguridad, privacidad, licencias, prompt injection, fuentes no verificadas, acciones externas y efectos irreversibles.

Niveles:

- **light:** estructura + smoke test;
- **standard:** baseline, versión con skill, assertions y revisión;
- **strict:** pressure testing, microtests de wording, benchmark, análisis de varianza, triggering y revisión ciega.

No ejecutar acciones externas ni publicar cambios sin autorización separada. No inventar datos faltantes. No borrar evidencia; archivarla.

## Reglas de calidad

- Investigar el dominio antes de escribir la solución.
- No confundir documentación de un proveedor con verdad universal.
- No incluir reglas sin propósito, evidencia o criterio de verificación.
- No optimizar solo por pass rate: coste y latencia también importan.
- No usar una descripción pushy para justificar falsos positivos.
- No marcar producción sin evidencia del nivel declarado.
- Documentar fuentes, supuestos, límites y decisiones antes de reportar finalización.

Leer solo las referencias necesarias para el dominio. Consultar schemas del harness para evals, grading y benchmark; consultar guías especializadas para comparación ciega o análisis estadístico.
