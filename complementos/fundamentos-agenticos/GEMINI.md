# Gemini como respaldo en OpenClaw

Guía preparada el 15-sep-2026 para OpenClaw local 2026.7.1-2. No ejecuta cambios ni contiene claves. La configuración y el acceso real se prueban por separado. El respaldo envía contexto de la petición al proveedor Google; revisar qué datos pueden salir antes de usarlo.

## 1. Registrar el estado previo

```sh
openclaw --version
openclaw models status
openclaw models fallbacks list
openclaw models list --all --provider google --plain
```

Guardar de forma privada el modelo principal y el orden de fallbacks. No publicar salidas con información de cuenta. El catálogo local incluye `google/gemini-3.5-flash`; también está en el catálogo de Google verificado en la fecha indicada. No significa que tu cuenta esté autenticada o tenga cuota.

## 2. Registrar la API key

Crear o seleccionar una clave en [Google AI Studio](https://aistudio.google.com/apikey). Introducirla en el prompt interactivo privado:

```sh
openclaw models auth paste-api-key --provider google
```

La ayuda local confirma el comando. No incluir la clave en un argumento, historial, chat, slide o repositorio. Alternativa soportada: `GEMINI_API_KEY` o `GOOGLE_API_KEY` en el entorno del proceso que ejecuta OpenClaw. Una variable exportada en tu terminal no garantiza que el Gateway iniciado como servicio la reciba. Se prefiere el flujo de autenticación de OpenClaw para evitar esa confusión.

## 3. Añadir el respaldo conservando los existentes

```sh
openclaw models fallbacks add google/gemini-3.5-flash
openclaw models fallbacks list
openclaw models status
```

Añadir no significa poner primero. Revisar el orden resultante. No usar `clear` ni reemplazar el archivo de configuración completo. Si un agente tiene modelo o fallbacks propios, revisar ese agente con `openclaw models status --agent ID`.

## 4. Probar acceso, comportamiento y cambio por fallo

La siguiente prueba hace llamadas reales y puede consumir cuota:

```sh
openclaw models status --probe --probe-provider google
```

Después, en un entorno separado de prueba:

1. Comprobar que Gemini contesta una tarea pequeña y usa una herramienta permitida.
2. Volver al modelo predeterminado si se fijó un modelo específico. La selección explícita puede ser estricta y no recorrer fallbacks.
3. Ensayar un fallo controlado del principal en ese entorno, sin romper credenciales ni apagar producción.
4. Registrar modelo principal solicitado, causa del fallo, modelo usado y resultado de la herramienta. Configurar una lista no demuestra failover.
5. Restaurar el entorno de prueba y verificar recuperación. El comportamiento de persistencia entre turnos cambia entre versiones; observarlo en la versión instalada.

Perfil de autenticación = conjunto de credenciales. Entorno de prueba = instalación/configuración/sesión separada para experimentar. No son lo mismo.

## 5. Revertir solo lo añadido

```sh
openclaw models fallbacks remove google/gemini-3.5-flash
openclaw models fallbacks list
```

Retirar el fallback no borra la credencial. Comparar el orden con el registro inicial. Ante 401/403 revisar credencial y permisos; ante 429 revisar cuota y política de reintentos. El failover no arregla herramientas ausentes, datos incorrectos o cualquier error de programación.

## Fuentes

- [Google en OpenClaw](https://docs.openclaw.ai/providers/google)
- [CLI de modelos](https://docs.openclaw.ai/cli/models)
- [Failover de modelos](https://docs.openclaw.ai/concepts/model-failover)
- [API keys de Gemini](https://ai.google.dev/gemini-api/docs/api-key)
- [Catálogo Gemini](https://ai.google.dev/gemini-api/docs/models)

Compatibilidad: documentación local consultada bajo `/opt/homebrew/lib/node_modules/openclaw/docs/`. El sitio actual incluye estructuras posteriores, como `agents.entries`; los ejemplos locales usan `agents.list`. La guía utiliza comandos confirmados por `--help` en la instalación local.
