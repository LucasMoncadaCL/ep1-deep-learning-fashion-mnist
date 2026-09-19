# E5 — comparación controlada de capacidad

Todos los experimentos usan seed 42, la misma partición estratificada, ReLU, categorical crossentropy, SGD, `learning_rate=0.1`, batch 128, 20 épocas y ninguna regularización. La única variable experimental es la arquitectura de capas ocultas. El conjunto oficial de test no fue evaluado.

| ID | Capas ocultas | Parámetros | Accuracy validation | F1 Macro | Mejor val. accuracy (época) | Mejor val. loss (época) | Gap final accuracy | Gap final loss | Duración CPU de referencia |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| E5_capacity_64 | `[64]` | **50.890** | 0,8873 | 0,8881 | 0,8873 (20) | 0,3105 (20) | **0,0100** | **0,0256** | **12,09 s** |
| E5_capacity_256_128 | **`[256, 128]`** | 235.146 | 0,8933 | 0,8936 | 0,8938 (13) | 0,3009 (18) | 0,0298 | 0,0885 | 19,52 s |
| E5_capacity_512_256_128 | `[512, 256, 128]` | 567.434 | **0,8990** | **0,8989** | **0,8990 (20)** | **0,2895 (16)** | 0,0379 | 0,1215 | 31,32 s |

`Gap final accuracy = train_accuracy - val_accuracy`; `gap final loss = val_loss - train_loss`. Los gaps se interpretan junto con las curvas y el costo, no como criterio aislado.

## Decisión

Se selecciona `[256, 128]` como configuración candidata para el handoff a Cesar. Frente a `[64]`, mejora 0,60 puntos porcentuales de accuracy y 0,55 puntos de F1 Macro, con un aumento de costo aceptable para el tamaño del problema. Frente a `[512, 256, 128]`, pierde 0,57 puntos de accuracy y 0,53 puntos de F1 Macro, pero utiliza 58,6 % menos parámetros, tardó 37,7 % menos en la corrida de referencia y presenta gaps menores.

La red grande ofrece el mayor desempeño absoluto, pero su mejora es marginal frente al incremento de 2,41 veces en parámetros y, en la corrida de referencia, 1,60 veces en duración. Los tiempos pueden variar entre ejecuciones y solo se interpretan dentro del mismo entorno; la conclusión se apoya también en parámetros, métricas y gaps. Además, su mejor `val_loss` ocurre en la época 16 y empeora posteriormente mientras train continúa ajustándose. No se adopta como candidata equilibrada, aunque queda registrada como alternativa si el equipo decide priorizar exclusivamente métricas de validation.

## Early Stopping

No se activa una comparación adicional de Early Stopping en esta etapa. Para la candidata `[256, 128]`, la mejor `val_loss` fue 0,3009 en la época 18 y la final fue 0,3015: una diferencia aproximada de 0,0006, sin degradación material de accuracy. El beneficio esperable sería evitar como máximo dos épocas dentro de un entrenamiento corto. Cesar deberá reevaluar esta técnica si los cambios de optimizador o regularización generan una separación sostenida o trasladan la mejor época de forma relevante.

## Evidencia

- `results/tables/E3_E5_validation_metrics.md` — Accuracy, Precision, Recall y F1, macro y ponderadas.
- `results/figures/E5_capacity_validation_accuracy.png`
- `results/figures/E5_capacity_validation_loss.png`
- Registros regenerables locales bajo `results/runs/E5_capacity_*`
