# Tres skills convierten hechos en un borrador revisable

El ejemplo usa un perfil sintético con SQL y una oferta que pide SQL y Python. La entrega es un borrador local con evidencia, brecha y revisión. Necesitas Python 3; para ejecutar las skills, un agente que pueda leer sus instrucciones. No hay dependencias Python externas.

Desde la raíz de tu copia del repositorio:

```bash
python3 -m unittest discover -s s06-skills-workflows/material/lab/workflow/tests -v
```

Lee [SPEC.md](SPEC.md) para conocer los criterios, [PLAN.md](PLAN.md) para el orden de trabajo y [WORKFLOW.md](WORKFLOW.md) para ejecutar la demo con prompts y archivos. [casos.json](casos.json) contiene entradas de prueba y criterios esperados, no salidas observadas. Un fixture es un dato controlado de prueba; aquí todos los perfiles son sintéticos.

Una skill es una instrucción reutilizable para el agente. El workflow fija qué paso consume la salida de otro. El validador solo comprueba estructura e IDs: superar sus pruebas no acredita veracidad, activación implícita, Telegram ni concurrencia real.

En tu capstone, define tres responsabilidades propias y al menos un caso positivo, negativo, de dato ausente y de presión para inventar. Entrega spec, skills, salidas reales y una comparación con control sin skill. No entregues CV reales en el repositorio. [GOAL-ENSAYO.md](GOAL-ENSAYO.md) ofrece una práctica adicional acotada que debes autorizar en tu entorno. El [registro docente](../ENSAYOS.md) distingue resultados observados y límites.
