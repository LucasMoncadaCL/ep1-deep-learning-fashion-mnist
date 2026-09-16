# Run Handoff 03 - Cesar Rojas

**Estado:** WAITING_ON_PREDECESSOR  
**Responsable:** Cesar Rojas  
**Revisor de salida:** Lucas Moncada  
**Destino:** integración grupal

## Entrada obligatoria desde Lucas

Esta sección debe ser completada al cerrar el Handoff 02:

- estado o commit revisado: pendiente;
- configuración de control: pendiente;
- infraestructura y módulos públicos: pendiente;
- tabla de hiperparámetros: pendiente;
- riesgos y decisiones abiertas: pendiente.

## Misión

Evaluar optimizadores y regularización, consolidar el análisis de métricas y errores, y preparar una propuesta final para decisión grupal. Test solo puede abrirse después de congelar configuración y protocolo.

Cesar debe sincronizar el mismo entorno mediante `uv` y ejecutar todo desde el `.venv` del repositorio. Cualquier cambio de dependencia debe quedar bloqueado y comunicado antes de generar resultados comparables.

## Metas orientativas

Estas son **metas mínimas y orientativas, ampliables con justificación técnica**. No representan una lista exhaustiva ni inmutable: Cesar puede incorporar o reajustar pasos necesarios, siempre que respete el alcance de la guía maestra y documente las decisiones, la evidencia y su efecto sobre la integración final.

- comparar SGD, RMSProp y Adam bajo un control explícito;
- conservar el entorno uv aceptado para evitar diferencias de dependencias;
- retunear learning rate en una segunda etapa claramente separada si es necesario;
- evaluar Dropout, Batch Normalization y L2 de forma controlada;
- consolidar Accuracy, Precision, Recall y F1;
- producir matrices de confusión y análisis visual de errores;
- documentar criterios de selección antes de evaluar test;
- integrar la evaluación final sin convertir test en validation.

## Entregables

- código reutilizable de evaluación y visualización;
- `notebooks/03_cesar_optimization_evaluation.ipynb`;
- tablas y figuras finales seleccionadas;
- `docs/collaborators/cesar/REPORT.md` completo;
- decisiones y checklist actualizados;
- propuesta de configuración final con trade-offs;
- paquete de evidencia para integrar `EP1_FashionMNIST_FINAL.ipynb`.

## Criterios de salida

- comparaciones de optimización y regularización son interpretables;
- pruebas y evaluación ejecutadas desde el `.venv` creado con `uv`;
- métricas están calculadas e interpretadas correctamente;
- configuración final fue congelada antes de test;
- evaluación de test se ejecutó una sola vez según el protocolo acordado;
- errores por clase y limitaciones están documentados;
- resultados pueden rastrearse a configuración y código;
- informe permite a todo el grupo preparar la defensa.
