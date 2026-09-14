# Extensión opcional · Preparar sin enviar

Estos fragmentos ilustran una integración futura. No se instalan en el workflow ni se ejecutan durante la práctica. Requieren credenciales propias y autorización explícita para el destinatario. Una plantilla preparada no acredita un mensaje enviado.

Mensaje propuesto: `Capstone CI: RESULTADO · COMMIT · URL_RUN`. Nunca incluir valores de secrets, datos personales ni logs completos. En Actions usar contexto de resultado adecuado y conservar fallo de tests aunque una notificación falle.

## Telegram

API oficial: https://core.telegram.org/bots/api#sendmessage . Guardar token como `TELEGRAM_BOT_TOKEN` y destino como `TELEGRAM_CHAT_ID` en secrets. Referenciarlos por env en step separado. Ejemplo Python **inactivo**, requiere requests fijado; al activarlo intencionalmente realiza envío:

```python
import os, requests
requests.post(
    'https://api.telegram.org/bot' + os.environ['TELEGRAM_BOT_TOKEN'] + '/sendMessage',
    json={'chat_id': os.environ['TELEGRAM_CHAT_ID'], 'text': os.environ['CI_MESSAGE']},
    timeout=15,
).raise_for_status()
```

No imprimir URL: contiene token. Antes de activar, controlar errores sin volcar URL/token, destino y autorización, y limitar eventos de confianza. No usar el bot del curso ni un chat ajeno.

## Slack

API oficial: https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/ . Webhook ligado a destino autorizado; guardarlo en `SLACK_WEBHOOK_URL`. Ejemplo Python **inactivo**, requiere requests:

```python
import os, requests
requests.post(os.environ['SLACK_WEBHOOK_URL'],
              json={'text': os.environ['CI_MESSAGE']}, timeout=15).raise_for_status()
```

La URL también es credencial. No imprimir excepciones que la expongan. Los PR de forks normalmente no reciben secrets. No ampliar privilegios para facilitar una notificación; núcleo CI sin mensajes sigue siendo verificable.
