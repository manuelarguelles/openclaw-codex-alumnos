# Laboratorio S03 · Tu agente, versionado y recuperable

## Resultado

Crearás un repositorio **privado** con un snapshot sanitizado de un proyecto. Al final demostrarás que puedes restaurar un archivo y clonar el proyecto en otra carpeta. Todo lo pedirás desde OpenClaw; no necesitas trabajar por terminal.

## Tres logros de hoy

- Preparar una carpeta nueva sin subir secretos.
- Entender qué significa cada paso de Git al pedírselo a OpenClaw.
- Recuperar un archivo y comprobar un clon con el mismo hash.

## Ejercicio vivo · Mi primer proyecto recuperable

Usaremos durante toda la clase `mi-primer-proyecto`, con un `README.md` y un `RECOVERY-DEMO.md`. Envía un pedido, observa la evidencia y espera antes de autorizar efectos externos.

| Momento | Pídeselo a OpenClaw | Qué debe devolverte |
|---|---|---|
| Ver | «Dime qué cambió dentro de `[RUTA]/mi-primer-proyecto`, sin modificar nada» | `git status --short` explicado en palabras |
| Preparar | «Incluye solo `README.md` y `RECOVERY-DEMO.md`; muéstrame nombres, diff y búsqueda de secretos; detente» | `git add` + `git diff --cached` y una revisión entendible |
| Publicar | «La revisión está aprobada. Crea un repo privado, haz commit y `push`; devuelve URL, rama y hash» | URL, `origin`, rama `main`, hash corto y estado limpio |
| Recuperar | «Deshaz solo el cambio de `RECOVERY-DEMO.md` y luego clona el repo en otra carpeta; compara hashes» | archivo restaurado y dos hashes iguales |

La misma secuencia sirve para una web, una carpeta de documentos o la configuración de OpenClaw: cambia el contenido, no el método.

## Regla de seguridad

No conviertas `~/.openclaw` completo en un repositorio. Trabaja en una carpeta nueva llamada `mi-agente-infra` y copia únicamente archivos revisados.

### Puedes incluir después de revisarlos

- `IDENTITY.md`
- `SOUL.md`
- `AGENTS.md`
- `TOOLS.md`
- `HEARTBEAT.md`
- `BOOTSTRAP.md`
- README y plantillas sanitizadas

`USER.md` y `MEMORY.md` pueden contener información privada: solo incluye versiones sanitizadas si entiendes exactamente qué dicen.

### Nunca incluyas

- `openclaw.json`, `.env` o sus backups
- tokens, contraseñas, API keys o llaves privadas
- `credentials/`, pairing, `identity/`, `devices/`
- logs, bases SQLite, medios o estado operativo

Un repositorio privado reduce exposición, pero no transforma un token publicado en algo seguro.

## Ruta cero · preparar el equipo desde cero

Si no tienes cuenta de GitHub, Git o GitHub CLI, completa esta lista antes del Checkpoint 1. No necesitas saber programar para seguirla.

