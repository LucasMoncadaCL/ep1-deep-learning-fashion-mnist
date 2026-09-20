# EP1 Deep Learning - Fashion-MNIST

Proyecto colaborativo para estudiar cómo la arquitectura, las funciones, los hiperparámetros, los optimizadores y la regularización afectan a una MLP aplicada a Fashion-MNIST.

## Estado

Las etapas de Ignacio y Lucas están integradas. Cesar completó las comparaciones E6–E9, congeló la configuración F0 exclusivamente con train/validation y ejecutó la evaluación F1 una sola vez sobre test. La configuración final, sus métricas y limitaciones están resumidas en [`results/tables/FINAL_MODEL_SELECTION.md`](results/tables/FINAL_MODEL_SELECTION.md); no se permiten ajustes posteriores a F1.

Los puntos de entrada para revisar el cierre son [`docs/collaborators/cesar/REPORT.md`](docs/collaborators/cesar/REPORT.md), [`results/tables/FINAL_MODEL_SELECTION.md`](results/tables/FINAL_MODEL_SELECTION.md) y [`docs/DECISION_LOG.md`](docs/DECISION_LOG.md).

El plan ejecutado de Cesar está en [`docs/collaborators/cesar/PLAN.md`](docs/collaborators/cesar/PLAN.md). El archivo `notebooks/EP1_FashionMNIST_FINAL.ipynb` es autónomo para Colab: integra las tres etapas y no depende de archivos del repositorio. Solo restan la revisión humana de cierre, el commit y su ejecución limpia en Colab.

## Principios

- justificar técnicamente cada decisión;
- separar hipótesis previas de conclusiones posteriores;
- modificar una variable por experimento controlado;
- reservar test hasta congelar la configuración;
- mantener código reutilizable fuera de los notebooks;
- respaldar resultados con configuraciones, métricas y visualizaciones;
- exigir documentación y handoff verificable por colaborador;
- trabajar exclusivamente con `.venv` creado mediante `uv venv`;
- ejecutar el notebook final desde cero en Google Colab.

## Flujo de colaboradores

```text
Ignacio Silva
    -> datos, EDA, preprocesamiento y baseline
    -> handoff validado

Lucas Moncada
    -> infraestructura experimental e hiperparámetros
    -> handoff validado

Cesar Rojas
    -> optimización, regularización y evaluación final
    -> integración y cierre
```

Todos los handoffs establecen **metas mínimas y orientativas, ampliables con justificación técnica**; no constituyen una lista exhaustiva ni inmutable. Pueden incorporarse o reajustarse pasos cuando aparezca nueva evidencia, siempre que el cambio quede documentado y respete el alcance de la guía maestra.

El procedimiento completo está en [`docs/COLLABORATION_WORKFLOW.md`](docs/COLLABORATION_WORKFLOW.md). El trabajo inicial de Ignacio se define en [`docs/handoffs/RUN_HANDOFF_01_IGNACIO.md`](docs/handoffs/RUN_HANDOFF_01_IGNACIO.md).

## Estructura

```text
configs/                     configuraciones reproducibles
data/                        instrucciones; datos locales ignorados por Git
docs/                        metodología, decisiones, auditoría y colaboración
notebooks/                   análisis curados y notebook final
src/ep1_fashion_mnist/       código reutilizable del proyecto
tests/                       validaciones de datos, código y protocolo
results/figures/             figuras seleccionadas para el informe
results/tables/              tablas seleccionadas para el informe
```

Los materiales docentes y la rúbrica binaria permanecen disponibles localmente en `docs/material-ea1/` y `docs/ref/`, pero no se versionan.

## Documentos principales

- [`docs/GUIA_MAESTRA_EP1_FashionMNIST.md`](docs/GUIA_MAESTRA_EP1_FashionMNIST.md)
- [`docs/AUDITORIA_RUBRICA_EP1.md`](docs/AUDITORIA_RUBRICA_EP1.md)
- [`docs/DATA_CONTRACT.md`](docs/DATA_CONTRACT.md)
- [`docs/ENVIRONMENT.md`](docs/ENVIRONMENT.md)
- [`docs/RUBRICA_CHECKLIST.md`](docs/RUBRICA_CHECKLIST.md)
- [`docs/DECISION_LOG.md`](docs/DECISION_LOG.md)
- [`docs/COLLABORATION_WORKFLOW.md`](docs/COLLABORATION_WORKFLOW.md)
- [`docs/reviews/REVIEW_02_LUCAS.md`](docs/reviews/REVIEW_02_LUCAS.md)
- [`docs/latex/collaborators/lucas/main.tex`](docs/latex/collaborators/lucas/main.tex)

## Entorno obligatorio

Cada colaborador debe usar **Python 3.12.x** dentro de un `.venv` en la raíz del repositorio, creado exclusivamente con:

```powershell
uv venv --python 3.12 .venv
```

No se permite desarrollar con Python global, `python -m venv`, Conda, Poetry ni instalaciones directas con `pip`.

La rama menor queda fijada en `.python-version`; `uv` resuelve el parche estable disponible. Las dependencias declaradas en `pyproject.toml` ya están resueltas con versiones exactas en `uv.lock`; reconstruirlas con `uv sync --frozen`. El procedimiento y la justificación completa están en [`docs/ENVIRONMENT.md`](docs/ENVIRONMENT.md).
