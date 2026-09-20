# F0 — configuración y protocolo congelados antes de test

**Estado:** congelado antes de test. El conjunto oficial de test permanece sin evaluación ni predicción.

## Configuración seleccionada

| Componente | Valor congelado |
|---|---|
| Arquitectura | `[256, 128]` |
| Activación oculta / salida | ReLU / Softmax de 10 unidades |
| Loss / etiquetas | categorical crossentropy / one-hot |
| Optimizador / learning rate | SGD / `0,1` |
| Batch / épocas | 128 / 20 |
| Dropout | `0,2` tras cada capa oculta |
| Batch Normalization | desactivada |
| L2 | `0` |
| Early Stopping | desactivado |
| Seed | 42 |

## Criterio y protocolo de selección

La candidata se seleccionó por Accuracy, F1 Macro, curvas de validation, gaps, complejidad y evidencia de E6-E9. E7 eligió Dropout `0,2`; E8 y E9 descartaron Batch Normalization y L2 en las condiciones evaluadas. La repetición con seed 7 confirmó que L2 `1e-4` quedó por debajo del control sin L2 en ambas seeds disponibles.

Se adopta la estrategia **evaluar el modelo seleccionado que conserva el split 54.000/6.000**. No se reentrenará con los 60.000 ejemplos oficiales: el modelo final se entrenará una vez con la configuración congelada y se evaluará sobre los 10.000 ejemplos de test exactamente una vez. Las 20 épocas se fijan antes de test porque la mejor validation loss/accuracy del control aparece al final del presupuesto y no existe evidencia material para Early Stopping.

## Presupuesto de test

1. Entrenar una única vez el modelo congelado con train 54.000 y validation 6.000.
2. Evaluar y predecir sobre test oficial una sola vez.
3. Calcular métricas globales y por clase, matriz de confusión y ejemplos de errores.
4. No realizar ningún ajuste posterior desde test.

La configuración exacta está en `configs/F0_frozen_config.json`.
