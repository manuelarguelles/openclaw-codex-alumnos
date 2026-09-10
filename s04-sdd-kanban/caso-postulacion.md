# Caso central S04 · Asistente de postulación laboral desde cero

## El antes que realmente existe
Repositorio de referencia: https://github.com/manuelarguelles/asistente-postulacion-laboral
Baseline público observado el 10-sep-2026: commit f023fa933150856a05da18ed333e902521844f35.
Contiene README, PROJECT, ROADMAP, STATE, BRIEF y archivos de configuración iniciales. No contiene implementación, suite de tests ni CI.
Manu indica que nació de un prompt sencillo sin estructura ni skills. El texto exacto de ese prompt no está en el repo: no lo presentamos como cita.
La copia local tiene otra revisión con stack Railway-first; no se presume publicada ni aprobada para este ejercicio.
Contradicción concreta del baseline: PROJECT.md dice «Repositorio limpio y privado» y «pendiente de publicación», aunque el repo ya es público. Discovery debe confirmar la intención y actualizar los documentos antes de ejecutar, sin cambiar visibilidad por su cuenta. Es un ejemplo real de por qué revisar consistencia importa.

## Qué significa profesionalizarlo
| Antes observado | Decisión SDD | Evidencia que pediremos |
|---|---|---|
| Visión amplia | Caso de uso y límites explícitos | spec.md aprobada |
| Discovery abierto | Comparar alternativas y resolver supuestos | brainstorm.md |
| Roadmap por fases | Tareas pequeñas con criterios y dependencias | plan.md y tarjetas |
| No hay implementación | Construir una primera parte completa | analizarOferta y demo |
| No hay tests | Casos esperados y de rechazo antes del código | RED, GREEN y regresión |
| Principio de veracidad | Toda coincidencia cita un dato del perfil | tests y revisión humana |
| No enviar sin permiso | En S04 no existe herramienta de envío | contrato, inventario de tools y ensayo |

No afirmamos que el prompt original produjo software defectuoso: produjo un inicio documental. SDD vuelve observables las decisiones y el avance.

## Producto objetivo y recorte de clase
Visión completa: preferencias, ingreso de ofertas, extracción de requisitos, comparación con perfil, borradores, historial y control humano.
En tres horas escribimos la spec del MVP y lanzamos su primera parte: un perfil ficticio + una oferta estructurada → coincidencias, brechas, evidencia y borrador revisable. Es el núcleo del agente, no un portal de empleo desplegado.
Texto libre/URL/PDF, persistencia, interfaz, autenticación, proveedor LLM y Railway quedan planificados con criterios propios. No fingimos haber construido esos componentes.

## Datos de práctica
Perfil ficticio: p1 «SQL: construí consultas para un proyecto académico»; p2 «Python: analicé datos de práctica».
Oferta ficticia o1: SQL y Python obligatorios; AWS deseable.
Resultado esperado: dos coincidencias con p1/p2, brecha AWS, cobertura literal de obligatorios 100%. No es probabilidad de contratación ni valoración de una persona.
Cambiar Python por inglés en la oferta: cobertura 50%, brecha inglés. El borrador no puede inventar inglés, AWS, certificaciones ni años de experiencia.

## Decisiones de discovery para el ejercicio
Propuesta didáctica que el alumno debe confirmar, no aprobación histórica de Manu:
- Un usuario, datos sintéticos, sin almacenamiento ni red en la primera parte.
- Entrada estructurada para poder probar reglas. El agente ayuda a preparar esos datos y pide aclaraciones.
- Coincidencia literal normalizada, sin inferir equivalencias como JS/JavaScript.
- Sin envío externo, aunque se pida. El alumno revisa el borrador.
- La interfaz inicial es la conversación del curso; el runtime invoca el núcleo local.
- No copiar auto-postulacion-cvs ni CVs, memoria o credenciales reales.

## Issue significa tarea
Una issue es una ficha de trabajo en GitHub con título, descripción y criterio de aceptación. Un Project agrupa esas fichas en un tablero.
Aquí creamos tareas nuevas T1–T5; no necesitas encontrar una supuesta issue de S03.
T1 contrato y fixtures. T2 análisis con evidencia. T3 borrador veraz. T4 integración conversacional y evaluación. T5 revisión y entrega.
Los números #1/#2 no se inventan: GitHub devuelve el número real al crear la issue.

## Qué cambia en el papel del alumno
El agente redacta y programa. El alumno decide alcance, aprueba la spec, interpreta resultados, abre la evidencia, controla el tablero y autoriza la entrega.
El método no garantiza ausencia de errores: permite detectarlos y decidir con evidencia.
