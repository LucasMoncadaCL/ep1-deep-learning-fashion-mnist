# E0 — resumen de validation

**Configuración:** `configs/baseline.json` · **Seed:** 42 · **Partición:** train 54.000 / validation 6.000.  
**Importante:** el conjunto de test oficial no fue evaluado en esta ejecución.

| Medida | Resultado |
|---|---:|
| Parámetros entrenables | 235.146 |
| Accuracy de validation | 0,8722 |
| Precision macro | 0,8737 |
| Recall macro | 0,8722 |
| F1 macro | 0,8726 |
| Precision ponderada | 0,8737 |
| Recall ponderado | 0,8722 |
| F1 ponderado | 0,8726 |
| Loss de train (época 20) | 0,3751 |
| Loss de validation (época 20) | 0,3666 |

La pérdida de validation disminuyó de 0,7395 a 0,3666 y la accuracy de validation aumentó de 0,7592 a 0,8722 durante las 20 épocas. Como validation contiene 600 ejemplos por clase, las métricas macro y ponderadas coinciden en esta corrida. E0 es un control inicial; no es la configuración final ni habilita evaluación sobre test.
