# Mapa del ciclo completo

using-superpowers selecciona instrucciones según contexto. Para un proyecto nuevo: brainstorming aclara y propone diseño, la persona aprueba la spec, writing-plans genera tareas y using-git-worktrees aísla el trabajo.
executing-plans permite ejecutar el plan; subagent-driven-development es otra ruta cuando existen subagentes. test-driven-development guía pruebas y código; systematic-debugging se activa ante fallos. dispatching-parallel-agents solo separa trabajo independiente.
requesting-code-review pide revisión; receiving-code-review verifica hallazgos; verification-before-completion comprueba resultados frescos; finishing-a-development-branch presenta opciones de integración.
writing-skills permite crear instrucciones reutilizables y probarlas: se profundiza en S06.

## Despliegue: extensión conceptual, no incluida en S04
Superpowers no contiene una skill universal de deploy. Tras aprobación, el agente puede cargar una skill externa disponible del proveedor elegido, con credenciales/permisos configurados y pruebas de salud/recuperación. No implica instalar nada ni desplegar hoy. El paralelismo solo sirve si servicios independientes lo permiten; base de datos/migraciones dependientes se coordinan antes. Se verifica el conjunto después.

## Tablero real de demostración
https://github.com/users/manuelarguelles/projects/3/views/2
Seis tareas ficticias repartidas en4 etapas y4 áreas, WIP Haciendo=1. Son draft issues del Project, no issues publicadas en el repositorio original. Status y Etapa coinciden; la vista Board creada por API usa Status con opciones personalizadas. Se puede agrupar manualmente por Etapa.
Los estados son ilustrativos, no certifican avance del agente. No se envían postulaciones.