1. **Crear la cuenta:** abre [github.com/signup](https://github.com/signup), registra un correo al que tengas acceso y confirma el mensaje de verificación. Recuerda tu nombre de usuario; no compartas tu contraseña.
2. **Instalar Git:** descarga el instalador correspondiente a tu sistema en [git-scm.com/downloads](https://git-scm.com/downloads). Acepta las opciones predeterminadas. En Windows, abre una terminal nueva después de instalar.
3. **Instalar GitHub CLI:** sigue [cli.github.com/manual/installation](https://cli.github.com/manual/installation) y elige Windows, macOS o Linux.
4. **Comprobar instalaciones:**

   ```bash
   git --version
   gh --version
   ```

   Deben aparecer dos versiones. Si algún comando dice que no existe, vuelve al paso de instalación de esa herramienta.

5. **Conectar tu cuenta desde el navegador:**

   ```bash
   gh auth login --web --git-protocol https
   gh auth status
   ```

   Elige GitHub.com y HTTPS cuando la CLI lo pregunte. La contraseña se escribe únicamente en GitHub; nunca en Telegram ni en un archivo del proyecto.

Si el correo no está verificado, aparece otra cuenta o `gh auth status` falla, detente y consulta al instructor antes de continuar.

> **Importante:** Git se instala en tu computadora y guarda el historial local. GitHub es la copia remota. Puedes crear una carpeta normal primero y convertirla después en repositorio cuando OpenClaw ejecute `git init`; no tienes que crear el agente dentro de Git desde el comienzo.

## Checkpoint 1 · Preflight

Pídele al agente desde Telegram:

> Sin modificar nada, verifica si Git y GitHub CLI están disponibles y si GitHub CLI está autenticado. Ejecuta `git --version`, `gh --version` y `gh auth status`. No muestres tokens. Dime qué falta.

Si falta autenticación, una persona debe completar el navegador:

```bash
gh auth login --web --git-protocol https
```

## Checkpoint 2 · Preparar sin publicar

Descarga `gitignore-openclaw.example` de esta sesión y guárdalo como `.gitignore` dentro de `mi-agente-infra`. Copia también `RECOVERY-DEMO.md` a la raíz de `mi-agente-infra`; ese archivo descartable se usará después para practicar restauración sin arriesgar tu configuración.

Prompt:

> Trabaja solo dentro de `[RUTA]/mi-agente-infra`. Prepara un snapshot sanitizado de mi agente. No leas ni copies secretos ni estado operativo. Incluye únicamente los Markdown que yo nombre. Inicializa Git en `main`, agrega `.gitignore` y los archivos permitidos. Antes del commit, muéstrame el estado, los nombres staged, el diff y una búsqueda de patrones sensibles. No hagas commit ni push todavía.

Debes ver y entender estas cuatro evidencias:

```bash
git status --short
git diff --cached --name-status
git diff --cached
git grep --cached -n -I -E 'ghp_|github_pat_|sk-|api.?key|bot.?token|password'
```

Si no hay salida y el comando termina con código 1, no encontró patrones. Si aparece un valor real, detente. Retira el archivo del staging y consulta al instructor.

El instructor demostrará el bloqueo con `sensitive-pattern-demo.txt`, un fixture público que contiene un patrón ficticio y nunca una credencial real. El archivo debe aparecer en la búsqueda sensible y retirarse del staging antes de continuar.

## Checkpoint 3 · Commit y repo privado

Cuando la revisión esté limpia, autoriza explícitamente el commit y la publicación:

> La revisión está aprobada. Crea un commit con un mensaje que describa la decisión, crea en mi cuenta un repositorio privado llamado `mi-agente-infra`, agrega `origin` y publica. Al final devuelve la URL, la rama, el hash corto y `git status`.

Flujo esperado:

```bash
git commit -m "chore: versiona configuración sanitizada del agente"
gh repo create mi-agente-infra --private --source=. --remote=origin --push
git remote -v
git status --short --branch
git rev-parse --short HEAD
```

Comprueba en GitHub que el repositorio diga **Private** y que el hash corresponde al commit local.

## Checkpoint 4 · Demostrar recuperación

### Recuperar un archivo sin commit

Usa exclusivamente `RECOVERY-DEMO.md`:

```bash
git diff -- RECOVERY-DEMO.md
git restore -- RECOVERY-DEMO.md
git status --short
```

### Reconstruir desde GitHub

```bash
cd ..
gh repo clone TU_USUARIO/mi-agente-infra recuperacion-mi-agente
git -C recuperacion-mi-agente rev-parse --short HEAD
git -C mi-agente-infra rev-parse --short HEAD
```

Los dos hashes deben coincidir.

## Entrega

Crea `entregas/<tu-usuario>/S03.md` con:

- nombre del repo y confirmación de que es privado;
- hash corto del commit validado;
- lista de archivos versionados;
- evidencia de que no se rastrean secretos;
- evidencia de la recuperación local y del clon, incluidos los dos hashes coincidentes;
- URL privada o captura sin secretos de la issue puente a S04;
- una frase: «ahora puedo reconstruir mi agente porque…».

No pegues tokens, rutas privadas completas ni capturas que muestren credenciales.

## Puente a S04

Crea la issue en tu repositorio privado `mi-agente-infra`, llámala `Mejorar una regla de mi agente` e incluye:

1. problema observable;
2. resultado esperado;
3. evidencia que demostraría que quedó resuelto.

Guarda su URL privada o una captura sin secretos en `entregas/<tu-usuario>/S03.md`.
