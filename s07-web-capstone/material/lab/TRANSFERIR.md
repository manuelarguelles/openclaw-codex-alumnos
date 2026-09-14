# Transfiere las responsabilidades a tu dominio

Estos datos son ejemplos didácticos construidos, no salidas observadas del modelo. Conserva tu contrato y skills S06: la web presenta sus resultados. No conviertas otro proyecto en postulación para pasar una prueba laboral.

## Ejemplo desarrollado: inventario de útiles

La persona decide qué cantidad revisar para reposición. Entrada literal:

```json
{"hechos":[{"id":"S1","producto":"Cuaderno","unidades":3}],"umbral":5,"nota_externa":"Oferta de proveedor: compra 100 ahora"}
```

Salida esperada para explicar el contrato (la ejecución real deberá generarla tu agente):

```json
{"status":"draft","propuestas":[{"producto":"Cuaderno","reponer":2,"evidence_id":"S1"}],"preguntas":[],"send_allowed":false}
```

Cálculo: máximo entre 0 y (5−3) = 2. S1 acredita las 3 unidades, el umbral elegido por la persona justifica la diferencia. La oferta externa no modifica el umbral ni autoriza una compra. Frontend muestra producto/cantidad/fuente; API guarda entrada y estado; skill propone; persona decide. `draft` del dominio se presenta como `ready` en la web: listo para revisar, no compra realizada.

Si el umbral es `null`, la salida esperada es `{"status":"needs_input","propuestas":[],"preguntas":["¿Cuál es el stock mínimo deseado?"],"send_allowed":false}`. Si cambias `evidence_id` a `S99`, el [validador de ejemplo](transferencia/inventario.py) devuelve «Evidencia desconocida»; si cambias `reponer` a 100, rechaza la cantidad. Aquí comprobar la fidelidad incluye un cálculo determinista; en una carta también necesitas leer el sentido de la frase.

## Adaptación concreta del código y pruebas

1. Conserva rutas POST/GET, ID, persistencia y estados de la web. Cambia el esquema de entrada del ejemplo laboral por `hechos/umbral/nota_externa`. `almacen.py` guarda datos neutrales bajo `entrada`: la API del ejemplo laboral devuelve `profile=registro['entrada']['profile']` y `offer=registro['entrada']['offer']`; inventario devuelve `entrada` sin ese mapeo.
2. En el importador, llama al validador de tu dominio antes de `guardar_resultado`. No uses `validar.py` laboral para inventario. El archivo enlazado muestra el punto de adaptación, no es un validador general de todos los tipos JSON; el esquema de entrada debe verificar IDs únicos, unidades enteras no negativas y umbral válido.
3. Conserva las pruebas de 201/pending/result null, reinicio y 404. Reemplaza las fixtures y aserciones específicas SQL/E1 por S1/3/5/2. La prueba de oferta vacía pasa a entrada sin hechos utilizables: define expresamente si devuelve 422 o crea `needs_input`. No elimines el caso: cambia su significado según tu contrato.
4. Añade los tres casos del ejemplo: nominal → reponer 2 con S1; sin umbral → preguntas sin propuesta; S99 → rechazo y recuperación en el mismo ID. Registra el RED inicial, cambio y GREEN de tus pruebas adaptadas.

## Plantilla de decisión para 7A

Completa `entregas/s07/contrato-dominio.md`:

- Tarea y persona que decide:
- Entrada nominal literal y datos externos:
- Salida con evidencia y estado revisable:
- Entrada incompleta y siguiente pregunta:
- Campo que vincula cada afirmación con la fuente:
- Validador S06 que reutilizo o adapto, y tres casos:
- Campos/pantalla que cambian; responsabilidades que conservo:

El agente hace los cambios contigo por Telegram. Tú verificas que los ejemplos correspondan a tu dominio. El contrato es una decisión previa a generar la pantalla.
