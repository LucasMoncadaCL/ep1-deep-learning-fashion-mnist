# E6b — retuning separado de learning rate por optimizador

E6 mostró que Adam y RMSProp quedaron limitados con el learning rate común `0,1`. E6b mantiene fijo cada optimizador y cambia únicamente su learning rate a `0,001`; arquitectura `[256, 128]`, ReLU, Softmax, categorical crossentropy, batch 128, 20 épocas, seed 42 y ausencia de regularización permanecen constantes. El test oficial no fue evaluado ni se generaron predicciones sobre él.

| ID | Optimizador | Learning rate | Accuracy validation | F1 Macro | Mejor val. accuracy (época) | Mejor val. loss (época) | Gap final accuracy | Gap final loss |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| E6_optimizer_sgd | **SGD** | 0,1 | **0,8952** | **0,8954** | **0,8952 (20)** | **0,2975 (20)** | **0,0287** | **0,0851** |
| E6b_adam_lr_0_001 | Adam | 0,001 | 0,8912 | 0,8916 | 0,8912 (17) | 0,3043 (12) | 0,0527 | 0,1941 |
| E6b_rmsprop_lr_0_001 | RMSProp | 0,001 | 0,8933 | 0,8929 | 0,8933 (16) | 0,3137 (8) | 0,0476 | 0,2165 |

`Gap final accuracy = train_accuracy - validation_accuracy`; `gap final loss = validation_loss - train_loss`.

## Decisión provisional

Se mantiene SGD con `learning_rate=0,1` como control provisional para E7. RMSProp recuperó una accuracy cercana, pero quedó 0,18 puntos porcentuales por debajo de SGD, con F1 Macro menor, mayor validation loss y gaps finales de accuracy/loss más altos. Adam también recuperó el aprendizaje, pero quedó por debajo de ambos controles y presentó los gaps más altos.

La diferencia entre SGD y RMSProp es pequeña en accuracy; antes del congelamiento F0 deben repetirse las candidatas relevantes con seeds adicionales si esa diferencia sigue siendo importante para la elección final. Esta decisión solo selecciona un control de continuación para regularización; no congela el modelo ni consulta test.

## Evidencia

- `configs/E6b_adam_lr_0_001.json`
- `configs/E6b_rmsprop_lr_0_001.json`
- `results/figures/E6b_retuned_optimizer_validation_accuracy.png`
- `results/figures/E6b_retuned_optimizer_validation_loss.png`
- Registros regenerables locales bajo `results/runs/E6b_*`.
