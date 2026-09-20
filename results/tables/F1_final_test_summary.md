# F1 — evaluación final única sobre test

La configuración `F0_frozen_config` se entrenó con train 54.000/validation 6.000 y se evaluó una única vez sobre los 10.000 ejemplos oficiales de test. Después de esta consulta no se realizaron ajustes.

| Métrica | Test |
|---|---:|
| Accuracy | 0,8838 |
| Precision macro | 0,8844 |
| Recall macro | 0,8838 |
| F1 macro | 0,8836 |
| Precision ponderada | 0,8844 |
| Recall ponderado | 0,8838 |
| F1 ponderado | 0,8836 |

## Métricas por clase

| Clase | Precision | Recall | F1 |
|---|---:|---:|---:|
| T-shirt/top | 0,8721 | 0,7980 | 0,8334 |
| Trouser | 0,9898 | 0,9700 | 0,9798 |
| Pullover | 0,7958 | 0,7990 | 0,7974 |
| Dress | 0,8394 | 0,9250 | 0,8801 |
| Coat | 0,8030 | 0,8070 | 0,8050 |
| Sandal | 0,9795 | 0,9550 | 0,9671 |
| Shirt | 0,7021 | 0,6930 | 0,6975 |
| Sneaker | 0,9238 | 0,9700 | 0,9463 |
| Bag | 0,9710 | 0,9720 | 0,9715 |
| Ankle boot | 0,9674 | 0,9490 | 0,9581 |

La principal dificultad es `Shirt`, seguida por las confusiones visualmente plausibles entre T-shirt/top y Shirt, Pullover y Coat. La matriz de confusión lo respalda; no se ajusta el modelo después de observarlo.

## Evidencia

- `results/figures/F1_test_confusion_matrix.png`
- `results/figures/F1_test_low_confidence_errors.png`
- Registro local protegido: `results/runs/F1_final_test/F1_final_test_record.json`.
