# Informe de colaborador - Cesar Rojas

**Estado:** READY_FOR_REVIEW — E6–F1, la integración documental y la validación limpia en Colab están completos; queda la revisión humana de cierre.

**Plan de referencia:** `docs/collaborators/cesar/PLAN.md`

## Metas orientativas

- comparar optimizadores con un control explícito;
- evaluar Dropout, Batch Normalization y regularización pertinente;
- consolidar métricas, matriz de confusión y análisis de errores;
- participar en la selección congelada del modelo;
- ejecutar evaluación final sin retroalimentar ajustes desde test.

## Trabajo realizado

- Se preparó `.venv` mediante `uv sync --frozen`, se registró el kernel `EP1 Fashion-MNIST (.venv)` y se descargó Fashion-MNIST mediante la API de Keras.
- Se verificó el contrato efectivo: train `(54000, 28, 28)`, validation `(6000, 28, 28)`, imágenes `float32` en `[0, 1]`, etiquetas one-hot y distribución estratificada de 5.400/600 ejemplos por clase.
- Se reprodujo el control `E5_capacity_256_128` sin consultar test: Accuracy de validation `0,8952` y F1 Macro `0,8954`.
- Se implementó E6 con tres configuraciones que modifican únicamente el optimizador y se añadió una prueba automática para ese invariante.
- Se ejecutó la comparación inicial E6 exclusivamente sobre validation y se guardaron tabla y curvas seleccionadas.
- Se ejecutó E6b con Adam y RMSProp fijos, cambiando únicamente `learning_rate` de `0,1` a `0,001`; SGD conserva el mejor compromiso y queda como control provisional para E7.
- Se ejecutó E7 con y sin Dropout; Dropout `0,2` mejoró Accuracy/F1 Macro y redujo los gaps, por lo que queda como control para E8.
- Se corrigió y probó el orden Batch Normalization→ReLU. E8 mostró que activar Batch Normalization empeora las métricas y gaps bajo este control, por lo que queda desactivada para E9.
- Se ejecutó E9 con L2 `0` y `1e-4`; L2 no superó el control ya regularizado con Dropout, por lo que queda en cero.
- Las corridas canónicas L2 con seeds 42 y 7 favorecieron la configuración sin L2. Una revisión externa observó una diferencia marginal e inversión, por lo que L2 cero se reporta como opción prudente y no como ventaja robusta entre entornos. Se descartó Early Stopping por falta de oportunidad material y se congeló F0 antes de test.
- F1 se ejecutó una única vez mediante el evaluador separado: Accuracy de test 0,8838 y F1 Macro 0,8836. El resultado decisorio quedó versionado junto al hash de F0 y sus versiones; el notebook de Colab lo presenta sin volver a consultar test.

## Archivos creados o modificados

- `configs/E6_optimizer_sgd.json`.
- `configs/E6_optimizer_rmsprop.json`.
- `configs/E6_optimizer_adam.json`.
- `configs/E6b_adam_lr_0_001.json`.
- `configs/E6b_rmsprop_lr_0_001.json`.
- `configs/E7_dropout_0.json`.
- `configs/E7_dropout_0_2.json`.
- `configs/E8_batch_norm_off.json`.
- `configs/E8_batch_norm_on.json`.
- `configs/E9_l2_0.json`.
- `configs/E9_l2_1e-4.json`.
- `configs/R_e9_l2_0_seed_7.json`.
- `configs/R_e9_l2_1e-4_seed_7.json`.
- `configs/F0_frozen_config.json`.
- `tests/test_data_validation.py`.
- `results/tables/E6_optimizer_initial_comparison.md`.
- `results/tables/E6b_retuned_optimizer_comparison.md`.
- `results/tables/E7_dropout_comparison.md`.
- `results/tables/E8_batch_norm_comparison.md`.
- `results/tables/E9_l2_comparison.md`.
- `results/tables/F0_frozen_protocol.md`.
- `results/tables/F1_final_test_summary.md`.
- `results/figures/E6_optimizer_validation_accuracy.png`.
- `results/figures/E6_optimizer_validation_loss.png`.
- `results/figures/E6b_retuned_optimizer_validation_accuracy.png`.
- `results/figures/E6b_retuned_optimizer_validation_loss.png`.
- `results/figures/E7_dropout_validation_accuracy.png`.
- `results/figures/E7_dropout_validation_loss.png`.
- `results/figures/E8_batch_norm_validation_accuracy.png`.
- `results/figures/E8_batch_norm_validation_loss.png`.
- `results/figures/E9_l2_validation_accuracy.png`.
- `results/figures/E9_l2_validation_loss.png`.
- `notebooks/03_cesar_optimization_evaluation.ipynb`.

