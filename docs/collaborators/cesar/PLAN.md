# Plan experimental vivo - Cesar Rojas

**Estado:** WAITING_ON_HANDOFF_02_ACCEPTANCE

**Entrada prevista:** `main` después de integrar el Handoff 02.

**Naturaleza:** metas mínimas y orientativas, ampliables con justificación técnica. El orden puede adaptarse si aparece evidencia nueva, pero no se pueden mezclar variables ni abrir test antes de congelar configuración y protocolo.

## 1. Objetivo

Comparar optimizadores y técnicas de regularización sobre la candidata recibida de Lucas, seleccionar una configuración final mediante validation y realizar una única evaluación sobre test después de congelar todas las decisiones.

La etapa debe producir evidencia suficiente para:

- explicar estabilidad, convergencia y generalización;
- atribuir cada cambio a una variable identificable;
- justificar resultados negativos y alternativas descartadas;
- responder los indicadores de optimización, regularización y evaluación de la rúbrica;
- integrar el notebook final sin depender de archivos locales no versionados.

## 2. Entrada técnica

Control recibido:

- dataset Fashion-MNIST;
- split estratificado train/validation 54.000/6.000 con seed 42;
- arquitectura `[256, 128]`;
- ReLU y salida Softmax de diez unidades;
- categorical crossentropy;
- SGD con `learning_rate=0.1`;
- batch size 128;
- 20 épocas;
- sin Dropout, Batch Normalization, L2 ni Early Stopping;
- Accuracy validation `0,8933` y F1 Macro `0,8936`;
- test oficial sin evaluación ni predicción.

La candidata es un control trazable, no un modelo final.

## 3. Invariantes metodológicas

1. Trabajar exclusivamente en `.venv` creado y sincronizado con `uv`.
2. Partir desde `main` actualizado después de la aceptación del Handoff 02.
3. Mantener test fuera de toda decisión de ajuste.
4. Cambiar una variable por comparación inicial.
5. Separar comparación de optimizadores y retuning de learning rate.
6. Evaluar cada técnica de regularización primero contra un control sin esa técnica.
7. Registrar configuración efectiva, seed, épocas, mejores épocas, duración, parámetros, métricas y gaps.
8. Tratar las diferencias marginales como hipótesis que requieren repetición.
9. Documentar decisiones antes y después del código en el notebook.
10. No presentar una técnica como aplicada si el ejecutor no la implementa realmente.

## 4. Etapas recomendadas

### C0 - Recepción y reproducción

Objetivo: demostrar que el punto de partida puede reproducirse antes de modificarlo.

Acciones mínimas:

- ejecutar `uv sync --frozen`;
- registrar versiones y `sys.executable`;
- ejecutar pruebas y Ruff;
- reproducir `configs/E5_capacity_256_128.json`;
- comparar las métricas con el margen razonable de reproducibilidad documentado;
- registrar cualquier divergencia antes de iniciar E6.

Criterio de salida: control reproducido y entorno verificado sin consultar test.

### E6 - Comparación inicial de optimizadores

Comparar SGD, RMSProp y Adam manteniendo fija la configuración recibida, incluido inicialmente el learning rate. Esta primera comparación atribuye el cambio al optimizador, aunque el valor común no sea óptimo para todos.

Observar como mínimo:

- Accuracy, Precision, Recall y F1 macro y ponderadas;
- validation loss y accuracy por época;
- estabilidad de curvas;
- mejor época;
- gaps finales;
- duración por CPU o entorno comparable.

No concluir que un optimizador es globalmente peor solo porque requiere otra escala de learning rate.

### E6b - Retuning condicional de learning rate

Solo si E6 muestra que el optimizador candidato está limitado por el learning rate común, ejecutar una etapa separada. Mantener optimizador, arquitectura, batch, épocas y seed, modificando únicamente learning rate.

Los valores concretos se definen después de observar E6 y deben justificarse. No convertir esta etapa en una grilla combinatoria sin hipótesis.

### E7 - Dropout

Comparar el nuevo control con y sin Dropout. Seleccionar uno o más valores plausibles a partir de los gaps observados; documentar ubicación de las capas, tasa y efecto sobre convergencia y validation.

No activar simultáneamente L2 o Batch Normalization en la primera comparación.

### E8 - Batch Normalization

Comparar con y sin Batch Normalization usando el control vigente. Antes de entrenar, revisar y justificar el orden efectivo `Dense`, activación y normalización implementado en `build_mlp`; cualquier cambio estructural exige pruebas y una decisión registrada.

No mezclar esta primera comparación con Dropout o L2 salvo que una etapa posterior evalúe explícitamente la combinación.

### E9 - Regularización L2

Comparar el control con y sin L2. Elegir la fuerza a partir de una hipótesis explícita y registrar su efecto sobre loss, gaps y desempeño. Si se prueban varios valores, mantener las demás variables constantes.

