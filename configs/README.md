# Configuraciones

Este directorio contiene configuraciones versionadas de experimentos. Una configuración debe permitir reconstruir qué se entrenó sin depender de memoria, capturas de pantalla o celdas editadas manualmente.

Reglas:

- no reutilizar un identificador para configuraciones diferentes;
- registrar seed, arquitectura, funciones, optimizador, learning rate, batch, épocas y regularización;
- si una ejecución se desvía de la configuración, documentarlo en el informe del colaborador;
- actualizar una configuración propuesta solo antes de generar evidencia; después debe crearse otra versión o ID.

`baseline.json` representa la hipótesis E0 y puede cambiar antes de su primera ejecución validada. Una vez utilizada como evidencia, los cambios posteriores deberán conservar trazabilidad.
