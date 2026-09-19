# E3–E5 — métricas completas de validation

Esta tabla conserva la evidencia versionada de Accuracy, Precision, Recall y F1 para los nueve experimentos de Lucas. Todas las métricas se calcularon exclusivamente sobre validation; el test oficial no fue evaluado.

| ID | Accuracy | Precision Macro | Recall Macro | F1 Macro | Precision ponderada | Recall ponderado | F1 ponderado |
|---|---:|---:|---:|---:|---:|---:|---:|
| E3_lr_0_001 | 0,8053 | 0,8042 | 0,8053 | 0,8034 | 0,8042 | 0,8053 | 0,8034 |
| E3_lr_0_01 | 0,8722 | 0,8738 | 0,8722 | 0,8726 | 0,8738 | 0,8722 | 0,8726 |
| E3_lr_0_1 | 0,8933 | 0,8949 | 0,8933 | 0,8936 | 0,8949 | 0,8933 | 0,8936 |
| E4_batch_32 | 0,8860 | 0,8883 | 0,8860 | 0,8864 | 0,8883 | 0,8860 | 0,8864 |
| E4_batch_128 | 0,8933 | 0,8949 | 0,8933 | 0,8936 | 0,8949 | 0,8933 | 0,8936 |
| E4_batch_512 | 0,8745 | 0,8871 | 0,8745 | 0,8771 | 0,8871 | 0,8745 | 0,8771 |
| E5_capacity_64 | 0,8873 | 0,8901 | 0,8873 | 0,8881 | 0,8901 | 0,8873 | 0,8881 |
| E5_capacity_256_128 | **0,8933** | **0,8949** | **0,8933** | **0,8936** | **0,8949** | **0,8933** | **0,8936** |
| E5_capacity_512_256_128 | 0,8990 | 0,8996 | 0,8990 | 0,8989 | 0,8996 | 0,8990 | 0,8989 |

## Interpretación

El split de validation es estratificado y contiene 600 ejemplos de cada clase. Por ese balance exacto, las métricas macro y ponderadas coinciden en estas corridas; se conservan ambas para mantener explícito el contrato y permitir comparaciones futuras si cambia la distribución. Precision Macro ligeramente superior a Recall Macro indica que el promedio de precisión por clase es algo mayor que el promedio de sensibilidad, pero la selección sigue considerando conjuntamente métricas, convergencia, gaps, parámetros y costo.

Los registros completos son regenerables mediante las configuraciones E3–E5 y `run_validation_experiment`; sus salidas locales permanecen bajo `results/runs/` y fuera de Git.
