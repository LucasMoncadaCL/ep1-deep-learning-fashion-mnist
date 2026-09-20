# Selección final consolidada

## Configuración congelada antes de test

La selección se realizó exclusivamente con train/validation y quedó congelada en `configs/F0_frozen_config.json` antes de consultar el conjunto oficial de test.

| Componente | Selección | Evidencia de validation |
|---|---|---|
| Arquitectura | MLP `[256, 128]` | Equilibrio entre desempeño, parámetros y gaps en E5. |
| Activación / salida / pérdida | ReLU / Softmax / categorical crossentropy | E1/E2; combinación de control para clasificación multiclase. |
| Optimizador | SGD, learning rate `0,1` | E6b: Accuracy `0,8952`, F1 Macro `0,8954`; mejor compromiso frente a Adam y RMSProp retuneados. |
| Batch size / épocas | `128` / `20` | E4 y curvas E7/E9: la mejor validation accuracy y loss quedan al final de las 20 épocas. |
| Dropout | `0,2` | E7: Accuracy `0,8997`, F1 Macro `0,8997` y gaps menores que sin Dropout. |
| Batch Normalization | desactivada | E8: activarla redujo Accuracy y F1 Macro, y aumentó gaps. |
| L2 | `0` | E9 y repetición seed 7: `1e-4` no mejoró Accuracy ni F1 Macro. |
| Early Stopping | desactivado | No había deterioro ni ahorro material; no se implementó sin una comparación interpretable. |

Las dos repeticiones de la decisión L2 conservaron la dirección de la selección: sin L2 obtuvo Accuracy de validation `0,8997` y `0,8902` (promedio `0,8949`); con L2 `1e-4`, `0,8967` y `0,8863` (promedio `0,8915`).

## Evaluación final única

Después de F0, el modelo seleccionado se entrenó con el split 54.000/6.000 y se evaluó una única vez sobre los 10.000 ejemplos oficiales de test. No se ajustó ningún parámetro después de este resultado.

| Métrica | Test |
|---|---:|
| Accuracy | 0,8838 |
| Precision macro | 0,8844 |
| Recall macro | 0,8838 |
| F1 macro | 0,8836 |
| Precision ponderada | 0,8844 |
| Recall ponderado | 0,8838 |
| F1 ponderado | 0,8836 |

La matriz de confusión muestra dificultades principalmente entre clases de prendas superiores visualmente similares. `Shirt` es la clase con menor F1 (`0,6975`); por ello, este resultado se comunica como limitación del modelo y no se utiliza para hacer nuevos ajustes.

## Trazabilidad

- Decisiones D-014--D-026: `docs/DECISION_LOG.md`.
- Comparaciones: `results/tables/E1_E2_validation_comparison.md`, `E3_learning_rate_comparison.md`, `E4_batch_size_comparison.md`, `E5_capacity_comparison.md`, `E6b_retuned_optimizer_comparison.md`, `E7_dropout_comparison.md`, `E8_batch_norm_comparison.md` y `E9_l2_comparison.md`.
- Protocolo: `results/tables/F0_frozen_protocol.md`.
- Evaluación definitiva: `results/tables/F1_final_test_summary.md` y las figuras `F1_test_*`.
