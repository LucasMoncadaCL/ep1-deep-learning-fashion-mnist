# E7 — comparación controlada de Dropout

Se parte del control provisional SGD con `learning_rate=0,1`, arquitectura `[256, 128]`, ReLU, Softmax, categorical crossentropy, batch 128, 20 épocas y seed 42. La única variable modificada es Dropout: se aplica después de cada capa oculta cuando está activo. Batch Normalization y L2 permanecen desactivados. El conjunto oficial de test no fue evaluado ni se generaron predicciones sobre él.

| ID | Dropout | Accuracy validation | F1 Macro | Mejor val. accuracy (época) | Mejor val. loss (época) | Gap final accuracy | Gap final loss | Duración CPU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| E7_dropout_0 | 0,0 | 0,8952 | 0,8954 | 0,8952 (20) | 0,2975 (20) | 0,0287 | 0,0851 | **28,83 s** |
| E7_dropout_0_2 | **0,2** | **0,8997** | **0,8997** | **0,8997 (20)** | **0,2830 (20)** | **0,0021** | **0,0135** | 33,09 s |

`Gap final accuracy = train_accuracy - validation_accuracy`; `gap final loss = validation_loss - train_loss`. Las duraciones corresponden a una corrida CPU local y no son comparables con GPU o Colab.

## Decisión

Se selecciona Dropout `0,2` como control para E8. Mejoró 0,45 puntos porcentuales de accuracy y 0,43 puntos de F1 Macro, mientras redujo el gap final de accuracy de 0,0287 a 0,0021 y el gap de loss de 0,0851 a 0,0135. El costo adicional fue de aproximadamente 4,26 segundos en la corrida de referencia.

Esta selección no evalúa combinaciones con Batch Normalization ni L2: E8 y E9 deberán aislar esas técnicas sobre este control. No se congela todavía el modelo ni se consulta test.

## Evidencia

- `configs/E7_dropout_0.json`
- `configs/E7_dropout_0_2.json`
- `results/figures/E7_dropout_validation_accuracy.png`
- `results/figures/E7_dropout_validation_loss.png`
- Registros regenerables locales bajo `results/runs/E7_dropout_*`.
