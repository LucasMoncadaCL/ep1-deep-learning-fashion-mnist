# EP1 Deep Learning - Fashion-MNIST

Proyecto colaborativo para estudiar cómo la arquitectura, las funciones, los hiperparámetros, los optimizadores y la regularización afectan a una MLP aplicada a Fashion-MNIST.

## Estado

La etapa inicial de Ignacio fue aceptada e integrada. La etapa de Lucas completó la infraestructura experimental y las comparaciones E3–E5; permanece `READY_FOR_REVIEW` antes de integrarse y habilitar el trabajo de Cesar. Todos los ajustes se ejecutaron exclusivamente sobre train/validation y el conjunto oficial de test continúa sellado.

Los puntos de entrada actuales son [`docs/handoffs/RUN_HANDOFF_02_LUCAS.md`](docs/handoffs/RUN_HANDOFF_02_LUCAS.md) para revisar la entrega de Lucas y [`docs/handoffs/RUN_HANDOFF_03_CESAR.md`](docs/handoffs/RUN_HANDOFF_03_CESAR.md) para preparar la etapa siguiente una vez aceptada la integración.

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

## Entorno obligatorio

Cada colaborador debe usar **Python 3.12.x** dentro de un `.venv` en la raíz del repositorio, creado exclusivamente con:

```powershell
uv venv --python 3.12 .venv
```

No se permite desarrollar con Python global, `python -m venv`, Conda, Poetry ni instalaciones directas con `pip`.

La rama menor queda fijada en `.python-version`; `uv` resuelve el parche estable disponible. Las dependencias declaradas en `pyproject.toml` ya están resueltas con versiones exactas en `uv.lock`; reconstruirlas con `uv sync --frozen`. El procedimiento y la justificación completa están en [`docs/ENVIRONMENT.md`](docs/ENVIRONMENT.md).