## Evidencia del entorno uv

- `uv --version`: `uv 0.11.8`.
- `python --version` dentro de `.venv`: `Python 3.12.13`.
- `sys.executable`: `C:\\Users\\cesar\\OneDrive\\Desktop\\DuocUC\\3erYear\\deepLearning\\ep1-deep-learning-fashion-mnist\\.venv\\Scripts\\python.exe`.
- comando de sincronización: `uv sync --frozen`.
- resultado de pruebas dentro de `.venv`: 31/31 correctas después de integrar F1 y su guardia de evaluación única.

## Decisiones técnicas

| Decisión | Alternativas | Justificación | Evidencia |
|---|---|---|---|
| Comparar optimizadores primero con LR común | SGD, RMSProp y Adam con LR ajustado desde el inicio | Aísla el efecto del optimizador antes de atribuir cambios al learning rate | `results/tables/E6_optimizer_initial_comparison.md` |

## Experimentos

| ID | Configuración | Objetivo | Resultado | Evidencia |
|---|---|---|---|---|
| C0_control_recibido | `E5_capacity_256_128` sin cambios | Reproducir el punto de partida | Accuracy 0,8952; F1 Macro 0,8954 | `results/runs/cesar_control_recibido/` local e ignorado |
| E6_optimizer_sgd | Solo optimizador: SGD | Control común de E6 | Accuracy 0,8952; F1 Macro 0,8954 | Configuración, tabla y curvas E6 |
| E6_optimizer_rmsprop | Solo optimizador: RMSProp | Comparar con LR común 0,1 | Accuracy 0,1985; F1 Macro 0,0684 | Configuración, tabla y curvas E6 |
| E6_optimizer_adam | Solo optimizador: Adam | Comparar con LR común 0,1 | Accuracy 0,4722; F1 Macro 0,4166 | Configuración, tabla y curvas E6 |
| E6b_adam_lr_0_001 | Adam fijo; LR 0,001 | Retunear LR sin mezclar optimizador | Accuracy 0,8912; F1 Macro 0,8916 | Configuración y tabla E6b |
| E6b_rmsprop_lr_0_001 | RMSProp fijo; LR 0,001 | Retunear LR sin mezclar optimizador | Accuracy 0,8933; F1 Macro 0,8929 | Configuración y tabla E6b |
| E7_dropout_0 | Sin Dropout | Control para aislar regularización | Accuracy 0,8952; F1 Macro 0,8954 | Configuración, tabla y curvas E7 |
| E7_dropout_0_2 | Solo Dropout 0,2 | Evaluar regularización estocástica | Accuracy 0,8997; F1 Macro 0,8997; gaps menores | Configuración, tabla y curvas E7 |
| E8_batch_norm_off | BatchNorm OFF | Control recibido de E7 | Accuracy 0,8997; F1 Macro 0,8997 | Configuración, tabla y curvas E8 |
| E8_batch_norm_on | Solo BatchNorm ON | Evaluar normalización de activaciones | Accuracy 0,8922; F1 Macro 0,8911; gaps mayores | Configuración, tabla y curvas E8 |
| E9_l2_0 | L2 0 | Control para aislar L2 | Accuracy 0,8997; F1 Macro 0,8997 | Configuración, tabla y curvas E9 |
| E9_l2_1e-4 | Solo L2 1e-4 | Evaluar penalización de pesos | Accuracy 0,8967; F1 Macro 0,8970 | Configuración, tabla y curvas E9 |
| R_e9_l2_*_seed_7 | Solo seed 7 | Repetir decisión L2 marginal | Sin L2: Accuracy 0,8902; con L2: 0,8863 | Configuraciones y registros locales |
| F0_frozen_config | Configuración seleccionada | Congelar antes de test | SGD, Dropout 0,2, sin BatchNorm/L2/ES | `F0_frozen_protocol.md` |
| F1_final_test | Configuración congelada | Evaluación única en test | Accuracy 0,8838; F1 Macro 0,8836 | Tabla F1 y figuras finales |

