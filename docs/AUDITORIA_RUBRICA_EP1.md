# Auditoría de alineación con la rúbrica - EP1 Fashion-MNIST

**Fecha:** 2026-09-15

**Documento auditado:** `GUIA_MAESTRA_EP1_FashionMNIST.md`

**Fuente normativa:** `ref/EP1_DLY0100_Estudiante.pdf`

## 1. Alcance y criterio

Esta auditoría evalúa si la guía contiene un plan capaz de producir la evidencia exigida por la rúbrica. No evalúa todavía el desempeño del modelo ni declara indicadores cumplidos, porque aún no existen notebook final, ejecuciones, tablas ni resultados experimentales.

Estados utilizados:

- **Cubierto:** la guía contempla explícitamente el requisito y define evidencia adecuada.
- **Parcial:** existe intención, pero falta concretar evidencia o procedimiento.
- **Pendiente de ejecución:** el diseño es adecuado, pero solo podrá verificarse con resultados.
- **No aplicable como obligación:** aparece como sugerencia general de la pauta, no como indicador evaluado o no es pertinente al caso.

## 2. Resultado ejecutivo

La guía presenta una alineación metodológica alta con la rúbrica. Cubre los trece indicadores del encargo y los doce indicadores de la presentación a nivel de planificación. Sus fortalezas principales son:

1. separación rigurosa entre train, validation y test;
2. baseline previo y justificable;
3. experimentación controlada;
4. comparación de funciones, hiperparámetros y regularización;
5. registro estructurado de resultados;
6. importancia explícita de la interpretación y defensa técnica;
7. revisión cruzada para evitar conocimiento fragmentado.

El riesgo principal no está en el plan, sino en convertirlo en evidencia concisa y defendible. La rúbrica asigna 80% a la presentación individual, por lo que un notebook completo pero difícil de explicar no sería suficiente.

## 3. Auditoría del encargo grupal

| Indicador | Estado del plan | Evidencia prevista | Observación de auditoría |
|---|---|---|---|
| IEE 1.1.1 - Datos y preprocesamiento | Cubierto | EDA, normalización, división y Markdown | Añadir comprobaciones ejecutables de formas, rangos, tipos, clases y ausencia de solapamiento. |
| IEE 1.1.2 - Parámetros clave | Cubierto | Configuración de épocas, LR y batch | Registrar siempre valor, justificación y función dentro del proceso de optimización. |
| IEE 1.1.3 - Experimentos controlados | Cubierto | E1-E10, curvas y tablas | Mantener una configuración de control explícita por experimento; no basta con afirmar que lo demás quedó constante. |
| IEE 1.1.4 - Evaluación y ajustes | Cubierto | Patrón objetivo-hipótesis-resultado-decisión | El Decision Log debe enlazar cada cambio importante con el experimento que lo respalda. |
| IEE 1.2.1 - Funciones pertinentes | Cubierto | ReLU/Tanh/Sigmoid, Softmax y losses | Diferenciar función oculta, salida y pérdida; explicar compatibilidad entre Softmax, etiquetas y crossentropy. |
| IEE 1.2.2 - Comparación de funciones | Cubierto | Tabla y curvas | MSE debe presentarse como contraste pedagógico, no como alternativa igualmente apropiada para la solución final. |
| IEE 1.2.3 - Pertinencia para el caso | Cubierto | Selección basada en Fashion-MNIST | Conectar la selección final con convergencia, desempeño y naturaleza multiclase. |
| IEE 1.3.1 - Arquitectura MLP | Cubierto | Baseline y experimento de capacidad | Reportar número de parámetros y relación entre capacidad, underfitting, overfitting y costo. |
| IEE 1.3.2 - Optimización y regularización | Cubierto | SGD/RMSProp/Adam, Dropout, L2, BatchNorm, Early Stopping | Separar optimización de regularización en la explicación, aunque la pauta las agrupe. |
| IEE 1.3.3 - Hiperparámetros | Cubierto | LR, batch, capacidad y selección final | Evitar elegir por una sola métrica; usar validation loss, Macro F1, gap y complejidad. |
| IEE 1.4.1 - Métricas | Cubierto | Accuracy, Precision, Recall y F1 | Añadir ejemplos numéricos desde la matriz de confusión para demostrar comprensión del cálculo. |
| IEE 1.4.2 - Interpretación y mejora | Parcial | Métricas globales y por clase | Debe existir al menos una decisión o propuesta explícita derivada de la interpretación de métricas. |
| IEE 1.4.3 - Comparación final | Cubierto | Tabla maestra y criterios de selección | Congelar criterios antes de mirar test y explicar los trade-offs del modelo escogido. |

## 4. Auditoría de la presentación individual

