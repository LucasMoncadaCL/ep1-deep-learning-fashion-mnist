# Informe de colaborador - Ignacio Silva

**Estado:** READY_FOR_REVIEW

## Metas orientativas

- establecer el contrato de datos y entorno reproducible;
- realizar EDA y preprocesamiento justificado;
- implementar y validar el baseline E0;
- comparar activaciones y pérdidas si la base queda estable;
- evaluar L2 si existe evidencia de sobreajuste y el tiempo lo permite.

## Trabajo realizado

- Se creó el entorno local obligatorio con `uv venv --python 3.12 .venv`.
- Se definió y bloqueó el stack inicial en `pyproject.toml` y `uv.lock`.
- Se implementó la carga reutilizable de Fashion-MNIST, validación del contrato, split estratificado desde índices y preprocesamiento.
- Se verificó la carga efectiva del dataset oficial: train `(60000, 28, 28)`, test `(10000, 28, 28)`, `uint8`, píxeles `[0, 255]` y distribución balanceada de 6.000/1.000 casos por clase.
- El split con seed 42 produjo 54.000 ejemplos de train y 6.000 de validation, con 5.400/600 ejemplos por clase, sin solapamiento y con cobertura completa del train oficial.
- Se entrenó E0 durante 20 épocas exclusivamente con train/validation; el test oficial no fue evaluado.
- Se creó y ejecutó desde kernel limpio `notebooks/01_ignacio_data_baseline.ipynb`, con EDA, contrato de datos y E0.
- Se añadió un informe formal en LaTeX con resultados, figuras y rutas relativas verificadas; no se generó PDF porque este equipo no tiene instalado un motor LaTeX.

## Archivos creados o modificados

- `pyproject.toml` y `uv.lock`.
- `src/ep1_fashion_mnist/data.py`.
- `src/ep1_fashion_mnist/model.py`.
- `src/ep1_fashion_mnist/experiment.py` y `src/ep1_fashion_mnist/visualization.py`.
- `tests/test_data_validation.py`.
- `notebooks/01_ignacio_data_baseline.ipynb`.
- `docs/latex/collaborators/ignacio/main.tex` y su guía de compilación.
- `results/figures/D0_train_examples.png`, `results/figures/D0_train_class_distribution.png` y `results/figures/E0_curves.png`.
- `results/figures/E1_activation_validation_accuracy.png` y `results/figures/E2_loss_validation_accuracy.png`.
- `results/tables/E0_validation_summary.md`.
- `results/tables/E1_E2_validation_comparison.md`.

## Evidencia del entorno uv

- `uv --version`: `uv 0.12.10`.
- `python --version` dentro de `.venv`: `Python 3.12.14`.
- `sys.executable`: `C:\\Users\\yvl\\Documents\\GitHub\\ep1-deep-learning-fashion-mnist\\.venv\\Scripts\\python.exe`.
- comandos ejecutados: `uv venv --python 3.12 .venv`, `uv sync` y `uv lock --check`.
- versiones resueltas: TensorFlow 2.21.0, NumPy 2.5.3, Pandas 3.0.5 y scikit-learn 1.9.1.
- pruebas dentro de `.venv`: 12/12 correctas con `python -m unittest discover -s tests -v` y `PYTHONPATH=src`.
- disponibilidad computacional comprobada: CPU detectada (`/physical_device:CPU:0`); GPU no disponible en TensorFlow nativo de Windows, por lo que las ejecuciones usaron CPU.

## Decisiones técnicas

| Decisión | Alternativas | Justificación | Evidencia |
|---|---|---|---|
| Mantener imágenes como matrices 28×28 normalizadas, y aplicar `Flatten` dentro del modelo | Aplanar al cargar los datos | Conserva imágenes utilizables para EDA y visualización sin cambiar la entrada efectiva de la MLP | `data.py`, `model.py` y prueba de salida `(None, 10)` |
| One-hot encoding con Softmax y categorical crossentropy para E0 | Etiquetas sparse con sparse categorical crossentropy | Es coherente con la hipótesis E0 definida y permite comprobar explícitamente la forma de las etiquetas | `one_hot_encode`, `baseline.json` |
| Conservar ReLU + categorical crossentropy como control | Tanh, Sigmoid y MSE | Bajo la misma configuración, ReLU y CCE tuvieron las métricas de validation más altas | tabla y figuras E1/E2 |