## Reproducción y verificaciones

```powershell
uv sync --frozen
$env:PYTHONPATH = "src"
uv run python -m unittest discover -s tests -v
uv run ruff check src tests
uv run python -m ep1_fashion_mnist.experiment configs\E5_capacity_256_128.json --output results\runs\cesar_control_recibido
uv run python -m ep1_fashion_mnist.experiment configs\E6_optimizer_sgd.json --output results\runs\E6_optimizer_sgd
uv run python -m ep1_fashion_mnist.experiment configs\E6_optimizer_rmsprop.json --output results\runs\E6_optimizer_rmsprop
uv run python -m ep1_fashion_mnist.experiment configs\E6_optimizer_adam.json --output results\runs\E6_optimizer_adam
uv run python -m ep1_fashion_mnist.experiment configs\E6b_adam_lr_0_001.json --output results\runs\E6b_adam_lr_0_001
uv run python -m ep1_fashion_mnist.experiment configs\E6b_rmsprop_lr_0_001.json --output results\runs\E6b_rmsprop_lr_0_001
uv run python -m ep1_fashion_mnist.experiment configs\E7_dropout_0.json --output results\runs\E7_dropout_0
uv run python -m ep1_fashion_mnist.experiment configs\E7_dropout_0_2.json --output results\runs\E7_dropout_0_2
uv run python -m ep1_fashion_mnist.experiment configs\E8_batch_norm_off.json --output results\runs\E8_batch_norm_off
uv run python -m ep1_fashion_mnist.experiment configs\E8_batch_norm_on.json --output results\runs\E8_batch_norm_on
uv run python -m ep1_fashion_mnist.experiment configs\E9_l2_0.json --output results\runs\E9_l2_0
uv run python -m ep1_fashion_mnist.experiment configs\E9_l2_1e-4.json --output results\runs\E9_l2_1e-4
uv run python -m ep1_fashion_mnist.experiment configs\R_e9_l2_0_seed_7.json --output results\runs\R_e9_l2_0_seed_7
uv run python -m ep1_fashion_mnist.experiment configs\R_e9_l2_1e-4_seed_7.json --output results\runs\R_e9_l2_1e-4_seed_7
```

## Desviaciones respecto del plan

No hay desviaciones metodológicas. La documentación aún debe registrar la aceptación humana del Handoff 02, aunque la base técnica ya está integrada en `main` y se usó como fuente explícita para esta etapa.

## Limitaciones y resultados negativos

- Con LR común `0,1`, RMSProp y Adam no convergieron a un desempeño comparable con SGD. Este resultado no permite compararlos en su régimen de LR apropiado.
- Se requiere E6b, separado de E6, para retunear learning rate por optimizador sin mezclar variables.
- RMSProp queda cerca de SGD en accuracy, pero sus gaps finales son mayores; la diferencia debe revisarse con seeds adicionales antes de F0 si continúa siendo determinante.
- E7 usa una sola seed. La mejora conjunta de métricas y reducción marcada de gaps respaldan continuar con Dropout 0,2, pero debe reevaluarse antes de F0 si otra técnica cambia el control.
- Batch Normalization no mejoró bajo el control recibido; se conserva como resultado negativo contextual, no como conclusión general sobre la técnica.
- L2 1e-4 redujo levemente el gap de loss, pero no mejoró Accuracy ni F1 Macro; la loss con L2 incluye penalización y no se compara como costo puro.
- Los tiempos de las repeticiones fueron afectados por carga local de CPU; no se usan como criterio de selección.
- Las duraciones se midieron por CPU en Windows nativo; no se deben extrapolar a GPU o Colab.

## Asuntos abiertos

- La ejecución limpia de `EP1_FashionMNIST_FINAL.ipynb` en Google Colab fue verificada después de publicar la rama; presentó la evidencia sin ejecutar F1 ni consultar test.
- Solicitar revisión humana de cierre sobre el notebook canónico, el contrato F1 y la documentación corregida.

## Resumen para la integración grupal

E6-F1 están completos e integrados en los notebooks de evidencia. La evaluación única de test obtuvo Accuracy `0,8838` y F1 Macro `0,8836`; Shirt fue la clase más difícil. No se hicieron ajustes posteriores. La ejecución limpia en Colab y los commits de corrección fueron completados; resta la revisión humana de cierre.
