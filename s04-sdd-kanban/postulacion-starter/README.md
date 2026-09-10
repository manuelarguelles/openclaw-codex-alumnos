# Starter · asistente de postulación
Node.js 22+. Sin instalar paquetes, sin red, sin credenciales.
```bash
node --test tests/postulacion.test.mjs
node demo.mjs
```
Los 15 tests fallan antes de implementar: RED intencional. Diseña y aprueba spec/plan primero, luego construye tu implementación.
fixtures.json contiene únicamente datos ficticios. AGENTS.md se usa solo en la carpeta de práctica.
Tests: CA1–CA5. CA6 exige evaluación conversacional real; CA7 exige revisión y trazabilidad. No atribuir al modelo los resultados del núcleo determinista.
