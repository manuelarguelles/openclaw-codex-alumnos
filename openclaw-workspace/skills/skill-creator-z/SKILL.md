---
name: "skill-creator-z"
description: "Create and improve reusable skills with domain research, source comparison, evaluation, hardening, and parallel delegated reviews using task-specific priming."
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

## Fase 1.25 — Delegación paralela y priming

Cuando existan revisiones independientes, usa `dispatching-parallel-agents` —o la capacidad equivalente de subagentes del runtime— para ejecutarlas en paralelo. El paralelismo no es solo lanzar varias tareas: cada subagente debe recibir un contexto construido específicamente para su encargo.

### Regla de priming

- El coordinador conserva el contexto completo; cada subagente recibe solo la skill, archivos, ejemplos y criterios que necesita para su revisión.
- No envíes la conversación completa por comodidad. Elimina secretos, datos personales, decisiones no relacionadas y contexto que pueda sesgar la revisión.
- Cada encargo debe declarar objetivo, alcance de lectura, pregunta concreta, formato de salida y criterio de parada.
- Divide por responsabilidad y evita que dos subagentes escriban el mismo archivo. Las revisiones deben ser independientes y preferentemente de solo lectura.
- Lanza las tareas independientes en paralelo, no secuencialmente. Mientras esperan, el coordinador puede preparar la síntesis o una tarea no solapada.
- Si la capacidad de paralelismo no está disponible, declara la limitación y no presentes una ejecución secuencial como paralela.

### Prompt reusable de revisión

```text
Tengo tres revisiones independientes que hacer sobre [NOMBRE_SKILL]. Usa dispatching-parallel-agents para lanzar un subagente por cada una, en paralelo; no las hagas tú mismo. Dale a cada subagente SOLO el contexto que necesita para SU revisión, no toda esta conversación:

1. Activación: revisa si la description puede disparar la skill en momentos equivocados (falsos positivos) o no dispararla cuando debería (falsos negativos). Encargo: leer solo SKILL.md y 3–5 frases de ejemplo que te paso.
2. Veracidad: revisa si la salida puede inventar datos que no estén en el perfil o la oferta de entrada. Encargo: leer solo el contrato de entrada/salida y un caso de ejemplo.
3. Permisos: revisa si alguna instrucción amplía el alcance más allá de leer perfil y oferta, por ejemplo enviar algo o modificar datos. Encargo: leer solo la sección de límites de SKILL.md.

Cuando los tres terminen, junta los hallazgos en una sola lista e indica cuál subagente encontró algo real, cuál no encontró nada y cuál evidencia lo sustenta. No descartes un “sin hallazgos”: sirve para comprobar si el encargo estaba bien acotado.
```

### Síntesis y control de calidad

Después de recibir los resultados, crea una tabla `subagente → alcance → hallazgo → evidencia → severidad → acción`. Separa `hallazgo real`, `falso positivo`, `sin hallazgo` y `fuera de alcance`. No conviertas tres revisiones parciales en una afirmación de auditoría completa.

El coordinador debe comprobar que cada hallazgo provenga del contexto permitido, resolver contradicciones con una nueva verificación acotada y registrar qué subagente leyó qué. Si un agente intenta leer archivos fuera de su encargo, detén esa rama y marca la desviación.

### Cuándo aplicar este patrón

Úsalo para activación, veracidad, permisos, seguridad, compatibilidad, fuentes o evaluaciones que puedan separarse. No lo uses para fragmentar una decisión que depende de una única cadena causal ni para multiplicar agentes sin una assertion discriminante.

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
