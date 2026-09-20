# E9 — comparación controlada de regularización L2

Se parte del control de E8: MLP `[256, 128]`, ReLU, Softmax, categorical crossentropy, SGD con `learning_rate=0,1`, batch 128, 20 épocas, seed 42, Dropout `0,2` y Batch Normalization apagada. La única variable modificada es la fuerza L2. El conjunto oficial de test no fue evaluado ni se generaron predicciones sobre él.

| ID | L2 | Accuracy validation | F1 Macro | Mejor val. accuracy (época) | Mejor val. loss (época) | Gap final accuracy | Gap final loss |
|---|---:|---:|---:|---:|---:|---:|---:|
| E9_l2_0 | **0** | **0,8997** | **0,8997** | **0,8997 (20)** | **0,2804 (20)** | **0,0021** | 0,0135 |
| E9_l2_1e-4 | 0,0001 | 0,8967 | 0,8970 | 0,8985 (19) | 0,3369 (19) | 0,0025 | **0,0102** |

`Gap final accuracy = train_accuracy - validation_accuracy`; `gap final loss = validation_loss - train_loss`. La loss de la fila con L2 incluye la penalización regularizadora; por tanto, no es directamente equivalente a la loss sin L2 como estimación de ajuste puro.

## Decisión

Se mantiene L2 en cero. La variante `1e-4` no superó la Accuracy ni F1 Macro del control y su mejor accuracy (`0,8985`) permaneció por debajo de la accuracy final sin L2 (`0,8997`). Aunque su gap de loss final fue ligeramente menor, el control ya presenta gaps de generalización muy bajos gracias a Dropout `0,2`, por lo que no se justifica introducir complejidad adicional.

Esta decisión es contextual: no afirma que L2 sea inefectiva en general. No se evaluaron combinaciones de L2 con Batch Normalization porque E8 ya mostró que esa técnica no mejoró el control. El modelo no queda congelado ni se consulta test.

## Evidencia

- `configs/E9_l2_0.json`
- `configs/E9_l2_1e-4.json`
- `results/figures/E9_l2_validation_accuracy.png`
- `results/figures/E9_l2_validation_loss.png`
- Registros regenerables locales bajo `results/runs/E9_l2_*`.
