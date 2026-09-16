# Informe de colaborador - Ignacio Silva

**Estado:** IN_PROGRESS

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
- Se implementó la construcción y compilación de la MLP E0. Aún no se ha entrenado E0.

## Archivos creados o modificados

- `pyproject.toml` y `uv.lock`.
- `src/ep1_fashion_mnist/data.py`.
- `src/ep1_fashion_mnist/model.py`.
- `tests/test_data_validation.py`.

## Evidencia del entorno uv

- `uv --version`: `uv 0.12.10`.
- `python --version` dentro de `.venv`: `Python 3.12.14`.
- `sys.executable`: `C:\\Users\\yvl\\Documents\\GitHub\\ep1-deep-learning-fashion-mnist\\.venv\\Scripts\\python.exe`.
- comandos ejecutados: `uv venv --python 3.12 .venv`, `uv sync` y `uv lock --check`.
- versiones resueltas: TensorFlow 2.21.0, NumPy 2.5.3, Pandas 3.0.5 y scikit-learn 1.9.1.
- pruebas dentro de `.venv`: 10/10 correctas con `python -m unittest discover -s tests -v` y `PYTHONPATH=src`.

## Decisiones técnicas

| Decisión | Alternativas | Justificación | Evidencia |
|---|---|---|---|
| Mantener imágenes como matrices 28×28 normalizadas, y aplicar `Flatten` dentro del modelo | Aplanar al cargar los datos | Conserva imágenes utilizables para EDA y visualización sin cambiar la entrada efectiva de la MLP | `data.py`, `model.py` y prueba de salida `(None, 10)` |
| One-hot encoding con Softmax y categorical crossentropy para E0 | Etiquetas sparse con sparse categorical crossentropy | Es coherente con la hipótesis E0 definida y permite comprobar explícitamente la forma de las etiquetas | `one_hot_encode`, `baseline.json` |

## Experimentos

| ID | Configuración | Objetivo | Resultado | Evidencia |
|---|---|---|---|---|
| D0 | Carga Keras + split estratificado 90/10, seed 42 | Validar contrato y preprocesamiento | Correcto: 54.000/6.000, 5.400/600 por clase, `float32 [0,1]` | ejecución de `prepare_fashion_mnist()` y tests |

## Reproducción y verificaciones

```powershell
uv sync --frozen
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Para cargar y validar el dataset real, ejecutar `prepare_fashion_mnist()` desde `ep1_fashion_mnist.data`. La descarga queda en la caché local de Keras; los datos no se versionan.

## Desviaciones respecto del plan

Pendiente.

## Limitaciones y resultados negativos

Pendiente.

## Asuntos abiertos

- Crear el notebook de Ignacio con EDA y narrativa reproducible.
- Entrenar E0 y registrar curvas y métricas de validation. El test sigue sin evaluación.
- Confirmar el manifiesto en Colab durante la validación final del proyecto.

## Resumen para el handoff a Lucas

Pendiente.
