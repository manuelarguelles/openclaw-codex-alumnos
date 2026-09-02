# Workspace docente de OpenClaw (sanitizado)

Esta carpeta documenta la estructura del workspace que usa OpenClaw en la máquina del docente.
Los archivos `.md` son plantillas de comportamiento y contexto; no contienen tokens ni credenciales.

## Qué se excluyó deliberadamente

- `~/.openclaw/openclaw.json` original y todas sus copias de respaldo.
- `credentials/`, `identity/`, `devices/`, `memory/`, `logs/`, `media/`, `cron/`, `state/`, `tasks/` y archivos de pairing.
- Tokens de Telegram, gateway, proveedores LLM, Brave, OAuth, WhatsApp y cualquier secreto de entorno.
- IDs de grupos, prompts privados, historiales, bases SQLite y rutas personales.

Consulta `config.sanitized.json` para la configuración estructural sin valores sensibles.
