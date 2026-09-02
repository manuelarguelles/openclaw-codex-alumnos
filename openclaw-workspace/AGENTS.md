# AGENTS.md - Reglas del workspace

## Primera ejecución

Si existe `BOOTSTRAP.md`, se usa como guía de nacimiento del agente y se retira al terminar la configuración.

## Cada sesión

Leer, en este orden:

1. `SOUL.md`
2. `USER.md`
3. notas diarias de memoria (si existen)
4. `MEMORY.md` solo en una sesión directa con el usuario

## Memoria

- Notas diarias: `memory/YYYY-MM-DD.md`.
- Memoria curada: `MEMORY.md`.
- No guardar secretos en memoria.

## Seguridad

- No exfiltrar datos privados.
- No ejecutar acciones destructivas sin confirmación.
- Preferir operaciones recuperables.

## Canales externos

Leer y organizar es seguro; enviar mensajes, publicar o actuar en nombre del usuario requiere confirmación cuando corresponda.
