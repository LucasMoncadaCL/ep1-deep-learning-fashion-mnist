# E6 — comparación inicial controlada de optimizadores

Todos los experimentos usan la misma partición estratificada, seed 42, arquitectura `[256, 128]`, ReLU, salida Softmax, categorical crossentropy, `learning_rate=0,1`, batch 128, 20 épocas y ninguna regularización. La única variable modificada es el optimizador. El test oficial no fue evaluado ni se generaron predicciones sobre él.

| ID | Optimizador | Accuracy validation | F1 Macro | Mejor val. accuracy (época) | Mejor val. loss (época) | Gap final accuracy | Gap final loss | Duración CPU |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| E6_optimizer_sgd | **SGD** | **0,8952** | **0,8954** | **0,8952 (20)** | **0,2975 (20)** | 0,0287 | 0,0851 | 156,48 s |
| E6_optimizer_rmsprop | RMSProp | 0,1985 | 0,0684 | 0,2010 (1) | 1,7061 (18) | -0,0001 | -0,0065 | **152,47 s** |
| E6_optimizer_adam | Adam | 0,4722 | 0,4166 | 0,5045 (7) | 1,1918 (4) | 0,0006 | -0,0054 | 152,53 s |

`Gap final accuracy = train_accuracy - validation_accuracy`; `gap final loss = validation_loss - train_loss`. Las duraciones corresponden a una corrida CPU local y no son comparables con GPU o Colab.

## Lectura y decisión provisional

Con el learning rate común `0,1`, SGD conservó la convergencia esperada. Adam y RMSProp obtuvieron resultados marcadamente inferiores bajo las mismas condiciones. Esto establece el efecto de cambiar exclusivamente el optimizador con un presupuesto compartido, pero **no** permite concluir que Adam o RMSProp sean inferiores en general: ambos pueden requerir otra escala de learning rate.

Se abre E6b como etapa separada: para cada optimizador adaptativo se ajustará el learning rate manteniendo fijos arquitectura, funciones, batch, épocas, seed y regularización. No se selecciona todavía un optimizador final ni se consulta test.

## Evidencia

- `configs/E6_optimizer_sgd.json`
- `configs/E6_optimizer_rmsprop.json`
- `configs/E6_optimizer_adam.json`
- `results/figures/E6_optimizer_validation_accuracy.png`
- `results/figures/E6_optimizer_validation_loss.png`
- Registros regenerables locales bajo `results/runs/E6_optimizer_*`.
