# Superpowers · instalación y catálogo completo
## Qué es
Superpowers es un paquete de skills de metodología para agentes de programación, mantenido por Jesse Vincent y colaboradores. Una skill es un conjunto de instrucciones reutilizables con nombre y descripción que permiten elegir cuándo cargarla. El plugin empaqueta esas skills y su integración por entorno.
No es un modelo, un reemplazo de OpenClaw, un servicio que ejecuta solo ni una garantía de calidad.

## Versión y fuente
Inventario verificado: versión 6.3.0, commit b36e0829c6d0140e93cfef2ca599b1b07d4a7797.
Fuente fijada: https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797
14 directorios con SKILL.md. El catálogo puede cambiar; registra tu versión antes de comparar.
El repositorio contiene skills y referencias/scripts de apoyo, manifiestos de plugins por entorno, hooks de arranque para algunos entornos, tests e infraestructura de evaluación, documentación, assets y licencia MIT. No todo archivo es una skill. El manifiesto Codex 6.3.0 apunta a ./skills/ y tiene hooks vacío: no extrapolar el hook de Claude Code a Codex.
El compañero visual opcional de brainstorming es una herramienta de discusión de diseño; no hace falta activarlo para este caso. El README documenta su carga opcional de marca/telemetría y opt-out.

## Dónde se instala
Telegram es el canal; OpenClaw enruta la tarea; el runtime efectivo lee skills y usa herramientas. Verifica usuario del proceso y carpeta de trabajo. No pegues tokens.
Codex App y el proceso de Codex que utiliza OpenClaw pueden tener distinta configuración. No atribuir disponibilidad en Telegram a una instalación visible solo en la App.
Si OpenClaw no expone estas skills, ejecutar la práctica en Codex sobre el mismo snapshot y registrar esa limitación. No afirmar compatibilidad nativa que el README oficial no promete.

## Instalación principal: Codex App
1. Abrir Plugins, localizar Superpowers en Coding y revisar origen.
2. Instalar con + y completar los pasos que muestre la aplicación.
3. Abrir una sesión nueva en el snapshot del curso.
4. Verificar catálogo, nombre y ruta de una skill; luego probar su activación.

## Codex CLI
En la sesión interactiva ejecutar /plugins, buscar superpowers y elegir Install Plugin.
En CLI 0.154.0 también existe la ruta no interactiva:
```bash
codex --version
codex plugin list --available --json
codex plugin add superpowers@openai-curated-remote --json
codex plugin list --json
```
El identificador anterior se comprobó en el catálogo del instructor; si tu catálogo usa otro nombre, usa el identificador que realmente liste. El JSON de list enumera catálogos; el de add confirma instalación y ruta. No confundas disponible con instalado.
No usar instrucciones antiguas de .codex/INSTALL.md sin verificar: esa ruta no está en el commit 6.3.0 examinado.

## Windows
Abre Codex App o la CLI en la cuenta que ejecuta la práctica. La ruta plugin evita junctions manuales. Tras instalar, abre sesión nueva. Si /plugins no existe, revisa versión y la documentación de tu instalación; no inventes un comando de bootstrap. Git y Node deben estar visibles en esa terminal.
El instructor puede instalar desde la interfaz; el alumno verifica por conversación.

## Claude Code (alternativa explicada, no necesaria para la práctica)
```text
/plugin install superpowers@claude-plugins-official
```
Es un comando del chat de Claude Code. No pegarlo en Telegram o terminal como si fuese universal. La instalación se hace por entorno.

## Prueba de activación
Prompt: «Identifica las skills de Superpowers disponibles en esta sesión. Carga brainstorming desde la instalación y dime qué ruta leíste. Quiero crear desde cero un asistente de postulación laboral; empieza por aclarar criterios y alternativas, sin implementar aún».
Observa una pregunta pertinente y un diseño revisable antes del código. Pedir solo «¿tienes superpowers?» no basta.
Tras aprobar: «Usa writing-plans sobre la spec aprobada; indica tareas, archivos y pruebas». Antes del cierre: «Usa verification-before-completion y ejecuta las pruebas de nuevo».
Registrar versión, ruta, prompt, salida y runtime. Si no aparece en catálogo, detener esa parte y recuperar instalación. No fingir que una lectura manual del README es activación.

## Las 14 skills
### using-superpowers
- Cuándo: Antes de responder o actuar.
- Qué hace: Detecta qué skill corresponde y carga sus instrucciones.
- En el caso: Pedir que identifique skill y ruta antes de empezar.
- Límite: No añade herramientas ni permisos al runtime.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/using-superpowers/SKILL.md

### brainstorming
- Cuándo: Antes de diseñar o construir.
- Qué hace: Aclara objetivo, alternativas y alcance; obtiene aprobación del diseño.
- En el caso: Pregunta qué datos acepta el asistente y cómo citará evidencia.
- Límite: En 6.3.0 distingue spike, bounded y architectural; el ciclo documental completo es elección pedagógica de esta clase.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/brainstorming/SKILL.md

### using-git-worktrees
- Cuándo: Antes de implementar aisladamente.
- Qué hace: Prepara una rama/carpeta separada y comprueba baseline.
- En el caso: Aislar la construcción del asistente sin tocar el repo original.
- Límite: Un worktree comparte el historial Git, no es una copia de seguridad ni una VM.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/using-git-worktrees/SKILL.md

