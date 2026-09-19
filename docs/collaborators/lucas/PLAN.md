# Plan de trabajo — Lucas Moncada

**Handoff:** 02 — hiperparámetros e infraestructura experimental

**Estado:** EN EJECUCIÓN

**Rama:** `feature/lucas-hyperparameters`

**Control inicial:** E0 aceptado en el Handoff 01

## Objetivo

Construir una secuencia reproducible de experimentos controlados para estudiar learning rate, batch size y capacidad de la MLP, y evaluar Early Stopping solo cuando las curvas previas lo justifiquen. La salida será una configuración candidata técnicamente defendible para Cesar, no un modelo final.

Este documento es un plan vivo: puede ampliarse o ajustarse cuando aparezca evidencia nueva, siempre que el cambio, su motivo y su impacto queden documentados.

## Reglas invariantes

- Trabajar exclusivamente con el `.venv` administrado mediante `uv`.
- Mantener el conjunto oficial de test sellado durante toda esta etapa.
- Usar únicamente train y validation para comparar configuraciones.
- Modificar una sola variable dentro de cada familia experimental.
- Conservar un control explícito y una configuración JSON por ejecución.
- Reportar Accuracy, Precision, Recall y F1 Macro; mantener también las métricas ponderadas.
- Comparar además convergencia, gap train-validation, épocas, parámetros y duración.
- Versionar código, configuraciones, documentación y evidencia seleccionada; mantener las corridas regenerables en `results/runs/` fuera de Git.
- Escribir títulos y cuerpos de commit en español.

## Estrategia de selección

La búsqueda será secuencial y controlada, no una grilla combinatoria:

```text
E0 aceptado
  → E3 selecciona learning rate
    → E4 selecciona batch size
      → E5 selecciona capacidad
        → Early Stopping se evalúa solo si la evidencia lo justifica
          → configuración candidata para Cesar
```

Dentro de cada etapa se mantiene fija la configuración candidata recibida y se cambia únicamente la variable estudiada. Una etapa no se cierra solo por obtener mayor accuracy: también se consideran F1 Macro, estabilidad, costo, complejidad y diferencia entre train y validation.

## Etapa 1 — Contrato e infraestructura experimental

**Estado:** COMPLETADA

### Resultado esperado

El ejecutor debe producir resultados autocontenidos y comparables antes de iniciar E3.

### Trabajo

- Validar de forma explícita los campos numéricos y estructurales de cada configuración.
- Registrar en el JSON de salida la configuración efectiva completa.
- Registrar duración de entrenamiento, épocas completadas y cantidad de parámetros.
- Registrar mejor época según `val_loss`, mejores valores de validation y valores finales de train/validation.
- Calcular gaps finales de accuracy y loss sin consultar test.
- Mantener compatibilidad con las configuraciones E0, E1 y E2.
- Proteger el contrato mediante pruebas unitarias.

### Criterio de salida

- El esquema nuevo está probado con datos sintéticos o historiales pequeños.
- Las 14 pruebas recibidas continúan pasando junto con las pruebas nuevas.
- Ruff no presenta observaciones.
- E0 puede ejecutarse con el contrato ampliado sin cambiar su configuración.

### Evidencia de cierre

- 18 pruebas unitarias correctas.
- Ruff sin observaciones.
- `uv lock --check` correcto.
- E0 reproducido sin modificar `configs/baseline.json`: accuracy `0,8722` y F1 Macro `0,8726`.
- El registro de integración guardó la configuración completa, 235.146 parámetros, 20 épocas, mejores épocas, valores finales, gaps y 23,82 segundos de entrenamiento local por CPU.
- `final_accuracy_gap` se define como `train_accuracy - val_accuracy`; `final_loss_gap`, como `val_loss - train_loss`.

## Etapa 2 — E3: learning rate

**Estado:** LISTA PARA INICIAR

### Comparación inicial

- `0.001`
- `0.01` — control E0
- `0.1`

### Criterio de decisión

Seleccionar el valor que entregue el mejor equilibrio entre métricas de validation, estabilidad, velocidad de convergencia y gap. Si una corrida diverge, se conserva como resultado negativo. No se ampliará el rango sin evidencia documentada.

## Etapa 3 — E4: batch size

**Estado:** PENDIENTE

### Comparación inicial

- `32`
- `128` — control original
- `512`

Se utilizará el learning rate seleccionado en E3 y se mantendrán fijas las demás variables.

### Criterio de decisión

Comparar métricas, estabilidad, tiempo total, tiempo por época y costo computacional. Una mejora marginal no justifica automáticamente un batch más costoso.

## Etapa 4 — E5: capacidad

**Estado:** PENDIENTE

### Comparación inicial

- `[64]`
- `[256, 128]` — control original
- `[512, 256, 128]`

Se utilizarán el learning rate y batch seleccionados en las etapas anteriores.

### Criterio de decisión

Comparar capacidad de ajuste, métricas de validation, gap, cantidad de parámetros y duración. Una red mayor solo será candidata si su mejora compensa su complejidad y no introduce sobreajuste relevante.

## Etapa 5 — Evaluación de Early Stopping

**Estado:** PENDIENTE Y CONDICIONAL

Early Stopping se incorporará únicamente después de interpretar las curvas sin callback. Si corresponde, se comparará la configuración candidata con y sin la técnica, documentando `monitor`, `patience`, `min_delta`, máximo de épocas y restauración de pesos.

Esta evaluación es preliminar respecto de E10: Cesar podrá repetirla después de estudiar optimizadores y regularización si esas decisiones cambian sustancialmente la dinámica de entrenamiento.

## Etapa 6 — Consolidación y handoff

**Estado:** PENDIENTE

### Entregables

- `notebooks/02_lucas_hyperparameters.ipynb` ejecutado y curado.
- Configuraciones E3, E4 y E5 identificables.
- Tabla comparativa trazable y figuras seleccionadas.
- `docs/collaborators/lucas/REPORT.md` completo.
- Decisiones metodológicas actualizadas en `docs/DECISION_LOG.md`.
- Checklist de rúbrica actualizado.
- `docs/handoffs/RUN_HANDOFF_03_CESAR.md` completado con la configuración candidata, evidencia, límites y comandos de reproducción.

## Verificación general

```powershell
uv lock --check
uv sync --frozen
$env:PYTHONPATH = "src"
uv run python -m unittest discover -s tests -v
uvx ruff check src tests
```

Cada etapa añadirá sus comandos de reproducción y resultados observados al informe de Lucas. La evaluación sobre test continuará prohibida hasta la etapa final definida para Cesar e integración.
