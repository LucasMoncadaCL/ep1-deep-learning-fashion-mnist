# Informe de colaborador - Lucas Moncada

**Estado:** IN_PROGRESS

## Metas orientativas

- consolidar infraestructura común de experimentos;
- estudiar learning rate, batch size y capacidad;
- evaluar Early Stopping cuando corresponda;
- mantener una tabla comparativa trazable;
- entregar una configuración candidata y sus trade-offs.

## Trabajo realizado

- Se creó `feature/lucas-hyperparameters` desde el `main` que contiene el Handoff 01 aceptado.
- Se definió `docs/collaborators/lucas/PLAN.md` como plan experimental vivo y secuencial.
- Se auditó el ejecutor recibido y se identificó la necesidad de registrar configuración efectiva, duración, épocas, mejores valores, valores finales y gaps antes de comenzar E3.
- Se amplió la validación de configuraciones para rechazar tipos, rangos y estructuras inválidas antes de entrenar.
- Se incorporó un registro autocontenido por corrida con configuración, métricas, parámetros y resumen de entrenamiento.
- Se reprodujo E0 mediante el contrato ampliado sin modificar su configuración ni consultar test.

## Archivos creados o modificados

- `docs/collaborators/lucas/PLAN.md`.
- `docs/collaborators/lucas/REPORT.md`.
- `docs/handoffs/RUN_HANDOFF_02_LUCAS.md`.
- `src/ep1_fashion_mnist/experiment.py`.
- `tests/test_data_validation.py` y `tests/README.md`.
- `docs/ENVIRONMENT.md`.

## Evidencia del entorno uv

- `uv --version`: `uv 0.11.8`.
- `python --version` dentro de `.venv`: `Python 3.12.13`.
- `sys.executable`: `C:\Users\lucas\Documents\Deep-Learning-ev1\.venv\Scripts\python.exe`.
- comando de sincronización: `uv sync --frozen`.
- resultado de pruebas dentro de `.venv`: 18/18 correctas.

## Decisiones técnicas

| Decisión | Alternativas | Justificación | Evidencia |
|---|---|---|---|
| Búsqueda secuencial controlada | Grilla combinatoria | Permite atribuir cada efecto a una variable y limita costo computacional | `PLAN.md` y Handoff 02 |
| Registro autocontenido por corrida | Depender solo de nombres de carpetas y archivos separados | Evita perder la configuración exacta que produjo cada métrica | Pruebas y JSON local de E0 |
| Gaps con signo explícito | Diferencias absolutas | Conservan la dirección de la diferencia y facilitan interpretar sobreajuste o validation superior | `TrainingSummary` y `PLAN.md` |

## Experimentos

| ID | Configuración | Objetivo | Resultado | Evidencia |
|---|---|---|---|---|
| E0 — verificación de infraestructura | Configuración aceptada sin cambios | Comprobar compatibilidad y nuevo contrato de resultados | Accuracy 0,8722; F1 Macro 0,8726; 20 épocas; 23,82 s por CPU | `results/runs/stage1_e0_contract/` local e ignorado |

## Reproducción y verificaciones

```powershell
uv lock --check
uv sync --frozen
$env:PYTHONPATH = "src"
uv run python -m unittest discover -s tests -v
uvx ruff check src tests
uv run python -m ep1_fashion_mnist.experiment configs\baseline.json --output results\runs\stage1_e0_contract
```

## Desviaciones respecto del plan

No hubo desviaciones materiales en la etapa 1.

## Limitaciones y resultados negativos

- La duración se midió en CPU local y sirve para comparaciones realizadas en el mismo entorno; no debe compararse directamente con GPU o Colab.
- La validación mejoró ligeramente respecto de train al final de E0, por lo que los gaps con signo fueron negativos; esto no constituye evidencia de sobreajuste.
- Todavía no se ejecutaron nuevas configuraciones de hiperparámetros.

## Asuntos abiertos

- Crear las configuraciones controladas de E3 y ejecutar la comparación de learning rate.
- Definir evidencia seleccionada para versionar después de interpretar E3.

## Resumen para el handoff a Cesar

Pendiente.
