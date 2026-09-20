# Contrato de evaluación final y reproducción

## Fuente de verdad

La implementación canónica es `src/ep1_fashion_mnist/`. Las configuraciones versionadas y el ejecutor `run_validation_experiment` son la fuente de verdad para E0--E9; `final_evaluation.py` es la fuente de verdad para F1. Los notebooks no implementan una MLP alternativa ni recalculan métricas con lógica propia.

## F1 decisoria

La evaluación que fundamenta el informe es la corrida local registrada el 19 de septiembre de 2026. Su evidencia versionada es `results/records/F1_final_evaluation_record.json`, vinculada por hash a `configs/F0_frozen_config.json`. Sus métricas son Accuracy `0,8838` y F1 Macro `0,8836` sobre 10.000 ejemplos oficiales de test.

La corrida se realizó después de F0 y no produjo ajustes posteriores. El registro sustituye como evidencia histórica al archivo local e ignorado bajo `results/runs/`.

## Colab

El notebook final puede clonarse desde la rama del repositorio y presentar la evidencia versionada. Puede ejecutar verificaciones de entorno y reproducir comparaciones de validation con el código canónico si se requiere, pero la versión de entrega no vuelve a entrenar ni a predecir sobre `X_test`.

Una repetición de F1 para fines técnicos no puede modificar F0, escoger nuevas métricas ni reemplazar el registro decisorio. Si el docente exige una nueva F1 oficial en Colab, el equipo debe abrir un nuevo protocolo, documentarlo antes de ejecutarlo y regenerar todos los artefactos desde esa única corrida; no se puede elegir entre resultados según su valor.

## Variabilidad de validation

Una seed fija mejora la repetibilidad dentro de un mismo entorno, pero no garantiza identidad bit a bit entre hardware, kernels o versiones. La reproducción canónica actual con Python 3.12.13 y TensorFlow 2.21.0 coincide con los registros originales de las cuatro comparaciones auditadas. Una revisión externa observó diferencias marginales en seed 7; por ello L2 se mantiene en cero como decisión prudente de simplicidad y rendimiento agregado, no como confirmación robusta por dos seeds.
