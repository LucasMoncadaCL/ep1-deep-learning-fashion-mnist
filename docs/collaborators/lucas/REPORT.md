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
- Se ejecutó E3 comparando `learning_rate` 0,001, 0,01 y 0,1 con una sola variable modificada.
- Se seleccionó 0,1 como control para E4 y se documentó el mayor gap train-validation observado.
- Se ejecutó E4 comparando batch size 32, 128 y 512 con `learning_rate=0.1` y las demás variables controladas.
- Se mantuvo batch 128 como control para E5 por su mejor equilibrio entre métricas, costo y generalización.

## Archivos creados o modificados

- `docs/collaborators/lucas/PLAN.md`.
- `docs/collaborators/lucas/REPORT.md`.
- `docs/handoffs/RUN_HANDOFF_02_LUCAS.md`.
- `src/ep1_fashion_mnist/experiment.py`.
- `tests/test_data_validation.py` y `tests/README.md`.
- `docs/ENVIRONMENT.md`.
- `configs/E3_lr_0_001.json`, `configs/E3_lr_0_01.json` y `configs/E3_lr_0_1.json`.
- `results/tables/E3_learning_rate_comparison.md`.
- `results/figures/E3_learning_rate_validation_accuracy.png` y `results/figures/E3_learning_rate_validation_loss.png`.
- `configs/E4_batch_32.json`, `configs/E4_batch_128.json` y `configs/E4_batch_512.json`.
- `results/tables/E4_batch_size_comparison.md`.
- `results/figures/E4_batch_size_validation_accuracy.png` y `results/figures/E4_batch_size_validation_loss.png`.
- `docs/DECISION_LOG.md` y `docs/RUBRICA_CHECKLIST.md`.

## Evidencia del entorno uv

- `uv --version`: `uv 0.11.8`.
- `python --version` dentro de `.venv`: `Python 3.12.13`.
- `sys.executable`: `C:\Users\lucas\Documents\Deep-Learning-ev1\.venv\Scripts\python.exe`.
- comando de sincronización: `uv sync --frozen`.
- resultado de pruebas dentro de `.venv`: 20/20 correctas.

## Decisiones técnicas

| Decisión | Alternativas | Justificación | Evidencia |
|---|---|---|---|
| Búsqueda secuencial controlada | Grilla combinatoria | Permite atribuir cada efecto a una variable y limita costo computacional | `PLAN.md` y Handoff 02 |
| Registro autocontenido por corrida | Depender solo de nombres de carpetas y archivos separados | Evita perder la configuración exacta que produjo cada métrica | Pruebas y JSON local de E0 |
| Gaps con signo explícito | Diferencias absolutas | Conservan la dirección de la diferencia y facilitan interpretar sobreajuste o validation superior | `TrainingSummary` y `PLAN.md` |
| Seleccionar learning rate 0,1 para E4 | 0,001 y 0,01 | Mejoró accuracy y F1 Macro en aproximadamente 2,1 puntos frente al control, con duración similar | Tabla y figuras E3; D-014 |
| Mantener batch size 128 para E5 | 32 y 512 | Entregó la mejor accuracy y F1 Macro, con menor costo y gaps que 32; 512 fue más rápido, pero perdió desempeño relevante | Tabla y figuras E4; D-015 |

## Experimentos

