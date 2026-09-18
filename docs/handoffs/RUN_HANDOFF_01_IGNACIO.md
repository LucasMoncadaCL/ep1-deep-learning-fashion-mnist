# Run Handoff 01 - Ignacio Silva

**Estado:** READY_FOR_REVIEW
**Responsable:** Ignacio Silva  
**Revisor de salida:** Cesar Rojas  
**Siguiente responsable:** Lucas Moncada

## Corrección posterior a revisión

La revisión de la entrega solicitó reforzar reproducibilidad, trazabilidad y el contrato de métricas. Se corrigieron los comandos para usar `uv run`, se documentó la reproducción de E0/E1/E2, se añadieron métricas macro junto a las ponderadas, se actualizaron las referencias documentales y se corrigieron observaciones de Ruff. El estado permanece `READY_FOR_REVIEW`: esta actualización no convierte el handoff en aceptado.

La política de commits en español queda como decisión de Lucas: debe acordar si reescribe los mensajes de esta rama con `--force-with-lease` o si la integración final a `main` se realizará por squash con un título y cuerpo completos en español. No se reescribió historial sin esa coordinación.

### Evidencia de la corrección

- Archivos de implementación: `src/ep1_fashion_mnist/experiment.py`, `src/ep1_fashion_mnist/data.py` y `tests/test_data_validation.py`.
- Documentación actualizada: índice de entrega, informe de Ignacio, informe LaTeX, entorno, README y handoff a Lucas.
- `ValidationMetrics` y los JSON de cada corrida ahora contienen Accuracy, Precision, Recall y F1 tanto `macro` como `weighted`. En E0--E2 coinciden porque validation tiene 600 ejemplos por clase.
- Reproducción confirmada: `uv sync --frozen`; 14 pruebas unitarias correctas; `uvx ruff check src tests` sin observaciones; notebook ejecutado mediante `uv run jupyter nbconvert --to notebook --execute --inplace notebooks\01_ignacio_data_baseline.ipynb --ExecutePreprocessor.timeout=120`.
- E0, E1_tanh, E1_sigmoid y E2_mse se regeneraron desde sus JSON versionados. Sus métricas se mantuvieron, respectivamente, en accuracy 0,8722; 0,8643; 0,7535; y 0,7370. Los artefactos regenerables quedaron bajo `tmp/revision_runs/` durante la verificación y no se versionan.

## 1. Misión

Construir una base reproducible y técnicamente defendible para todo el proyecto: contrato de datos, exploración, preprocesamiento y baseline. El objetivo no es encontrar todavía el mejor modelo, sino entregar una referencia confiable sobre la que Lucas pueda ejecutar comparaciones controladas.

## 2. Contexto que debe leer antes de comenzar

En este orden:

1. `README.md`;
2. `docs/GUIA_MAESTRA_EP1_FashionMNIST.md`;
3. `docs/DATA_CONTRACT.md`;
4. `docs/ENVIRONMENT.md`;
5. `docs/AUDITORIA_RUBRICA_EP1.md`;
6. `docs/RUBRICA_CHECKLIST.md`;
7. `docs/DECISION_LOG.md`;
8. `docs/COLLABORATION_WORKFLOW.md`;
9. `configs/baseline.json`.

El material EA1 y la rúbrica se encuentran localmente y no se versionan.

## 3. Entradas y contratos vigentes

- Dataset: Fashion-MNIST.
- Seed inicial: 42.
- Train oficial: 60.000 imágenes.
- Test oficial: 10.000 imágenes reservadas.
- Validation propuesta: 10% estratificado del train oficial.
- Normalización propuesta: `float32` en `[0, 1]`.
- Baseline: configuración E0 de `configs/baseline.json`.
- Test no puede orientar arquitectura, funciones ni hiperparámetros.
- Las decisiones finales requieren teoría, evidencia experimental o ambas.

Hechos ya verificados sobre los binarios oficiales:

- formas `(60000, 28, 28)` y `(10000, 28, 28)`;
- imágenes y etiquetas `uint8`;
- píxeles en `[0, 255]`;
- 6.000/1.000 ejemplos por clase en train/test;
- cero duplicados exactos dentro o entre los splits oficiales;
- checksums coincidentes con el README de Zalando.

No es necesario volver a investigar estos hechos, pero sí comprobarlos sobre la carga efectiva del proyecto y conservar la salida como evidencia.

Si una entrada resulta técnicamente incorrecta o inviable, no debe forzarse: registrar el hallazgo y proponer el cambio en `DECISION_LOG.md`.

## 4. Metas orientativas

Estas son **metas mínimas y orientativas, ampliables con justificación técnica**. No representan una lista exhaustiva ni inmutable: Ignacio puede incorporar o reajustar pasos necesarios, siempre que respete el alcance de la guía maestra y documente las decisiones, la evidencia y su efecto sobre el siguiente handoff.

### M1 - Entorno mínimo reproducible

- crear obligatoriamente `.venv` en la raíz con `uv venv --python 3.12 .venv`;
- comprobar que el intérprete resuelto sea Python 3.12.x y registrar el parche exacto;
- registrar versiones de `uv`, Python y dependencias principales;
- documentar instalación y ejecución realmente probadas;
- fijar seeds de Python, NumPy y TensorFlow;
- comprobar disponibilidad de CPU/GPU sin hacerla requisito de corrección;
- usar WSL2 si se habilita TensorFlow moderno con GPU NVIDIA en Windows;
- evitar dependencias innecesarias;
- no usar Python global, `python -m venv`, Conda, Poetry ni `pip install` directo;
- preparar `pyproject.toml` y `uv.lock` únicamente después de validar las versiones elegidas.

