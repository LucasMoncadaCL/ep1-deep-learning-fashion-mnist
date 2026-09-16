# Checklist trazable de la rúbrica - EP1

Este archivo no declara cumplimiento por intención. Un indicador solo se marca como completado cuando existe evidencia verificable en el notebook, los resultados o la preparación de la defensa.

## Estados de evidencia

- `[ ]` pendiente.
- `[~]` implementado, pendiente de evidencia o revisión.
- `[x]` verificado con evidencia final.

## Encargo grupal - 20%

### IEE 1.1 - Datos, entrenamiento y ajustes

- [ ] **IEE 1.1.1 (2%) - Carga y preprocesamiento.** Evidencia: sección del notebook con formas, tipos, rango, normalización, división de datos y justificación Markdown.
- [ ] **IEE 1.1.2 (2%) - Épocas, learning rate y batch size.** Evidencia: configuración registrada y explicación técnica de los tres parámetros.
- [ ] **IEE 1.1.3 (2%) - Experimentos controlados.** Evidencia: comparaciones variando un parámetro por vez, datos precisos y visualizaciones.
- [ ] **IEE 1.1.4 (1%) - Ajustes según resultados.** Evidencia: secuencia observación, hipótesis, cambio, resultado y conclusión.

### IEE 1.2 - Funciones de la red

- [ ] **IEE 1.2.1 (1%) - Activación, pérdida y salida.** Evidencia: implementación pertinente y justificación técnica para el problema multiclase.
- [ ] **IEE 1.2.2 (2%) - Comparación de funciones.** Evidencia: tabla comparativa, curvas y análisis de ventajas, limitaciones e impacto.
- [ ] **IEE 1.2.3 (1%) - Pertinencia para el caso.** Evidencia: selección final conectada con Fashion-MNIST y resultados observados.

### IEE 1.3 - Arquitectura, optimización y regularización

- [ ] **IEE 1.3.1 (1%) - Arquitectura MLP.** Evidencia: diagrama o resumen de capas, parámetros y justificación de cada decisión estructural.
- [ ] **IEE 1.3.2 (2%) - Optimización y regularización.** Evidencia: comparación con/sin técnica y análisis de estabilidad, convergencia y generalización.
- [ ] **IEE 1.3.3 (2%) - Ajuste de hiperparámetros.** Evidencia: configuraciones comparadas y selección final fundamentada.

### IEE 1.4 - Evaluación

- [ ] **IEE 1.4.1 (2%) - Métricas pertinentes.** Evidencia: Accuracy, Precision, Recall y F1 correctamente calculadas e interpretadas.
- [ ] **IEE 1.4.2 (1%) - Uso de métricas para mejorar.** Evidencia: propuestas o decisiones derivadas de métricas globales y por clase.
- [ ] **IEE 1.4.3 (1%) - Comparación y solución final.** Evidencia: tabla global y elección de configuración basada en evidencia experimental.

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
- [ ] Markdown antes y después de cada experimento.
- [ ] Código modularizado y sin duplicación innecesaria.
- [ ] Tabla maestra de configuraciones y resultados.
- [ ] Test utilizado solo después de congelar decisiones.
- [ ] Instrucciones reproducibles de ejecución.
- [ ] Historial Git con contribuciones trazables.
- [ ] Revisión cruzada completada.
- [ ] Ensayo individual de defensa y control del tiempo.