| Indicador | Estado del plan | Acción necesaria |
|---|---|---|
| IP 1.1.1 - Preprocesamiento | Pendiente de ejecución | Preparar una explicación breve que conecte cada transformación con su efecto esperado. |
| IP 1.1.2 - Configuración y gráficos | Pendiente de ejecución | Seleccionar pocas curvas comparativas, legibles y directamente útiles para el argumento. |
| IP 1.1.3 - Evaluación crítica de ajustes | Pendiente de ejecución | Mostrar al menos un cambio que ayudó y uno que no ayudó o tuvo un costo. |
| IP 1.2.1 - Efecto de funciones | Pendiente de ejecución | Relacionar teoría de saturación/gradientes con curvas reales, sin afirmar causalidad más allá de la evidencia. |
| IP 1.2.2 - Diferencias gráficas | Pendiente de ejecución | Estandarizar escalas, colores, títulos y etiquetas para comparaciones honestas. |
| IP 1.2.3 - Selección final | Pendiente de ejecución | Preparar defensa de ReLU/Softmax/crossentropy o de las funciones que finalmente resulten seleccionadas. |
| IP 1.3.1 - Dominio integral | Parcial | La revisión cruzada está definida; falta ensayo individual y preguntas técnicas. |
| IP 1.3.2 - Técnicas de optimización | Pendiente de ejecución | Mostrar impacto en estabilidad, convergencia y generalización, no solo accuracy final. |
| IP 1.3.3 - Hiperparámetros | Pendiente de ejecución | Resumir comparaciones en una tabla y justificar la configuración elegida. |
| IP 1.4.1 - Cálculo de métricas | Parcial | Incorporar ejemplos con TP, FP y FN para una clase concreta. |
| IP 1.4.2 - Interpretación visual | Pendiente de ejecución | Conectar curvas, matriz de confusión y ejemplos de errores con conclusiones. |
| IP 1.4.3 - Hallazgos clave | Pendiente de ejecución | Diseñar la presentación alrededor de 3-5 hallazgos, no recorrer el notebook celda por celda. |

## 5. Decisiones correctas que deben mantenerse

### 5.1. Test reservado

El test no participa en selección de arquitectura, funciones o hiperparámetros. Esta decisión evita fuga de información y estimaciones optimistas del desempeño.

### 5.2. Baseline sin regularización

Permite medir el aporte incremental de Dropout, L2, Batch Normalization y Early Stopping. El baseline debe ser funcional, pero no artificialmente optimizado.

### 5.3. Una variable por comparación

Es indispensable para atribuir diferencias con prudencia. Cuando un optimizador requiera retuning de learning rate, debe tratarse como una segunda etapa explícita y no confundirse con la comparación controlada inicial.

### 5.4. Macro F1 como complemento

Fashion-MNIST está balanceado, pero Macro F1 sigue siendo útil para dar el mismo peso a cada clase y detectar degradaciones que la accuracy global puede ocultar.

### 5.5. Desarrollo local y entrega en Colab

Es viable mientras el notebook final se ejecute desde cero en Colab, no dependa de rutas locales y declare sus dependencias.

## 6. Ajustes prioritarios antes de programar experimentos

### Prioridad alta

1. Definir un esquema único de configuración y registro de experimentos.
2. Definir cómo se identificará inequívocamente cada ejecución.
3. Establecer funciones compartidas para construcción, entrenamiento, evaluación y gráficos.
4. Añadir comprobaciones automáticas del protocolo de datos.
5. Precisar el protocolo de reentrenamiento final antes de abrir test.
6. Definir criterios de selección del modelo antes de obtener resultados finales.

### Prioridad media

1. Registrar tiempo de entrenamiento y número de parámetros.
2. Repetir con varias semillas solo comparaciones críticas o diferencias marginales.
3. Guardar configuración, historia y métricas juntas para evitar resultados huérfanos.
4. Estandarizar gráficos para que las comparaciones utilicen escalas equivalentes.

### Prioridad de presentación

1. Incorporar ejemplos numéricos del cálculo de métricas.
2. Preparar preguntas individuales de defensa.
3. Ensayar un máximo de 10 minutos.
4. Seleccionar hallazgos y visualizaciones después de terminar los experimentos.

## 7. Sugerencias de la pauta que no deben incorporarse automáticamente

### Data augmentation

La pauta la menciona como buena práctica general, pero no es un indicador obligatorio. Puede ser útil para imágenes, aunque añadirla introduciría otra variable experimental y mayor complejidad. Solo debe incluirse si responde a una hipótesis concreta y queda tiempo para evaluarla controladamente.

### Transfer learning

No es pertinente para demostrar una MLP construida y analizada por el equipo. Introducir un modelo preentrenado desviaría el foco de los fundamentos evaluados.

### Validación cruzada

No es obligatoria. Un split estratificado y fijo de validación es suficiente para el plan inicial. Las repeticiones con distintas semillas son una alternativa más directa para comprobar robustez en comparaciones críticas.

## 8. Veredicto

La guía es apta para dirigir el proyecto y tiene cobertura conceptual suficiente para aspirar al nivel de muy buen desempeño. La condición es que cada intención se convierta en evidencia verificable y que el volumen de experimentos no reduzca la calidad del análisis.

El proyecto debe optimizar claridad experimental, trazabilidad y dominio técnico; no cantidad bruta de modelos entrenados.
