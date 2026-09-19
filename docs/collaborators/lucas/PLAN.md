# Plan de trabajo — Lucas Moncada

**Handoff:** 02 — hiperparámetros e infraestructura experimental

**Estado:** COMPLETADO — PENDIENTE DE REVISIÓN

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

**Estado:** COMPLETADA

### Comparación inicial

- `0.001`
- `0.01` — control E0
- `0.1`

### Criterio de decisión

Seleccionar el valor que entregue el mejor equilibrio entre métricas de validation, estabilidad, velocidad de convergencia y gap. Si una corrida diverge, se conserva como resultado negativo. No se ampliará el rango sin evidencia documentada.

### Evidencia y decisión

- `0.001`: accuracy `0,8053`, F1 Macro `0,8034`; continuó mejorando, pero quedó subentrenado con 20 épocas.
- `0.01`: accuracy `0,8722`, F1 Macro `0,8726`; reprodujo exactamente el control.
- `0.1`: accuracy `0,8933`, F1 Macro `0,8936`; mejor resultado con duración comparable.
- Se selecciona `0.1` para E4. La mejora sobre `0.01` fue de 2,12 puntos porcentuales de accuracy y no se considera marginal.
- Se conserva como riesgo un gap final de accuracy de `0,0298` y el mínimo de `val_loss` en la época 18; esta evidencia se retomará al evaluar capacidad y Early Stopping.

## Etapa 3 — E4: batch size

**Estado:** COMPLETADA

### Comparación inicial

- `32`
- `128` — control original
- `512`

Se utilizará el learning rate seleccionado en E3 y se mantendrán fijas las demás variables.

### Criterio de decisión

Comparar métricas, estabilidad, tiempo total, tiempo por época y costo computacional. Una mejora marginal no justifica automáticamente un batch más costoso.

### Evidencia y decisión

- `32`: accuracy `0,8860`, F1 Macro `0,8864` y 57,46 segundos; presentó el mayor gap y deterioro de `val_loss` después de la época 9.
- `128`: accuracy `0,8933`, F1 Macro `0,8936` y 20,98 segundos; obtuvo el mejor desempeño con costo intermedio.
- `512`: accuracy `0,8745`, F1 Macro `0,8771` y 10,01 segundos; fue el más rápido y con menor gap, pero perdió 1,88 puntos porcentuales de accuracy frente a 128.
- Se mantiene `batch_size=128` para E5 por su mejor equilibrio entre desempeño, generalización y costo.
- `512` queda documentado como alternativa de eficiencia, mientras que `32` se descarta por mayor costo y sobreajuste.

## Etapa 4 — E5: capacidad

**Estado:** COMPLETADA

### Comparación inicial

- `[64]`
- `[256, 128]` — control original
- `[512, 256, 128]`

Se utilizarán el learning rate y batch seleccionados en las etapas anteriores.

### Criterio de decisión

Comparar capacidad de ajuste, métricas de validation, gap, cantidad de parámetros y duración. Una red mayor solo será candidata si su mejora compensa su complejidad y no introduce sobreajuste relevante.

### Evidencia y decisión

- `[64]`: 50.890 parámetros, accuracy `0,8873`, F1 Macro `0,8881` y 12,09 segundos; fue eficiente, pero perdió desempeño frente al control.
- `[256, 128]`: 235.146 parámetros, accuracy `0,8933`, F1 Macro `0,8936` y 19,52 segundos; mantiene el mejor equilibrio.
- `[512, 256, 128]`: 567.434 parámetros, accuracy `0,8990`, F1 Macro `0,8989` y 31,32 segundos; mejoró solo 0,57 puntos de accuracy frente al control, con 2,41 veces más parámetros y mayores gaps.
- Se selecciona `[256, 128]` como candidata para Cesar. La red grande queda como alternativa si se prioriza desempeño absoluto sobre eficiencia y generalización.

## Etapa 5 — Evaluación de Early Stopping

**Estado:** COMPLETADA SIN ACTIVAR EXPERIMENTO ADICIONAL

Early Stopping se incorporará únicamente después de interpretar las curvas sin callback. Si corresponde, se comparará la configuración candidata con y sin la técnica, documentando `monitor`, `patience`, `min_delta`, máximo de épocas y restauración de pesos.

Esta evaluación es preliminar respecto de E10: Cesar podrá repetirla después de estudiar optimizadores y regularización si esas decisiones cambian sustancialmente la dinámica de entrenamiento.

### Decisión condicional

No se ejecuta una comparación adicional con callback. En la candidata `[256, 128]`, la menor `val_loss` aparece en la época 18 (`0,3009`) y la final es `0,3015`; la diferencia es aproximadamente `0,0006` y no existe deterioro material de accuracy. El ahorro potencial sería de dos épocas dentro de un presupuesto corto. Cesar deberá reevaluar Early Stopping si sus cambios generan deterioro sostenido o desplazan la mejor época de forma relevante.

## Etapa 6 — Consolidación y handoff

**Estado:** COMPLETADA — PENDIENTE DE REVISIÓN

### Entregables

- `notebooks/02_lucas_hyperparameters.ipynb` ejecutado y curado.
- Configuraciones E3, E4 y E5 identificables.
- Tabla comparativa trazable y figuras seleccionadas.
- `docs/collaborators/lucas/REPORT.md` completo.
- Decisiones metodológicas actualizadas en `docs/DECISION_LOG.md`.
- Checklist de rúbrica actualizado.
- `docs/handoffs/RUN_HANDOFF_03_CESAR.md` completado con la configuración candidata, evidencia, límites y comandos de reproducción.

### Evidencia de cierre

- `notebooks/02_lucas_hyperparameters.ipynb` ejecutado de principio a fin desde `.venv`: 6/6 celdas de código con contador y cero errores.
- Las nueve corridas E3–E5 reprodujeron sus métricas, 20 épocas y cantidades de parámetros.
- Informe individual y decisiones D-014–D-018 actualizados.
- Handoff 02 listo para revisión y Handoff 03 preparado, condicionado a la aceptación e integración de esta rama.
- 22 pruebas correctas, Ruff 0.16.8 bloqueado, workflow de calidad preparado y lock verificado.

## Verificación general

```powershell
uv lock --check
uv sync --frozen
$env:PYTHONPATH = "src"
uv run python -m unittest discover -s tests -v
uv run ruff check src tests
```

Cada etapa añadirá sus comandos de reproducción y resultados observados al informe de Lucas. La evaluación sobre test continuará prohibida hasta la etapa final definida para Cesar e integración.
