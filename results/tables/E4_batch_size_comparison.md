# E4 — comparación controlada de batch size

Todos los experimentos usan seed 42, la misma partición estratificada, arquitectura `[256, 128]`, ReLU, categorical crossentropy, SGD, `learning_rate=0.1`, 20 épocas y ninguna regularización. La única variable experimental es el batch size. El conjunto oficial de test no fue evaluado.

| ID | Batch size | Accuracy validation | F1 Macro | Mejor val. accuracy (época) | Mejor val. loss (época) | Gap final accuracy | Gap final loss | Duración CPU | Segundos/época |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| E4_batch_32 | 32 | 0,8860 | 0,8864 | 0,8912 (12) | 0,3103 (9) | 0,0534 | 0,2022 | 57,46 s | 2,87 s |
| E4_batch_128 | **128** | **0,8933** | **0,8936** | **0,8938 (13)** | **0,3009 (18)** | 0,0298 | 0,0885 | 20,98 s | 1,05 s |
| E4_batch_512 | 512 | 0,8745 | 0,8771 | 0,8745 (19) | 0,3489 (20) | **0,0100** | **0,0303** | **10,01 s** | **0,50 s** |

`Gap final accuracy = train_accuracy - val_accuracy`; `gap final loss = val_loss - train_loss`. Los gaps se interpretan junto con las curvas y no como criterio aislado.

## Decisión

Se mantiene `batch_size=128` como control para E5. Logró la mayor accuracy y el mayor F1 Macro finales, con un costo moderado y gaps menores que el batch 32. Frente a 32, mejoró 0,73 puntos porcentuales de accuracy y 0,72 puntos de F1 Macro, redujo el tiempo de entrenamiento en aproximadamente 63,5 % y mostró menor separación entre train y validation.

El batch 32 alcanzó su menor `val_loss` en la época 9 y luego se deterioró hasta un gap final de loss de 0,2022; además, tardó 57,46 segundos. El batch 512 fue el más eficiente y presentó los gaps más bajos, pero terminó 1,88 puntos porcentuales por debajo de 128 en accuracy y todavía mejoraba al finalizar el presupuesto de 20 épocas. Por ello se conserva como alternativa orientada a costo, no como candidato principal.

## Evidencia

- `results/tables/E3_E5_validation_metrics.md` — Accuracy, Precision, Recall y F1, macro y ponderadas.
- `results/figures/E4_batch_size_validation_accuracy.png`
- `results/figures/E4_batch_size_validation_loss.png`
- Registros regenerables locales bajo `results/runs/E4_batch_*`
