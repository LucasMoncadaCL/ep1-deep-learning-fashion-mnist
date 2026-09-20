# E8 — comparación controlada de Batch Normalization

Se parte del control seleccionado en E7: MLP `[256, 128]`, ReLU, Softmax, categorical crossentropy, SGD con `learning_rate=0,1`, batch 128, 20 épocas, seed 42, Dropout `0,2` y L2 `0`. La única variable modificada es Batch Normalization. Cuando está activa, cada bloque oculto usa el orden `Dense lineal → BatchNormalization → ReLU → Dropout`. El conjunto oficial de test no fue evaluado ni se generaron predicciones sobre él.

| ID | Batch Normalization | Parámetros | Accuracy validation | F1 Macro | Mejor val. accuracy (época) | Mejor val. loss (época) | Gap final accuracy | Gap final loss | Duración CPU |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| E8_batch_norm_off | OFF | **235.146** | **0,8997** | **0,8997** | **0,8997 (20)** | **0,2830 (20)** | **0,0021** | **0,0135** | **32,79 s** |
| E8_batch_norm_on | ON | 236.682 | 0,8922 | 0,8911 | 0,8922 (19) | 0,3062 (19) | 0,0294 | 0,0827 | 44,20 s |

`Gap final accuracy = train_accuracy - validation_accuracy`; `gap final loss = validation_loss - train_loss`. Las duraciones corresponden a una corrida CPU local y no son comparables con GPU o Colab.

## Decisión

Se mantiene Batch Normalization desactivada para E9. Activarla redujo 0,75 puntos porcentuales de accuracy y 0,86 puntos de F1 Macro, incrementó ambos gaps y añadió 1.536 parámetros y aproximadamente 11,41 segundos a la corrida de referencia.

El resultado no sostiene que Batch Normalization sea inútil en general: solo indica que, con esta arquitectura, Dropout `0,2`, learning rate `0,1` y 20 épocas, no mejoró el control. E9 evaluará L2 de forma separada manteniendo Batch Normalization apagada.

## Evidencia

- `configs/E8_batch_norm_off.json`
- `configs/E8_batch_norm_on.json`
- `results/figures/E8_batch_norm_validation_accuracy.png`
- `results/figures/E8_batch_norm_validation_loss.png`
- Registros regenerables locales bajo `results/runs/E8_batch_norm_*`.