| ID | Configuración | Objetivo | Resultado | Evidencia |
|---|---|---|---|---|
| E0 — verificación de infraestructura | Configuración aceptada sin cambios | Comprobar compatibilidad y nuevo contrato de resultados | Accuracy 0,8722; F1 Macro 0,8726; 20 épocas; 23,82 s por CPU | `results/runs/stage1_e0_contract/` local e ignorado |
| E3_lr_0_001 | LR 0,001; resto igual a E0 | Medir convergencia lenta | Accuracy 0,8053; F1 Macro 0,8034; mejor época 20 | Configuración y tabla E3 |
| E3_lr_0_01 | LR 0,01; resto igual a E0 | Reproducir el control dentro de E3 | Accuracy 0,8722; F1 Macro 0,8726; mejor época 20 | Configuración y tabla E3 |
| E3_lr_0_1 | LR 0,1; resto igual a E0 | Evaluar convergencia más rápida | Accuracy 0,8933; F1 Macro 0,8936; mejor val. accuracy en época 13 | Configuración, tabla y figuras E3 |
| E4_batch_32 | Batch 32; LR 0,1; resto controlado | Evaluar actualizaciones más frecuentes | Accuracy 0,8860; F1 Macro 0,8864; 57,46 s; gap de loss 0,2022 | Configuración, tabla y figuras E4 |
| E4_batch_128 | Batch 128; LR 0,1; resto controlado | Revalidar el batch del control con el LR seleccionado | Accuracy 0,8933; F1 Macro 0,8936; 20,98 s | Configuración, tabla y figuras E4 |
| E4_batch_512 | Batch 512; LR 0,1; resto controlado | Evaluar eficiencia con actualizaciones menos frecuentes | Accuracy 0,8745; F1 Macro 0,8771; 10,01 s; menor gap | Configuración, tabla y figuras E4 |

## Reproducción y verificaciones

```powershell
uv lock --check
uv sync --frozen
$env:PYTHONPATH = "src"
uv run python -m unittest discover -s tests -v
uvx ruff check src tests
uv run python -m ep1_fashion_mnist.experiment configs\baseline.json --output results\runs\stage1_e0_contract
uv run python -m ep1_fashion_mnist.experiment configs\E3_lr_0_001.json --output results\runs\E3_lr_0_001
uv run python -m ep1_fashion_mnist.experiment configs\E3_lr_0_01.json --output results\runs\E3_lr_0_01
uv run python -m ep1_fashion_mnist.experiment configs\E3_lr_0_1.json --output results\runs\E3_lr_0_1
uv run python -m ep1_fashion_mnist.experiment configs\E4_batch_32.json --output results\runs\E4_batch_32
uv run python -m ep1_fashion_mnist.experiment configs\E4_batch_128.json --output results\runs\E4_batch_128
uv run python -m ep1_fashion_mnist.experiment configs\E4_batch_512.json --output results\runs\E4_batch_512
```

## Desviaciones respecto del plan

No hubo desviaciones materiales en la etapa 1.

## Limitaciones y resultados negativos

- La duración se midió en CPU local y sirve para comparaciones realizadas en el mismo entorno; no debe compararse directamente con GPU o Colab.
- La validación mejoró ligeramente respecto de train al final de E0, por lo que los gaps con signo fueron negativos; esto no constituye evidencia de sobreajuste.
- `learning_rate=0.001` quedó subentrenado con 20 épocas. Aumentar solo sus épocas rompería el presupuesto común de E3, por lo que se conserva como resultado negativo.
- `learning_rate=0.1` presentó gap final de accuracy de 0,0298 y gap de loss de 0,0885; debe vigilarse en E4/E5 y retomarse al evaluar Early Stopping.
- E3 utiliza una seed. La diferencia principal no fue marginal; las repeticiones se reservarán para decisiones finales o comparaciones estrechas.
- El batch 32 presentó deterioro de validation después de sus mejores épocas y fue aproximadamente 2,74 veces más lento que 128; se conserva como resultado negativo.
- El batch 512 redujo a la mitad el tiempo respecto de 128 y mostró menor gap, pero perdió 1,88 puntos porcentuales de accuracy; se conserva como alternativa de eficiencia.
- E4 utiliza una seed. La selección se apoya en desempeño, costo y generalización conjuntamente; las repeticiones se reservarán para una decisión final estrecha.

## Asuntos abiertos

- Crear las configuraciones E5 para capacidades `[64]`, `[256, 128]` y `[512, 256, 128]`, usando learning rate 0,1 y batch 128.
- Comparar métricas, cantidad de parámetros, duración y gaps antes de decidir si existe evidencia suficiente para evaluar Early Stopping.

## Resumen para el handoff a Cesar

Pendiente.