## Experimentos

| ID | Configuración | Objetivo | Resultado | Evidencia |
|---|---|---|---|---|
| D0 | Carga Keras + split estratificado 90/10, seed 42 | Validar contrato y preprocesamiento | Correcto: 54.000/6.000, 5.400/600 por clase, `float32 [0,1]` | ejecución de `prepare_fashion_mnist()`, tests y figuras D0 |
| E0 | `[256,128]`, ReLU, Softmax, CCE, SGD 0,01, batch 128, 20 épocas | Establecer control reproducible | Accuracy val. 0,8722; Precision pond. 0,8737; Recall pond. 0,8722; F1 pond. 0,8726 | `E0_curves.png`, tabla E0 y notebook ejecutado |
| E1_tanh | Solo activación: Tanh | Comparar activación con E0 como control | Accuracy val. 0,8643; F1 pond. 0,8647 | `configs/E1_tanh.json` y corrida local trazable |
| E1_sigmoid | Solo activación: Sigmoid | Comparar activación con E0 como control | Accuracy val. 0,7535; F1 pond. 0,7490 | `configs/E1_sigmoid.json` y corrida local trazable |
| E2_mse | Solo loss: MSE | Contrastar loss con CCE manteniendo ReLU | Accuracy val. 0,7370; F1 pond. 0,7168 | `configs/E2_mse.json` y corrida local trazable |

## Reproducción y verificaciones

```powershell
uv sync --frozen
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Para cargar y validar el dataset real, ejecutar `prepare_fashion_mnist()` desde `ep1_fashion_mnist.data`. La descarga queda en la caché local de Keras; los datos no se versionan.

## Desviaciones respecto del plan

No se evaluó L2: las curvas de E0 no muestran un gap train/validation que justifique introducir regularización en este bloque. Se deja esa decisión para una comparación explícita posterior si aparece evidencia de sobreajuste al cambiar capacidad u optimización.

El repositorio no tenía una rama `develop` al iniciar; la rama de Ignacio se creó desde `main`. La integración debe conservar el flujo documentado: revisión de Cesar y merge hacia `develop` cuando esta rama exista.

## Limitaciones y resultados negativos

- Sigmoid alcanzó accuracy de validation 0,7535; bajo este control fue claramente inferior a ReLU.
- MSE alcanzó accuracy de validation 0,7370 y F1 ponderado 0,7168; no se recomienda como loss de control para esta clasificación multiclase.
- La ejecución nativa de Windows usó CPU; TensorFlow moderno informó que la GPU requiere WSL2. Esto no afecta las verificaciones funcionales, pero debe declararse al comparar tiempos.
- El informe LaTeX está validado como fuente y sus figuras se resolvieron por ruta relativa; no se compiló a PDF porque no se detectó `pdflatex` ni `latexmk` en el equipo. No se versiona PDF sin revisión formal.

## Análisis del baseline

Durante E0, la accuracy de validation aumentó de 0,7592 a 0,8722 y la loss de validation bajó de 0,7395 a 0,3666. En la época 20, train/validation quedaron cerca (accuracy 0,8687/0,8722; loss 0,3751/0,3666); por lo tanto no hay evidencia clara de sobreajuste en esta corrida. El baseline sigue siendo una referencia, no un modelo definitivo: faltan capacidad, learning rate, batch size, optimización y regularización.

## Asuntos abiertos

- Cesar debe revisar este bloque antes de que Lucas tome sus decisiones como base aceptada.
- Generar curvas comparativas de activación y pérdida para integrar la narrativa del notebook final. El test sigue sin evaluación.
- Confirmar el manifiesto en Colab durante la validación final del proyecto.

## Resumen para el handoff a Lucas

Usar E0 como control reproducible, no como selección final. La evidencia actual favorece conservar ReLU y categorical crossentropy mientras se estudian learning rate, batch size y capacidad. Para cada comparación, partir de `configs/baseline.json`, crear otro ID y cambiar una sola variable. Ejecutar con `run_validation_experiment` y conservar las métricas de validation; no invocar evaluación sobre test.
