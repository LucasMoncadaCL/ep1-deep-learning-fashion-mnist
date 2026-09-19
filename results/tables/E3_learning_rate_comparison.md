# E3 — comparación controlada de learning rate

Todos los experimentos usan seed 42, la misma partición estratificada, arquitectura `[256, 128]`, ReLU, categorical crossentropy, SGD, batch 128, 20 épocas y ninguna regularización. La única variable experimental es el learning rate. El conjunto oficial de test no fue evaluado.

| ID | Learning rate | Accuracy validation | F1 Macro | Mejor val. accuracy (época) | Mejor val. loss (época) | Gap final accuracy | Gap final loss | Duración CPU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| E3_lr_0_001 | 0,001 | 0,8053 | 0,8034 | 0,8053 (20) | 0,5961 (20) | -0,0065 | -0,0113 | 20,54 s |
| E3_lr_0_01 | 0,01 | 0,8722 | 0,8726 | 0,8722 (20) | 0,3666 (20) | -0,0035 | -0,0084 | 20,52 s |
| E3_lr_0_1 | **0,1** | **0,8933** | **0,8936** | **0,8938 (13)** | **0,3009 (18)** | 0,0298 | 0,0885 | 21,47 s |

`Gap final accuracy = train_accuracy - val_accuracy`; `gap final loss = val_loss - train_loss`. Un valor positivo puede señalar que train se ha separado favorablemente de validation y debe interpretarse junto con las curvas.

## Decisión

Se selecciona `learning_rate=0.1` como control para E4. Superó a `0.01` por 2,12 puntos porcentuales de accuracy y aproximadamente 2,10 puntos de F1 Macro, con un costo temporal similar. La diferencia no se considera marginal para esta etapa.

La selección conserva una advertencia: el gap final de accuracy aumentó a 2,98 puntos, la mejor accuracy de validation apareció en la época 13 y la mejor loss en la 18. Esto no invalida la mejora, pero aporta evidencia para estudiar capacidad y evaluar Early Stopping posteriormente. `0.001` quedó subentrenado con el presupuesto común de 20 épocas y no se amplió su entrenamiento porque eso cambiaría simultáneamente el presupuesto experimental.

## Evidencia

- `results/tables/E3_E5_validation_metrics.md` — Accuracy, Precision, Recall y F1, macro y ponderadas.
- `results/figures/E3_learning_rate_validation_accuracy.png`
- `results/figures/E3_learning_rate_validation_loss.png`
- Registros regenerables locales bajo `results/runs/E3_lr_*`