### writing-plans
- Cuándo: Con diseño aprobado.
- Qué hace: Divide el trabajo en tareas con archivos, pruebas y resultados esperados.
- En el caso: T1 contrato, T2 análisis, T3 borrador, T4 runtime, T5 review.
- Límite: Un plan dice cómo; la spec dice qué y por qué.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/writing-plans/SKILL.md

### executing-plans
- Cuándo: Con plan revisado.
- Qué hace: Ejecuta el plan y conserva checkpoints.
- En el caso: Alternativa secuencial cuando no hay subagentes.
- Límite: No es licencia para improvisar si falta un requisito.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/executing-plans/SKILL.md

### subagent-driven-development
- Cuándo: Plan con tareas separables y herramientas disponibles.
- Qué hace: Un implementador por tarea, revisión de spec y luego calidad.
- En el caso: Demostración docente de separación de roles.
- Límite: Comparte siglas SDD, pero no significa Spec-Driven Development.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/subagent-driven-development/SKILL.md

### test-driven-development
- Cuándo: Antes de implementar un comportamiento.
- Qué hace: RED → GREEN → REFACTOR con fallo observado.
- En el caso: El starter aún no analiza una oferta válida; implementar contrato y repetir la suite de 15 tests.
- Límite: Los tests del núcleo local no certifican obediencia del modelo.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/test-driven-development/SKILL.md

### systematic-debugging
- Cuándo: Ante fallo inesperado.
- Qué hace: Investiga causa, compara patrón, prueba hipótesis y corrige.
- En el caso: Reproducir 0/0 como NaN cuando faltan obligatorios y comprobar la salida null definida por la spec.
- Límite: Una corrección sin reproducción no prueba causalidad.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/systematic-debugging/SKILL.md

### verification-before-completion
- Cuándo: Antes de decir terminado.
- Qué hace: Exige comprobación reciente y lectura de resultados.
- En el caso: Correr 15 tests y abrir referencias antes del dictamen.
- Límite: Un PASS viejo deja de servir si cambia el código.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/verification-before-completion/SKILL.md

### dispatching-parallel-agents
- Cuándo: Problemas independientes.
- Qué hace: Distribuye investigación sin dependencias compartidas.
- En el caso: Revisar spec y documentación en paralelo, con archivos separados.
- Límite: No paralelizar spec y código dependiente, ni dos editores del mismo archivo.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/dispatching-parallel-agents/SKILL.md

### requesting-code-review
- Cuándo: Después de un cambio relevante.
- Qué hace: Entrega contexto, diff y criterios al revisor.
- En el caso: Primero CA1–CA7 (núcleo, conversación y trazabilidad); luego robustez y claridad.
- Límite: Tests verdes no reemplazan cumplimiento de spec.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/requesting-code-review/SKILL.md

### receiving-code-review
- Cuándo: Al recibir hallazgos.
- Qué hace: Verifica, reproduce y decide cómo responder.
- En el caso: Aceptar guarda para cero obligatorios; discutir scraper o cloud fuera del recorte.
- Límite: No aceptar toda sugerencia automáticamente.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/receiving-code-review/SKILL.md

### finishing-a-development-branch
- Cuándo: Tras pruebas y revisión.
- Qué hace: Presenta opciones de integración y limpieza de rama/worktree.
- En el caso: Elegir PR o conservar rama hasta autorización.
- Límite: No borrar una rama ni publicar por inferencia de una suite verde.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/finishing-a-development-branch/SKILL.md

### writing-skills
- Cuándo: Al crear/modificar una skill.
- Qué hace: Prueba instrucciones, disparadores y resistencia a casos difíciles.
- En el caso: Puente conceptual a S06: mejorar la description de una skill.
- Límite: S04 explica el mecanismo; la forja completa es S06, sin prometer una skill nueva hoy.
- Fuente: https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/writing-skills/SKILL.md

## Cómo se combinan
brainstorming → diseño aprobado → writing-plans → using-git-worktrees → ejecución → test-driven-development → requesting-code-review → receiving-code-review → verification-before-completion → finishing-a-development-branch.
systematic-debugging se activa ante fallos; dispatching-parallel-agents solo ante independencia real. using-superpowers orienta la elección. writing-skills se usa al crear skills.
El orden de plan/worktree depende del flujo: la condición es diseño aprobado y entorno aislado antes de implementar.

## Recuperación
Plugin instalado, skill ausente: abrir nueva sesión y comprobar usuario/ruta de ejecución.
Skill visible, conducta incorrecta: invocarla por nombre y pedir evidencia de lectura; revisar contradicciones de instrucciones.
Subagentes ausentes: ejecutar secuencialmente; instalar skills no crea herramientas.
Tests fallan: observar mensaje y reproducir; no cambiar la expectativa para obtener verde.
El proceso de OpenClaw difiere: registrar «verificado en Codex; Telegram pendiente» y ensayar el canal aparte.

Fuentes: [Superpowers](https://github.com/obra/superpowers), [plugins de Codex](https://learn.chatgpt.com/docs/plugins), [skills](https://learn.chatgpt.com/docs/build-skills).