### M2 - Contrato de datos

- cargar Fashion-MNIST mediante `keras.datasets.fashion_mnist.load_data()`;
- definir claramente `X_train`, `X_val`, `X_test`, `y_train`, `y_val`, `y_test`;
- comprobar formas, tipos, rangos y clases;
- asegurar que test permanezca separado;
- justificar normalización, flatten y codificación de etiquetas;
- reutilizar `data_validation.py` y ampliar sus pruebas solo cuando aparezca una nueva invariante;
- llevar la carga y transformación reutilizable a `src/ep1_fashion_mnist/data.py`.

El split debe generarse desde índices del train oficial con 10% estratificado y seed 42. Debe producir 54.000 ejemplos de train, 6.000 de validation, 5.400/600 ejemplos por clase y ninguna intersección entre índices.

### M3 - Exploración

- distribución por clase;
- ejemplos representativos;
- comprobación de balance;
- observaciones relevantes para el modelado;
- figuras seleccionadas en `results/figures/`, no todas las pruebas intermedias.

### M4 - Baseline E0

- implementar construcción del modelo en código reutilizable;
- reportar arquitectura y número de parámetros;
- entrenar exactamente la configuración E0 o documentar cualquier desviación;
- registrar curvas de train/validation;
- calcular métricas de validación coherentes;
- analizar convergencia, underfitting/overfitting y limitaciones;
- no presentar E0 como modelo definitivo.

### M5 - Comparaciones iniciales opcionales

Solo después de validar M1-M4:

- activaciones ReLU, Tanh y Sigmoid;
- categorical crossentropy frente a MSE como contraste pedagógico;
- L2 únicamente si existe una pregunta clara sobre generalización.

Cada comparación debe variar una sola dimensión y conservar un control explícito.

## 5. Entregables esperados

- `src/ep1_fashion_mnist/data.py`;
- módulo de construcción del modelo con nombre acordado y responsabilidad acotada;
- `notebooks/01_ignacio_data_baseline.ipynb`;
- configuración E0 validada o nueva versión trazable;
- salida de los validadores definida en `docs/DATA_CONTRACT.md`;
- figuras/tablas seleccionadas con ID de experimento;
- actualización de `docs/collaborators/ignacio/REPORT.md`;
- decisiones nuevas en `docs/DECISION_LOG.md`;
- actualización pertinente de `docs/RUBRICA_CHECKLIST.md` sin marcar evidencia no verificada;
- handoff de Lucas completado con rutas y estado reales.

Los nombres de módulos pueden ajustarse si mejoran la cohesión. El cambio debe quedar reflejado en la documentación y no duplicar responsabilidades.

## 6. Documentación técnica obligatoria

Por cada decisión relevante, dejar:

1. problema o pregunta;
2. alternativas consideradas;
3. elección;
4. fundamento conceptual;
5. evidencia observada, si existe;
6. limitaciones;
7. impacto sobre el siguiente trabajo.

También deben documentarse los resultados negativos. Un experimento que contradice la hipótesis puede ser evidencia valiosa.

## 7. Criterios de salida

El handoff puede pasar a `READY_FOR_REVIEW` cuando:

- el notebook ejecuta de principio a fin con kernel limpio;
- `sys.executable` apunta al `.venv` del repositorio;
- el entorno puede reconstruirse mediante `uv` siguiendo instrucciones versionadas;
- la carga de datos no depende de rutas personales;
- train, validation y test están identificados y protegidos;
- existen comprobaciones de formas, tipos y rangos;
- las pruebas de `tests/test_data_validation.py` están en verde;
- el split produce 54.000/6.000 casos y conserva 5.400/600 por clase;
- los índices train/validation son disjuntos y cubren exactamente los 60.000 casos originales;
- el baseline se reconstruye desde una configuración identificable;
- las curvas y métricas indican el experimento que las produjo;
- código reutilizable no está duplicado dentro del notebook;
- el informe de Ignacio está completo;
- las desviaciones y preguntas abiertas están explícitas;
- Lucas puede identificar exactamente qué configuración usar como control.

El estado cambia a `ACCEPTED` cuando Cesar revisa la documentación, ejecuta las verificaciones acordadas y puede explicar cómo continuar.

## 8. Condiciones que obligan a detenerse y documentar

- no se puede reproducir el split;
- test fue usado accidentalmente para decidir;
- la codificación de etiquetas no coincide con loss/salida;
- resultados cambian sustancialmente sin explicación entre ejecuciones;
- la configuración E0 no entrena o diverge;
- una decisión requerida afectaría el alcance de Lucas o Cesar;
- una dependencia funciona localmente pero impide ejecución razonable en Colab.

Comando mínimo antes de solicitar revisión:

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m unittest tests.test_data_validation -v
```

Detenerse no significa abandonar: registrar evidencia, alcance del problema y propuesta de resolución.

## 9. Contenido mínimo del handoff a Lucas

Antes de cerrar, completar `RUN_HANDOFF_02_LUCAS.md` con:

- commit o estado exacto revisado;
- instrucciones de entorno probadas;
- rutas de módulos públicos;
- contrato de datos definitivo;
- ID y configuración del baseline validado;
- métricas y curvas de referencia;
- experimentos ya ejecutados;
- riesgos conocidos;
- decisiones que Lucas no debe asumir como definitivas;
- primera comparación recomendada y por qué.

## 10. Fuera de alcance inicial

- usar test para comparar modelos;
- seleccionar el modelo final;
- integrar todas las técnicas de regularización simultáneamente;
- realizar búsquedas automáticas masivas;
- añadir CNN o transfer learning;
- optimizar por diferencias marginales sin comprobar robustez.
