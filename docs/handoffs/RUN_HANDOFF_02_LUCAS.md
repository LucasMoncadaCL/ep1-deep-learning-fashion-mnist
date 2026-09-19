# Run Handoff 02 - Lucas Moncada

**Estado:** READY_FOR_REVIEW

**Responsable:** Lucas Moncada

**Revisor técnico de salida:** Ignacio Silva

**Aprobación de alcance e integración:** Lucas Moncada, como dueño del repositorio

**Siguiente responsable:** Cesar Rojas

## Entrada aceptada desde Ignacio

Lucas trabajó sobre el Handoff 01 aceptado e integrado: contrato de Fashion-MNIST, split estratificado seed 42 de 54.000/6.000, test oficial sellado, baseline E0 y controles ReLU + categorical crossentropy. El entorno se reconstruyó exclusivamente con `uv` y `.venv`.

## Alcance ejecutado

Las metas fueron mínimas y orientativas, ampliables con justificación técnica. Se completó:

- infraestructura autocontenida para validar configuraciones y registrar métricas, convergencia, gaps, parámetros y duración;
- E3 con learning rates 0,001, 0,01 y 0,1;
- E4 con batch sizes 32, 128 y 512;
- E5 con capacidades `[64]`, `[256, 128]` y `[512, 256, 128]`;
- evaluación condicional de Early Stopping;
- notebook ejecutado, tablas, figuras, decisiones y pruebas automatizadas;
- preparación del Handoff 03 sin utilizar test.

## Configuración candidata

Archivo: `configs/E5_capacity_256_128.json`.

| Componente | Valor |
|---|---|
| Arquitectura | `[256, 128]` |
| Activación oculta | ReLU |
| Salida | 10 unidades Softmax |
| Loss | categorical crossentropy |
| Optimizador | SGD |
| Learning rate | 0,1 |
| Batch size | 128 |
| Épocas | 20 |
| Seed | 42 |
| Regularización | ninguna |
| Parámetros | 235.146 |
| Accuracy validation | 0,8933 |
| Precision Macro validation | 0,8949 |
| Recall Macro validation | 0,8933 |
| F1 Macro validation | 0,8936 |

Esta configuración es una candidata equilibrada para el siguiente control, no el modelo final.

## Decisiones técnicas

- D-014 selecciona `learning_rate=0.1` por mejorar aproximadamente 2,1 puntos frente a 0,01 con duración comparable.
- D-015 mantiene batch 128: batch 32 fue más lento y sobreajustó más; 512 fue eficiente, pero perdió 1,88 puntos de accuracy.
- D-016 selecciona `[256, 128]`: la red grande mejoró 0,57 puntos, pero usó 2,41 veces más parámetros, tardó 1,60 veces más y aumentó los gaps.
- D-017 no activa Early Stopping: en la candidata, la diferencia entre la mejor `val_loss` y la final fue aproximadamente 0,0006 y el ahorro potencial era de dos épocas.
- D-018 hace que el ejecutor rechace `early_stopping=true` hasta que exista un callback real y probado.

## Evidencia verificable

- `notebooks/02_lucas_hyperparameters.ipynb`: ejecutado completamente, 6/6 celdas de código y cero errores.
- `results/tables/E3_learning_rate_comparison.md`.
- `results/tables/E4_batch_size_comparison.md`.
- `results/tables/E5_capacity_comparison.md`.
- `results/tables/E3_E5_validation_metrics.md`, con métricas macro y ponderadas completas.
- Figuras comparativas E3–E5 bajo `results/figures/`.
- `docs/collaborators/lucas/REPORT.md`.
- Decisiones D-014–D-018 en `docs/DECISION_LOG.md`.

## Verificación y reproducción

```powershell
uv sync --frozen
$env:PYTHONPATH = "src"
uv run python -m unittest discover -s tests -v
uv run ruff check src tests
uv run jupyter nbconvert --to notebook --execute --inplace notebooks\02_lucas_hyperparameters.ipynb --ExecutePreprocessor.timeout=600
```

La verificación de cierre debe confirmar `uv lock --check`, 22/22 pruebas, Ruff 0.16.8 limpio, ejecución completa del notebook y ausencia de consultas al test.

## Límites y riesgos

- Las comparaciones usan una seed; las diferencias marginales deben repetirse antes de una decisión final.
- Las duraciones corresponden a CPU local y solo son comparables dentro del mismo entorno.
- La red grande conserva el mayor desempeño absoluto y puede revisitarse si el equipo decide priorizar métricas sobre costo y generalización.
- Early Stopping debe reevaluarse si un nuevo optimizador o técnica de regularización cambia la dinámica de las curvas.
- El ejecutor rechazará `early_stopping=true`; habilitarlo exige implementar primero el callback y ampliar su contrato.
- El test oficial permanece sellado y no puede utilizarse durante nuevas decisiones de ajuste.

## Criterio de aceptación

Ignacio debe realizar la revisión cruzada técnica definida por el flujo del proyecto. Después, Lucas, como dueño del repositorio, debe comprobar que el alcance, la candidata, la evidencia y las restricciones sean coherentes y autorizar la integración. Solo tras ambas validaciones Cesar debe iniciar el Handoff 03 sobre la versión integrada.
