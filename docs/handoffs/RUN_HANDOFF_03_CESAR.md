# Run Handoff 03 - Cesar Rojas

**Estado:** WAITING_ON_HANDOFF_02_ACCEPTANCE

**Responsable:** Cesar Rojas

**Revisor de salida:** Lucas Moncada

**Destino:** integración grupal

## Condición de inicio

Este handoff contiene el contexto técnico necesario, pero Cesar no debe comenzar hasta que Ignacio complete la revisión cruzada, Lucas apruebe el alcance e integre la rama correspondiente. Al comenzar, la fuente de verdad será `main` actualizado, no una rama intermedia.

Las metas siguientes son **mínimas y orientativas, ampliables con justificación técnica**. No constituyen una lista exhaustiva ni inmutable. Cualquier ampliación debe respetar la guía maestra, mantener el test sellado durante el ajuste y quedar respaldada en el informe de Cesar.

El plan vivo de ejecución se encuentra en `docs/collaborators/cesar/PLAN.md`. El handoff define el contrato de entrada y salida; el plan organiza las etapas sin convertirlas en una receta rígida.

## Entrada técnica desde Lucas

- configuración candidata: `configs/E5_capacity_256_128.json`;
- arquitectura `[256, 128]`, ReLU, Softmax y categorical crossentropy;
- SGD con `learning_rate=0.1`, batch 128, 20 épocas y seed 42;
- sin Dropout, Batch Normalization, L2 ni Early Stopping;
- 235.146 parámetros;
- Accuracy `0,8933`, Precision Macro `0,8949`, Recall Macro `0,8933` y F1 Macro `0,8936` sobre validation;
- test oficial no evaluado.

La candidata es un control trazable, no una arquitectura definitiva. La alternativa `[512, 256, 128]` obtuvo accuracy `0,8990`, pero no fue seleccionada porque la mejora de 0,57 puntos implicó 2,41 veces más parámetros, 1,60 veces más tiempo en la corrida de referencia y mayores gaps. Los tiempos pueden variar entre ejecuciones y no deben usarse como único criterio.

## Infraestructura pública

- `ep1_fashion_mnist.data.prepare_fashion_mnist`: carga, valida y produce el split aceptado.
- `ep1_fashion_mnist.model.build_mlp`: construye la arquitectura configurable.
- `ep1_fashion_mnist.model.compile_model`: configura optimizador, learning rate y loss.
- `ep1_fashion_mnist.experiment.run_validation_experiment`: ejecuta una configuración y guarda historia, métricas y curva sin consultar test.
- `ep1_fashion_mnist.experiment.plot_validation_comparison`: genera curvas comparativas desde historiales.
- `ep1_fashion_mnist.visualization`: utilidades visuales aceptadas del bloque inicial.

Los registros locales bajo `results/runs/` son regenerables e ignorados. Las configuraciones, tablas y figuras seleccionadas sí están versionadas.

## Evidencia recibida

- `notebooks/02_lucas_hyperparameters.ipynb`.
- `results/tables/E3_learning_rate_comparison.md`.
- `results/tables/E4_batch_size_comparison.md`.
- `results/tables/E5_capacity_comparison.md`.
- `results/tables/E3_E5_validation_metrics.md`.
- decisiones D-014–D-018 en `docs/DECISION_LOG.md`.
- informe `docs/collaborators/lucas/REPORT.md`.

## Misión

Evaluar optimizadores y regularización, consolidar el análisis de métricas y errores, y preparar una propuesta final para decisión grupal. El test solo puede abrirse después de congelar configuración y protocolo.

Cesar debe sincronizar el entorno con `uv sync --frozen` y trabajar dentro del `.venv` del repositorio. Cualquier cambio de dependencia debe declararse en `pyproject.toml`, actualizar `uv.lock` y justificarse antes de producir resultados comparables.

## Orden experimental recomendado

1. Reproducir la candidata recibida y verificar sus métricas de validation.
2. Comparar SGD, RMSProp y Adam modificando solo el optimizador bajo un presupuesto común.
3. Si el optimizador seleccionado exige otro learning rate, realizar una etapa separada y explícita; no mezclar ambos efectos.
4. Evaluar Dropout, Batch Normalization y L2 mediante comparaciones controladas con/sin técnica.
5. Reevaluar Early Stopping solo después de observar las nuevas curvas. El ejecutor actualmente rechaza `early_stopping=true`; si se justifica la técnica, implementar y probar el callback documentando `monitor`, `patience`, `min_delta`, máximo de épocas y restauración de pesos.
6. Seleccionar y congelar configuración y protocolo mediante métricas de validation, costo, estabilidad y generalización.
7. Solo entonces ejecutar test una vez, calcular métricas finales, matriz de confusión y análisis visual de errores.

## Metas orientativas

- mantener un control explícito y cambiar una variable por comparación;
- comparar SGD, RMSProp y Adam;
- justificar cualquier retuning de learning rate;
- evaluar regularización y su efecto sobre gaps, estabilidad y convergencia;
- reportar Accuracy, Precision, Recall y F1 Macro, conservando también variantes ponderadas;
- producir matrices de confusión y análisis de errores por clase;
- registrar parámetros, épocas, duración y mejores épocas;
- documentar resultados negativos y alternativas descartadas;
- completar `docs/collaborators/cesar/REPORT.md` y su notebook ejecutado.

## Riesgos y restricciones

- No usar test para elegir optimizador, learning rate, regularización, épocas ni arquitectura.
- Las diferencias marginales con una seed requieren repetición antes de congelar el modelo.
- Adam y RMSProp pueden necesitar learning rates distintos; comparar y retunear deben ser etapas separadas.
- Batch Normalization, Dropout y L2 no deben activarse simultáneamente en la primera comparación.
- Early Stopping no fue descartado globalmente; quedó condicionado a nueva evidencia.
- `early_stopping=true` falla anticipadamente hasta que se implemente un callback real; no eliminar esta protección sin pruebas.
- Los tiempos locales de Lucas fueron medidos por CPU y no deben compararse directamente con GPU o Colab.

## Comandos iniciales

```powershell
uv sync --frozen
$env:PYTHONPATH = "src"
uv run python -m unittest discover -s tests -v
uv run ruff check src tests
uv run python -m ep1_fashion_mnist.experiment configs\E5_capacity_256_128.json --output results\runs\cesar_control_recibido
```

## Criterios de salida

- comparaciones de optimización y regularización interpretables y trazables;
- pruebas y experimentos ejecutados desde `.venv` administrado con `uv`;
- configuración final congelada antes de consultar test;
- test evaluado una sola vez según el protocolo acordado;
- matriz de confusión y errores por clase interpretados;
- tablas, figuras, notebook e informe reproducibles;
- decisiones, limitaciones y asuntos abiertos suficientes para que Lucas revise el cierre y el grupo prepare la defensa.