### E10 - Early Stopping condicional

Reevaluar solo cuando las curvas del control seleccionado muestren una oportunidad material de detener antes o restaurar mejores pesos.

El ejecutor actualmente rechaza `early_stopping=true`. Si corresponde implementar la técnica, el contrato mínimo debe incluir:

- `monitor`;
- `mode`;
- `patience`;
- `min_delta`;
- máximo de épocas;
- `restore_best_weights`;
- pruebas que demuestren que el callback se aplica;
- registro de épocas solicitadas y completadas.

Comparar con y sin callback bajo condiciones interpretables.

### R - Repeticiones para decisiones marginales

Si dos candidatas difieren de forma marginal, repetirlas con seeds adicionales antes de congelar el modelo. Informar media y dispersión sin reemplazar ni ocultar la corrida seed 42.

No son obligatorias repeticiones para diferencias grandes y estables; la necesidad debe justificarse.

### F0 - Congelamiento previo al test

Antes de consultar test debe existir una decisión versionada que congele:

- arquitectura y funciones;
- optimizador y learning rate;
- batch size;
- regularización y callbacks;
- seed o protocolo de seeds;
- criterio de selección;
- métricas finales;
- protocolo exacto de entrenamiento final.

También debe resolverse explícitamente una de estas estrategias:

1. evaluar el modelo seleccionado que conserva el split 54.000/6.000; o
2. reentrenar desde cero con los 60.000 ejemplos oficiales de train y un número de épocas fijado previamente a partir de validation.

La elección debe realizarse antes de observar test. Si se reentrena con 60.000 ejemplos, no puede usarse test como sustituto de validation ni para decidir épocas.

### F1 - Evaluación final única

Después de F0:

- ejecutar test una sola vez;
- calcular Accuracy, Precision, Recall y F1 macro y ponderadas;
- producir matriz de confusión;
- reportar métricas por clase;
- analizar ejemplos correctos, incorrectos y de baja confianza;
- registrar limitaciones sin volver a ajustar el modelo.

La infraestructura de evaluación final debe estar separada del ejecutor de validation para evitar aperturas accidentales durante el tuning.

### F2 - Integración documental

- completar `docs/collaborators/cesar/REPORT.md`;
- ejecutar `notebooks/03_cesar_optimization_evaluation.ipynb` desde kernel limpio;
- actualizar `docs/DECISION_LOG.md` y `docs/RUBRICA_CHECKLIST.md`;
- producir tablas y figuras seleccionadas;
- preparar el handoff de integración grupal;
- incorporar los resultados al notebook final y al informe formal solo después de revisión.

## 5. Convención inicial de IDs

La convención es orientativa y puede ampliarse sin reutilizar identificadores:

```text
E6_optimizer_<nombre>
E6b_<optimizador>_lr_<valor>
E7_dropout_<valor>
E8_batch_norm_<on|off>
E9_l2_<valor>
E10_early_stopping_<on|off>
F0_frozen_config
F1_final_test
```

## 6. Evidencia mínima por familia

Cada familia debe dejar:

- configuraciones JSON versionadas;
- una tabla comparativa;
- curvas de validation pertinentes;
- interpretación Markdown previa y posterior;
- decisión o resultado negativo;
- comandos de reproducción;
- actualización del informe de Cesar;
- entrada en Decision Log cuando cambie el control o el protocolo.

## 7. Criterio de selección

No seleccionar por una sola métrica. Evaluar conjuntamente:

- Accuracy y F1 Macro;
- Precision y Recall, especialmente por clase en la evaluación final;
- validation loss;
- estabilidad y convergencia;
- gaps train--validation;
- complejidad y parámetros;
- costo computacional en un entorno comparable;
- claridad y reproducibilidad de la solución.

Una mejora mínima puede no justificar mayor complejidad o menor estabilidad.

## 8. Condiciones de pausa

Detener y documentar antes de continuar si:

- el control recibido no se reproduce;
- una configuración cambia más de una variable sin una razón explícita;
- aparece una consulta accidental a test;
- una técnica declarada no está implementada;
- los artefactos no permiten identificar la configuración efectiva;
- la decisión de reentrenamiento final sigue abierta al llegar a F0.

## 9. Definición de terminado

La etapa de Cesar estará lista para revisión cuando:

- optimizadores y regularización tengan comparaciones controladas;
- los cambios estén justificados por teoría y evidencia;
- la configuración y el protocolo final estén congelados antes de test;
- test se haya evaluado una sola vez;
- exista análisis global, por clase y visual de errores;
- notebook, tablas, figuras, configuraciones e informe sean reproducibles;
- limitaciones y resultados negativos estén documentados;
- el siguiente revisor pueda reconstruir y defender las decisiones.
