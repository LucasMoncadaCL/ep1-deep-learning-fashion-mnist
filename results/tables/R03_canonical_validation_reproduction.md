# R03 - reproducción canónica de validation

Estas corridas se ejecutaron el 20 de septiembre de 2026 con `src/ep1_fashion_mnist/`, Python 3.12.13 y TensorFlow 2.21.0. No se consultó test. Se realizan para contrastar la auditoría R03, no para retunear ni reemplazar F0.

| Configuración | Accuracy validation | F1 Macro | Lectura |
|---|---:|---:|---|
| SGD, LR 0,1, seed 42 | 0,8952 | 0,8954 | Coincide con la evidencia E6 publicada. |
| Adam, LR 0,001, seed 42 | 0,8912 | 0,8916 | Queda bajo SGD en la métrica final. |
| Sin L2, seed 7 | 0,8902 | 0,8905 | Coincide con la repetición publicada. |
| L2 `1e-4`, seed 7 | 0,8863 | 0,8870 | Coincide con la repetición publicada. |

Una revisión en otro entorno informó un empate prácticamente completo e inversión marginal de la dirección en seed 7. Por eso esta tabla confirma la consistencia del pipeline canónico local, pero no convierte L2 en una conclusión robusta entre entornos.
