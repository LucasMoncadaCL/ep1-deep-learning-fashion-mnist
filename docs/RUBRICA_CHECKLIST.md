# Checklist trazable de la rúbrica - EP1

Este archivo no declara cumplimiento por intención. Un indicador solo se marca como completado cuando existe evidencia verificable en el notebook, los resultados o la preparación de la defensa.

## Estados de evidencia

- `[ ]` pendiente.
- `[~]` implementado, pendiente de evidencia o revisión.
- `[x]` verificado con evidencia final.

## Encargo grupal - 20%

### IEE 1.1 - Datos, entrenamiento y ajustes

- [~] **IEE 1.1.1 (2%) - Carga y preprocesamiento.** Evidencia: `01_ignacio_data_baseline.ipynb` ejecutado, contrato validado y figuras D0; pendiente de revisión cruzada.
- [~] **IEE 1.1.2 (2%) - Épocas, learning rate y batch size.** Evidencia: E3 y E4 comparan tres learning rates y tres batch sizes mediante configuraciones, tablas, curvas y decisiones D-014/D-015; integrado en el notebook de Lucas y pendiente del notebook final.
- [~] **IEE 1.1.3 (2%) - Experimentos controlados.** Evidencia: E1/E2 varían exclusivamente activación o loss; tabla y figuras comparativas seleccionadas, pendiente de revisión.
- [~] **IEE 1.1.4 (1%) - Ajustes según resultados.** Evidencia: E3–E5 seleccionan learning rate 0,1, batch 128 y capacidad `[256,128]`; D-017 no activa Early Stopping por falta de beneficio material y D-018 impide declararlo sin implementación. Integrado en el notebook de Lucas y pendiente del cierre grupal.

### IEE 1.2 - Funciones de la red

- [~] **IEE 1.2.1 (1%) - Activación, pérdida y salida.** Evidencia: E0 implementa ReLU, Softmax y categorical crossentropy; pendiente de comparación y revisión.
- [~] **IEE 1.2.2 (2%) - Comparación de funciones.** Evidencia: tabla E1/E2 y figuras comparativas de validation; pendiente de integración final y revisión.
- [ ] **IEE 1.2.3 (1%) - Pertinencia para el caso.** Evidencia: selección final conectada con Fashion-MNIST y resultados observados.

### IEE 1.3 - Arquitectura, optimización y regularización

- [~] **IEE 1.3.1 (1%) - Arquitectura MLP.** Evidencia: E5 compara tres capacidades, parámetros, métricas, costo y gaps; selecciona `[256,128]` como candidata equilibrada en el notebook de Lucas. Pendiente del cierre grupal.
- [x] **IEE 1.3.2 (2%) - Optimización y regularización.** Evidencia: E6/E6b y E7–E9 comparan una variable por vez; tablas, curvas y D-019–D-024 documentan estabilidad, convergencia, gaps y resultados negativos.
- [~] **IEE 1.3.3 (2%) - Ajuste de hiperparámetros.** Evidencia: E3–E5 comparan y seleccionan learning rate, batch size y capacidad mediante tablas, curvas, notebook ejecutado y decisiones D-014–D-017; pendiente del cierre grupal.

### IEE 1.4 - Evaluación

- [x] **IEE 1.4.1 (2%) - Métricas pertinentes.** Evidencia: F1 informa Accuracy, Precision, Recall y F1 macro/ponderadas, más métricas por clase y matriz de confusión.
- [x] **IEE 1.4.2 (1%) - Uso de métricas para mejorar.** Evidencia: E6b, E7–E9 y F0 usan métricas de validation, gaps y repeticiones para seleccionar sin usar test.
- [x] **IEE 1.4.3 (1%) - Comparación y solución final.** Evidencia: `FINAL_MODEL_SELECTION.md`, F0 y F1 enlazan las comparaciones con la configuración final y su evaluación única.

## Presentación individual - 80%

### IP 1.1 - Proceso experimental

- [ ] **IP 1.1.1 (8%) - Preprocesamiento.** Evidencia: explicación rigurosa de decisiones e impacto en el modelo.
- [ ] **IP 1.1.2 (8%) - Configuración y gráficos.** Evidencia: gráficos comparativos integrados en una explicación clara.
- [ ] **IP 1.1.3 (8%) - Evaluación crítica de ajustes.** Evidencia: antes/después y argumento causal prudente.

### IP 1.2 - Funciones

- [ ] **IP 1.2.1 (8%) - Efecto de activación, pérdida y salida.** Evidencia: relación entre funciones, convergencia y desempeño.
- [ ] **IP 1.2.2 (5%) - Diferencias mediante gráficos.** Evidencia: visualizaciones legibles y explicación de hallazgos.
- [ ] **IP 1.2.3 (8%) - Selección final de funciones.** Evidencia: defensa técnica relacionada con el problema.

### IP 1.3 - Implementación y optimización

- [ ] **IP 1.3.1 (5%) - Dominio integral.** Evidencia: cada integrante puede explicar código, arquitectura, hiperparámetros, entrenamiento y resultados.
- [ ] **IP 1.3.2 (5%) - Impacto de optimización.** Evidencia: estabilidad, convergencia y generalización respaldadas por resultados.
- [ ] **IP 1.3.3 (5%) - Efecto de hiperparámetros.** Evidencia: comparación, ajuste y selección final.

### IP 1.4 - Métricas y comunicación de resultados

- [ ] **IP 1.4.1 (5%) - Cálculo de métricas.** Evidencia: explicación con ejemplos derivados de la matriz de confusión.
- [ ] **IP 1.4.2 (4%) - Interpretación visual.** Evidencia: gráficos y visualizaciones que sostienen conclusiones.
- [ ] **IP 1.4.3 (11%) - Hallazgos clave.** Evidencia: narrativa técnica con tablas, curvas, matriz de confusión y ejemplos visuales.

## Requisitos transversales

- [ ] Notebook final ejecutado de principio a fin en Google Colab.
- [~] Markdown antes y después de E0–E5 y narrativa final integrada en `EP1_FashionMNIST_FINAL.ipynb`; pendiente de validación limpia en Colab.
- [x] Código reutilizable centralizado en `src/ep1_fashion_mnist/`; `final_evaluation.py` añade la guardia de F1 y está cubierto por pruebas.
- [x] Tabla consolidada disponible en `results/tables/FINAL_MODEL_SELECTION.md`, con vínculos a la evidencia por etapa.
- [x] Test utilizado solo después de congelar decisiones: F0, D-025 y el registro único F1 lo respaldan.
- [~] Instrucciones reproducibles en entorno, informes y handoffs; pendiente de validar la ruta final de Colab.
- [ ] Historial Git con contribuciones trazables.
- [ ] Revisión cruzada completada.
- [ ] Ensayo individual de defensa y control del tiempo.
