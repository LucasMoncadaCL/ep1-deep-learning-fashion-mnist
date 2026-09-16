# E1/E2 — comparación controlada en validation

Todos los experimentos usan la misma partición estratificada, seed 42, arquitectura `[256, 128]`, SGD (`learning_rate=0,01`), batch 128 y 20 épocas. El conjunto de test oficial no fue evaluado.

| ID | Única variable modificada | Accuracy validation | Precision ponderada | Recall ponderado | F1 ponderado |
|---|---|---:|---:|---:|---:|
| E0 | ReLU + categorical crossentropy | **0,8722** | **0,8737** | **0,8722** | **0,8726** |
| E1_tanh | Activación Tanh | 0,8643 | 0,8656 | 0,8643 | 0,8647 |
| E1_sigmoid | Activación Sigmoid | 0,7535 | 0,7472 | 0,7535 | 0,7490 |
| E2_mse | Loss MSE | 0,7370 | 0,7366 | 0,7370 | 0,7168 |

## Lectura posterior

ReLU superó a Tanh por 0,78 puntos porcentuales y a Sigmoid por 11,87 puntos en accuracy de validation. Con ReLU fija, categorical crossentropy superó a MSE por 13,52 puntos. Estas ejecuciones respaldan conservar ReLU y categorical crossentropy como control para los experimentos siguientes; no sustituyen las comparaciones de hiperparámetros, optimización y regularización.
