# Prompt · dispatching-parallel-agents — paralelismo Y priming

Qué demuestra: `dispatching-parallel-agents` no es solo "hacer varias cosas a la vez" — cada
subagente arranca con un contexto construido a medida para SU tarea puntual, sin heredar toda la
sesión del coordinador. Eso es priming: cada uno recibe exactamente lo que necesita, ni más ni
menos. El prompt de abajo lanza tres revisiones independientes de la misma skill en paralelo, cada
una con su propio encargo acotado.

Cómo usarlo en clase: copiar el bloque de abajo, reemplazar `[NOMBRE_SKILL]` por la skill del
capstone que estén construyendo, y pegarlo en el chat de OpenClaw (Telegram).

```text
Tengo tres revisiones independientes que hacer sobre [NOMBRE_SKILL]. Usá dispatching-parallel-agents
para lanzar un subagente por cada una, en paralelo (no secuencial) — no las hagas tú mismo. Dale a
cada subagente SOLO el contexto que necesita para SU revisión, no toda esta conversación:

1. Activación: revisar si la `description` puede disparar la skill en momentos equivocados
   (falsos positivos) o no dispararla cuando debería (falsos negativos). Encargo: leer solo
   SKILL.md y 3-5 frases de ejemplo que yo te paso, nada más.
2. Veracidad: revisar si la salida puede llegar a inventar datos que no estén en el perfil o la
   oferta de entrada. Encargo: leer solo el contrato de entrada/salida y un caso de ejemplo.
3. Permisos: revisar si alguna instrucción amplía el alcance más allá de leer perfil y oferta
   (por ejemplo, enviar algo o modificar datos). Encargo: leer solo la sección de límites del
   SKILL.md.

Cuando los tres terminen, juntá los hallazgos en una sola lista y decime cuál subagente encontró
algo real vs. cuál no encontró nada (para ver si algún encargo estaba mal acotado).
```

Recordatorio para el docente: pedile al grupo que se fije en algo concreto cuando vuelvan los tres
subagentes — ¿alguno "inventó" un hallazgo porque le diste de más contexto y se puso a opinar de
cosas que no le tocaban? Ese es el costo de NO primear bien: un subagente con contexto de más deja
de estar enfocado, aunque haya corrido en paralelo igual.
