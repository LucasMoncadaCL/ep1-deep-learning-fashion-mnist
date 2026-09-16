# Índice de entrega — Ignacio Silva

**Estado:** `READY_FOR_REVIEW`  
**Rama:** `codex/ignacio-data-baseline`  
**Revisor requerido:** Cesar Rojas

Este archivo es la puerta de entrada para reproducir, revisar y continuar el bloque inicial sin depender de conversaciones previas.

## Qué está entregado

| Área | Fuente de verdad |
|---|---|
| Contrato y preparación de datos | `src/ep1_fashion_mnist/data.py`, `docs/DATA_CONTRACT.md` |
| Validadores y pruebas | `src/ep1_fashion_mnist/data_validation.py`, `tests/test_data_validation.py` |
| Modelo MLP | `src/ep1_fashion_mnist/model.py` |
| Ejecutor de experimentos | `src/ep1_fashion_mnist/experiment.py` |
| Visualizaciones reutilizables | `src/ep1_fashion_mnist/visualization.py` |
| Notebook ejecutado | `notebooks/01_ignacio_data_baseline.ipynb` |
| Configuraciones | `configs/baseline.json`, `configs/E1_tanh.json`, `configs/E1_sigmoid.json`, `configs/E2_mse.json` |
| Evidencia seleccionada | `results/figures/` y `results/tables/` |
| Informe operativo | `docs/collaborators/ignacio/REPORT.md` |
| Informe formal | `docs/latex/collaborators/ignacio/main.tex` |
| Handoff posterior | `docs/handoffs/RUN_HANDOFF_02_LUCAS.md` |

## Reproducción mínima

Ejecutar desde la raíz del repositorio, dentro de la rama de Ignacio:

```powershell
uv sync --frozen
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\jupyter.exe nbconvert --to notebook --execute --inplace notebooks\01_ignacio_data_baseline.ipynb --ExecutePreprocessor.timeout=120
```

Resultado esperado: 12 pruebas correctas; notebook ejecutado sin traceback; E0 cercano a accuracy validation 0,8722. Pequeñas variaciones numéricas solo deben investigarse si cambian la conclusión experimental.

## Control que debe usar Lucas

E0 es el control de las siguientes comparaciones: `[256,128]`, ReLU, Softmax, categorical crossentropy, SGD con learning rate 0,01, batch 128, 20 épocas y sin regularización. No es el modelo final.

Comando para reproducirlo sin modificar el notebook:

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m ep1_fashion_mnist.experiment configs\baseline.json --output results\runs\e0_reproduced
```

## Límites que no se deben cruzar

- No evaluar ni ajustar con `X_test`/`y_test`.
- No cambiar más de una variable por experimento.
- No cambiar `baseline.json` como si fuera una nueva ejecución; crear una configuración con ID nuevo.
- No asumir que E0 es la selección final.
- No pasar Handoff 01 a `ACCEPTED` sin revisión de Cesar.

## Pendiente fuera de esta etapa

Learning rate, batch size, capacidad y Early Stopping corresponden a Lucas. Optimizadores, Dropout, BatchNorm, L2, evaluación final, matriz de confusión, análisis por clase y test final corresponden a Cesar e integración. El PDF del informe de Ignacio se genera solo si hay motor LaTeX instalado y tras revisión formal.
