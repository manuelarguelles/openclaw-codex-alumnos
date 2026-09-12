# Plan reproducible del laboratorio

1. Definir problema, límites y CA en `SPEC.md` antes de construir.
2. Ejecutar un control sin skill y guardar prompt, salida original, entorno y juicio por criterio. No llamar fallo a lo que el control sí hizo bien.
3. Escribir pruebas literales para el validador; correr RED antes de implementar. Conservar comando, stdout, stderr y código de salida.
4. Implementar el validador; correr GREEN. Las pruebas no reemplazan el ensayo de instrucciones con el modelo.
5. Preparar las tres skills con contratos. Ejecutar P1, I1, L1, A1 y los casos de selección por separado; guardar observaciones reales.
6. Ejecutar el flujo de `WORKFLOW.md`; bifurcar únicamente las revisiones independientes sobre entradas inmutables.
7. Refactorizar solo ante un fallo observado, repetir el caso y la regresión. Comparar las descripciones en sesiones nuevas manteniendo lo demás fijo.
8. Revisar diff, reproducibilidad y evidencia antes de versionar. Registrar pendientes de Telegram, activación, fan-out o `/goal` sin convertirlos en PASS.

Esta es la plantilla de trabajo del alumno. El ejemplo docente resuelto se conserva fuera del material público; el alumno aplica los CA a su propio capstone.
