# Mini-spec S07 · Dar una interfaz a tu capstone

Estado: contrato de práctica aprobado para construir. Los archivos iniciales son un starter; aún no implementan la web completa.

## Promesa observable

Tu web corre en tu equipo, guarda una petición, recibe la salida real de tu skill y muestra evidencia y faltantes. El ejemplo docente usa postulación laboral; conserva el dominio que elegiste en S06.

## Responsabilidades

- Navegador: recoge datos, pide guardarlos y muestra estados; no genera el análisis por sí solo.
- API local: valida entradas, genera ID, conserva petición y sirve el resultado correspondiente.
- Agente por Telegram: analiza y redacta según tus skills; revisa la salida e importa un archivo JSON mediante una herramienta local.
- Persona: contrasta afirmaciones y evidencias antes de usar un borrador.

Para otro dominio, sigue el [ejemplo resuelto de inventario y plantilla de adaptación](TRANSFERIR.md). El contrato laboral de abajo solo rige para postulación; conserva las rutas/estados y adapta esquema, validador y pruebas con tu contrato S06.

## Contrato del ejemplo

`POST /api/requests` recibe `profile` (lista de hechos con `id` y `text`) y `offer` (`requirements` y `untrusted_text`). Devuelve 201, ID generado y estado `pending`, con `result: null`.

`GET /api/requests/{id}` devuelve esa petición con su estado actual o404 si no existe. `GET /health` devuelve `{"status":"ok"}`. Los archivos se guardan en una carpeta controlada por el servidor; el navegador no elige rutas.

El importador `python import_result.py ID ARCHIVO_JSON --data-dir CARPETA` es local. Solo acepta el contrato de S06; los IDs deben existir y `send_allowed` debe ser literalmente `false`. Un borrador válido produce estado `ready`; datos insuficientes, `needs_input`; un resultado inválido deja `error` recuperable. La validación de estructura no demuestra que una afirmación sea verdadera.

## Criterios de aceptación

1. El navegador realiza peticiones a una API real en localhost; no sustituye la respuesta con contenido precargado.
2. Al crear una petición, se ve pendiente hasta que el agente entregue una salida validada.
3. SQL queda respaldado por E1 y Python como brecha en los datos sintéticos. Cambiar dominio exige nuevas pruebas con sus propios hechos.
4. El mismo ID conserva su entrada y resultado al recargar y reiniciar el servidor.
5. Una evidencia inexistente se rechaza; al corregir el resultado se puede recuperar la petición.
6. Perfil vacío produce petición utilizable para que el agente solicite datos; no inventa experiencia. Oferta vacía impide crear petición y explica qué falta.
7. Texto externo se presenta como texto, sin ejecutar HTML o instrucciones incrustadas.
8. Escritorio y móvil permiten completar la tarea; etiquetas, foco visible, teclado y contraste se verifican.
9. Se usa frontend-design con un contrato visual y se registra una iteración con antes/después verificable.
10. El README permite reiniciar el proyecto y deja claro qué se ejecuta localmente, qué hace el agente y qué aún no se ha comprobado.

## Contrato visual

Mesa de comparación con afirmación y evidencia frente a frente; brechas y preguntas distinguibles sin depender solo del color. Tokens del curso: tinta #0d253d, fondo #f6f9fc, papel #ffffff, acción #533afd, borde #e3e8ee; espaciado8/16/24/32. Tipografía legible, títulos ligeros, texto alineado a izquierda. No agregar adornos que compitan con la evidencia. En móvil, una columna conserva todas las acciones. Comprueba contraste de cada combinación, no asumas que un token lo garantiza.

## Fuera de alcance de S07

Hosting, cuentas, pagos, OCR, envío de postulaciones y ejecución de comandos recibidos del navegador. S08 automatiza comprobaciones de esta misma web; S09 decide y ensaya despliegue compatible con su backend.
