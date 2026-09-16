# Run Handoff 02 - Lucas Moncada

**Estado:** WAITING_ON_PREDECESSOR  
**Responsable:** Lucas Moncada  
**Revisor de salida:** Ignacio Silva  
**Siguiente responsable:** Cesar Rojas

## Entrada obligatoria desde Ignacio

Esta sección debe ser completada al cerrar el Handoff 01:

- estado o commit revisado: pendiente;
- entorno probado: pendiente;
- contrato de datos: pendiente;
- módulos públicos: pendiente;
- baseline de control: pendiente;
- métricas de referencia: pendiente;
- riesgos y decisiones abiertas: pendiente.

## Misión

Consolidar la infraestructura experimental y estudiar controladamente learning rate, batch size, capacidad y Early Stopping, manteniendo trazabilidad suficiente para entregar a Cesar una configuración candidata, no una conclusión incuestionable.

Lucas debe reconstruir o sincronizar el entorno mediante `uv` y trabajar en el `.venv` del repositorio. No debe reutilizar un entorno personal distinto del aceptado en el handoff de Ignacio.

## Metas orientativas

Estas son **metas mínimas y orientativas, ampliables con justificación técnica**. No representan una lista exhaustiva ni inmutable: Lucas puede incorporar o reajustar pasos necesarios, siempre que respete el alcance de la guía maestra y documente las decisiones, la evidencia y su efecto sobre el siguiente handoff.

- reutilizar el contrato de datos aceptado;
- usar el entorno bloqueado y versionado recibido de Ignacio;
- centralizar construcción, entrenamiento, evaluación y registro;
- ejecutar E3, E4 y E5 con una variable por comparación;
- incorporar Early Stopping solo después de comprender las curvas sin callback;
- comparar desempeño, convergencia, gap, costo y complejidad;
- repetir comparaciones críticas cuando diferencias marginales lo justifiquen.

## Entregables

- código reutilizable de entrenamiento y experimentos;
- `notebooks/02_lucas_hyperparameters.ipynb`;
- configuraciones identificables;
- tabla comparativa trazable;
- figuras seleccionadas;
- `docs/collaborators/lucas/REPORT.md` completo;
- actualización de decisiones y checklist;
- este documento completado con evidencia recibida;
- `RUN_HANDOFF_03_CESAR.md` actualizado con la configuración candidata real.

## Criterios de salida

- infraestructura común usada por todos los experimentos;
- pruebas y experimentos ejecutados desde el `.venv` creado con `uv`;
- cada comparación conserva un control explícito;
- resultados incluyen configuración e ID;
- conclusiones no dependen de test;
- configuración candidata justificada por más de una métrica;
- efectos de complejidad y Early Stopping están interpretados;
- informe y asuntos abiertos completos;
- Cesar puede continuar sin reconstruir el razonamiento desde cero.
