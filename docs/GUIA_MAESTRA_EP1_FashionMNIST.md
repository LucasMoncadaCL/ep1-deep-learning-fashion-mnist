# Guía Maestra — Evaluación Parcial 1 · Deep Learning (DLY0100)

> **Estado:** Documento vivo de referencia  
> **Versión actual:** v0.7  
> **Dataset seleccionado:** Fashion-MNIST  
> **Integrantes:** Ignacio Silva · Lucas Moncada · Cesar Rojas  
> **Propósito:** Coordinar el trabajo del grupo, evitar solapamientos, mantener trazabilidad de decisiones y asegurar cobertura completa de la rúbrica.

---

## 1. Naturaleza de esta guía

Esta guía **no es una receta que deba seguirse al pie de la letra**.

Su función es definir:

- qué exige la evaluación;
- qué principios metodológicos seguirá el grupo;
- qué evidencia debe producirse;
- cómo se documentarán las decisiones;
- cómo se dividirá y revisará el trabajo;
- qué hipótesis iniciales se probarán;
- cómo se decidirán los cambios durante el proyecto.

Las configuraciones técnicas incluidas aquí son **puntos de partida sujetos a validación experimental**.

> **Regla principal:** ninguna arquitectura, función, hiperparámetro o técnica se mantendrá únicamente porque aparezca en este documento. Toda decisión final debe quedar respaldada por teoría, evidencia experimental o ambas.

---

# 2. Fuentes de referencia del proyecto

## 2.1. Pauta oficial de evaluación

Documento principal:

- `EP1_DLY0100_Estudiante.pdf`

La pauta establece que la evaluación consiste en implementar una **Red Neuronal Artificial Multicapa (MLP)** para resolver un problema práctico de **clasificación**, usando Python y TensorFlow/Keras o PyTorch.

La evaluación solicita, entre otros aspectos:

- carga y preprocesamiento de datos;
- diseño e implementación de una MLP;
- configuración de épocas, tasa de aprendizaje y batch size;
- experimentos controlados variando un parámetro a la vez;
- comparación de funciones de activación y pérdida;
- técnicas de optimización y regularización;
- análisis de hiperparámetros;
- métricas Accuracy, Precision, Recall y F1-Score;
- tablas y visualizaciones comparativas;
- justificación técnica mediante Markdown;
- notebook documentado;
- uso de GitHub para trabajo colaborativo;
- presentación/defensa técnica.

## 2.2. Material teórico de EA1

Se utilizarán como fundamento conceptual:

- `1.1.1 Introducción al Deep Learning.pdf`
- `1.1.3 Aplicaciones de Deep Learning.pdf`
- `1.2.1 El Perceptrón.pdf`
- `1.2.4 Redes Fully Connected Feed Forward.pdf`
- `1.3.1 Descenso del Gradiente.pdf`
- `1.4.1 Backpropagation.pdf`
- `1.4.2 Generalización_Métricas.pdf`
- `1.5.1 Técnicas de Regularización.pdf`
- `1.6.1 Desvanecimiento y Explosión del Gradiente.pdf`
- `1.6.2 Optimizadores.pdf`

## 2.3. Repositorio práctico del docente

Repositorio:

- `gpintofuentes/DUOC--Deep-Learning-OLS`

Notebooks especialmente relevantes:

- `Desafio_Efecto_Hiperparametros_SOLUCION.ipynb`
- `1_4_3_Actividad__Ejemplo_práctico_de_Generalización.ipynb`
- `1.5.3 Aplicando_técnicas_de_Regularización.ipynb`
- `1.5.4 Uso_de_Early_Stopping.ipynb`
- `1.6.3 Actividad_Optimizadores.ipynb`
- `GP_1_3_3_Comprender_el_descenso_del_Gradiente.ipynb`
- `GP_new_1_2_3_Actividad_Construir_un_Perceptrón_programa_Python.ipynb`

Estos notebooks serán usados como referencia del **enfoque práctico enseñado por el profesor**, no como soluciones que deban copiarse literalmente.

---

# 3. Resumen de la evaluación

## 3.1. Objetivo académico

Construir, entrenar, analizar y mejorar una MLP capaz de resolver un problema de clasificación, demostrando comprensión de:

- cómo aprende una red neuronal;
- cómo influyen los hiperparámetros;
- cómo afectan las funciones de activación y pérdida;
- cómo influyen los optimizadores;
- cómo detectar problemas de generalización;
- cómo aplicar regularización;
- cómo interpretar métricas;
- cómo justificar técnicamente una configuración final.

## 3.2. Ponderación

Según la pauta:

- **Evaluación Parcial 1:** 30% de la asignatura.
- **Encargo / Notebook:** 20% de la evaluación.
- **Presentación / Defensa:** 80% de la evaluación.
- **Tiempo de presentación:** máximo 10 minutos.

> La defensa técnica tiene un peso especialmente alto. El proyecto debe prepararse pensando no solo en que el código funcione, sino en que **los tres integrantes puedan explicar y defender el trabajo completo**.

## 3.3. Conformación del equipo

La pauta general menciona trabajo **en parejas/duplas**, mientras que este grupo está compuesto por tres integrantes.

La conformación de Ignacio Silva, Lucas Moncada y Cesar Rojas como grupo de tres ya fue resuelta y autorizada. La distribución interna del trabajo no modifica el requisito de que cada integrante domine y pueda defender el proyecto completo.

---

# 4. Dataset seleccionado

## 4.1. Fashion-MNIST

Se utilizará **Fashion-MNIST**.

Las propiedades verificadas, checksums, política de particiones e invariantes automatizadas se mantienen en `docs/DATA_CONTRACT.md`.

Características:

- 70.000 imágenes en total;
- 60.000 imágenes de entrenamiento;
- 10.000 imágenes de prueba;
- escala de grises;
- 28 × 28 píxeles;
- 10 clases.

Clases:

| ID | Clase |
|---:|---|
| 0 | T-shirt/top |
| 1 | Trouser |
| 2 | Pullover |
| 3 | Dress |
| 4 | Coat |
| 5 | Sandal |
| 6 | Shirt |
| 7 | Sneaker |
| 8 | Bag |
| 9 | Ankle boot |

## 4.2. Razones para escoger Fashion-MNIST

La elección busca equilibrar:

- compatibilidad con una MLP;
- dificultad suficiente para generar análisis;
- impacto visual en la presentación;
- errores interpretables;
- posibilidad de estudiar generalización y regularización;
- comparación clara de configuraciones.

Fashion-MNIST permite analizar confusiones visualmente razonables como:

- Shirt ↔ T-shirt/top;
- Pullover ↔ Coat;
- Sandal ↔ Sneaker.

Esto permite conectar métricas y matriz de confusión con ejemplos concretos.

---

# 5. Pregunta central del proyecto

> **¿Cómo afectan las decisiones de arquitectura, funciones, hiperparámetros, optimizadores y técnicas de regularización al aprendizaje y a la capacidad de generalización de una MLP que clasifica prendas de Fashion-MNIST?**

El proyecto no debe limitarse a “obtener buena accuracy”.

Debe mostrar un proceso:

```text
Datos
  ↓
Preprocesamiento
  ↓
MLP baseline
  ↓
Experimentos controlados
  ↓
Análisis
  ↓
Ajustes
  ↓
Regularización / Optimización
  ↓
Selección de configuración
  ↓
Evaluación final
  ↓
Conclusiones
```

---

# 6. Principios metodológicos no negociables

1. **Un parámetro por experimento controlado.**
2. Mantener las demás condiciones constantes.
3. Fijar semillas para reproducibilidad.
4. No usar el conjunto de test para ajustar hiperparámetros.
5. Justificar las decisiones **antes** del experimento cuando sean hipótesis teóricas.
6. Analizar los resultados **después** del experimento.
7. No presentar una configuración como “mejor” sin evidencia.
8. Guardar tablas y gráficos de cada experimento.
9. Mantener un registro de decisiones.
10. No fusionar código al proyecto final sin revisión cruzada.
11. Todos los integrantes deben comprender el notebook completo.
12. La configuración final se decide por evidencia, no por preferencia.

---

# 7. Entorno de trabajo

## 7.1. Desarrollo

Se trabajará principalmente de forma local con GPU:

- RTX 3050 6 GB;
- RTX 4050 6 GB;
- RTX 4060 6 GB.

Fashion-MNIST + MLP es suficientemente liviano para este hardware.

## 7.2. Stack propuesto

| Elemento | Decisión |
|---|---|
| Lenguaje | Python 3.12.x |
| Framework | TensorFlow / Keras |
| Notebook | Jupyter Notebook |
| Colaboración | GitHub |
| Gráficos | Matplotlib |
| Datos | NumPy / Pandas |
| Métricas | scikit-learn |
| Semilla inicial | 42 |

## 7.3. Entorno virtual obligatorio

Todo desarrollo local debe ejecutarse dentro de `.venv` en la raíz del repositorio, creado mediante `uv venv`.

No se permite utilizar como entorno del proyecto:

- Python global;
- `python -m venv`;
- Conda;
- Poetry;
- instalaciones directas mediante `pip install`.

La versión oficial es Python 3.12.x. `.python-version` fija la rama menor `3.12` y el entorno debe crearse con `uv venv --python 3.12 .venv`. Esta versión está soportada por TensorFlow y coincide con la rama usada por los runtimes actuales de Colab. Las dependencias se fijarán en `pyproject.toml` y `uv.lock` después de su validación conjunta. El procedimiento y los criterios se mantienen en `docs/ENVIRONMENT.md`.

Para TensorFlow moderno, las GPU NVIDIA de los computadores Windows se utilizarán mediante WSL2; el soporte GPU nativo terminó en TensorFlow 2.10. La ejecución por CPU en Windows sigue siendo válida para comprobaciones rápidas.

## 7.4. Google Colab

La pauta menciona explícitamente Google Colab.

Por ello:

- el desarrollo puede realizarse localmente;
- el entregable seguirá siendo `.ipynb`;
- el notebook final debe abrir correctamente en Colab;
- antes de entregar, debe ejecutarse de principio a fin en un entorno limpio de Colab.

Colab será tratado como **entorno oficial de validación y entrega**, no necesariamente como entorno principal de desarrollo.

Antes de entregar, el notebook deberá ejecutarse mediante `Runtime > Run all` en un entorno limpio de Colab. No podrá depender de rutas absolutas, archivos locales no versionados ni del estado previo de celdas ejecutadas fuera de orden.

---

# 8. Reproducibilidad

Se fijarán semillas:

```python
import random
import numpy as np
import tensorflow as tf

SEED = 42

random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)
```

También se registrarán versiones:

```python
import tensorflow as tf
import sklearn
import numpy as np
import pandas as pd

print("TensorFlow:", tf.__version__)
print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("scikit-learn:", sklearn.__version__)
```

Se verificará GPU:

```python
tf.config.list_physical_devices("GPU")
```

> Aunque se fijen semillas, pequeñas diferencias numéricas pueden existir entre hardware, versiones y operaciones GPU. Las conclusiones deben basarse en tendencias suficientemente claras y no en diferencias marginales.

---

# 9. Protocolo de datos

## 9.1. Separación propuesta

Los 60.000 ejemplos oficiales de entrenamiento se dividirán en:

- **54.000 train**
- **6.000 validation**

Los 10.000 ejemplos oficiales de test quedarán reservados como:

- **10.000 test final**

Propuesta:

```python
train_test_split(
    X,
    y,
    test_size=0.10,
    random_state=42,
    stratify=y
)
```

## 9.2. Filosofía

```text
TRAIN
→ ajustar pesos y bias

VALIDATION
→ comparar configuraciones y tomar decisiones

TEST
→ evaluación final del modelo congelado
```

**Regla:** después de observar los resultados de test final, no se seguirán ajustando hiperparámetros.

---

# 10. Preprocesamiento

## 10.1. Normalización

Los píxeles se transformarán desde:

```text
0 ... 255
```

a:

```text
0 ... 1
```

mediante:

```python
X = X.astype("float32") / 255.0
```

Justificación inicial:

- homogeneizar escala;
- facilitar optimización;
- mantener consistencia con lo estudiado en EA1.

## 10.2. Entrada para MLP

Una imagen 28 × 28 se transformará en 784 características.

Dos alternativas válidas:

```python
keras.layers.Flatten(input_shape=(28, 28))
```

o:

```python
X.reshape(-1, 784)
```

Se elegirá una y se mantendrá consistentemente.

## 10.3. Etiquetas

Para el baseline se propone **one-hot encoding** para mantener coherencia con:

- salida Softmax;
- `categorical_crossentropy`.

Ejemplo:

```python
keras.utils.to_categorical(y, 10)
```

Esta decisión también será comparada conceptualmente con la alternativa `sparse_categorical_crossentropy` si resulta útil para la explicación, aunque no es necesario convertir esa diferencia en un experimento principal si no aporta evidencia relevante.

---

# 11. Análisis exploratorio obligatorio

Antes de entrenar:

- forma de los datasets;
- tipo de dato;
- mínimo y máximo de píxeles;
- cantidad de clases;
- distribución de clases;
- nombres de las clases;
- ejemplos visuales;
- comprobación del balance de clases.

Visualizaciones mínimas:

1. cuadrícula de imágenes;
2. distribución por clase.

---

# 12. Modelo baseline — hipótesis inicial

## 12.1. Configuración propuesta

> **Importante:** esta es una configuración de referencia, no la arquitectura final.

```text
Input: 784

Dense 256
ReLU

Dense 128
ReLU

Dense 10
Softmax
```

Configuración inicial propuesta:

| Parámetro | Valor |
|---|---|
| Capas ocultas | `[256, 128]` |
| Activación | ReLU |
| Salida | Softmax |
| Loss | Categorical Crossentropy |
| Optimizador | SGD |
| Learning rate | 0.01 |
| Batch size | 128 |
| Epochs | 20 |
| Dropout | 0 |
| Batch Normalization | No |
| L2 | 0 |
| Seed | 42 |

## 12.2. Justificación previa del baseline

### Entrada de 784

Fashion-MNIST contiene imágenes 28 × 28. Una MLP fully connected recibe un vector, por lo que cada imagen se representa mediante 784 características.

### Dos capas ocultas

Se propone una red de complejidad moderada:

- más expresiva que un perceptrón simple;
- suficientemente profunda para aprender relaciones no lineales;
- no excesivamente compleja para el baseline.

### 256 → 128 neuronas

Arquitectura decreciente de capacidad moderada.

No se asume que sea óptima: posteriormente se comparará con redes menores y mayores.

### ReLU

Hipótesis inicial sustentada en EA1:

- función no lineal;
- ampliamente utilizada en capas ocultas;
- comportamiento favorable respecto del desvanecimiento del gradiente frente a activaciones saturables.

### Softmax

El problema tiene 10 clases mutuamente excluyentes.

La salida necesita 10 valores interpretables como distribución de probabilidad.

### Categorical Crossentropy

Adecuada para clasificación multiclase con:

- Softmax;
- etiquetas one-hot.

### SGD

Se escoge como optimizador baseline porque:

- es conceptualmente simple;
- permite observar de forma clara el efecto del learning rate;
- servirá como referencia frente a RMSProp y Adam.

### Learning rate = 0.01

Punto de partida razonable para SGD y coherente con ejercicios del docente.

No se considera óptimo de antemano.

### Batch = 128

Punto intermedio para comenzar.

Posteriormente será comparado con batches menores y mayores.

### 20 épocas

Permite observar las primeras curvas de convergencia sin introducir inicialmente Early Stopping.

### Sin regularización

El baseline no tendrá inicialmente:

- Dropout;
- L2;
- Batch Normalization;
- Early Stopping.

Esto permitirá medir posteriormente el aporte de cada técnica.

---

# 13. Regla de justificación

Se diferenciarán siempre dos tipos de justificación.

## 13.1. Justificación previa / hipótesis

Ejemplo:

> Según lo estudiado, esperamos que ReLU favorezca una convergencia más estable que Sigmoid en capas ocultas.

## 13.2. Justificación posterior / evidencia

Ejemplo:

> En los experimentos realizados, ReLU alcanzó menor validation loss y mostró una convergencia más rápida que Sigmoid bajo las mismas condiciones.

> **No se deben escribir hipótesis retroactivamente después de conocer los resultados.**

---

# 14. Infraestructura común de código

Para evitar que cada integrante implemente modelos de forma distinta se crearán funciones reutilizables.

Propuesta:

```python
construir_modelo(
    capas_ocultas,
    activacion,
    dropout,
    batch_normalization,
    l2_strength,
    seed
)
```

```python
entrenar_modelo(
    modelo,
    optimizer,
    learning_rate,
    loss,
    batch_size,
    epochs,
    callbacks=None
)
```

```python
evaluar_modelo(...)
```

```python
graficar_historia(...)
```

```python
comparar_historias(...)
```

```python
registrar_resultado(...)
```

El objetivo es que todas las configuraciones sean generadas con la misma lógica y sean comparables.

---

# 15. Plan experimental inicial

> Esta matriz es un **plan de partida**. Los valores pueden modificarse si la evidencia obtenida durante el proyecto lo justifica.

| ID | Variable | Valores iniciales |
|---|---|---|
| E0 | Baseline | Configuración inicial |
| E1 | Activación | ReLU / Tanh / Sigmoid |
| E2 | Loss | Categorical Crossentropy / MSE |
| E3 | Learning rate | 0.001 / 0.01 / 0.1 |
| E4 | Batch size | 32 / 128 / 512 |
| E5 | Capacidad | `[64]` / `[256,128]` / `[512,256,128]` |
| E6 | Optimizador | SGD / RMSProp / Adam |
| E7 | Dropout | 0 / 0.2 / 0.4 |
| E8 | Batch Normalization | OFF / ON |
| E9 | L2 | 0 / 1e-4 / 1e-3 |
| E10 | Early Stopping | Sin / Con |
| FINAL | Modelo seleccionado | Según evidencia |

---

# 16. Experimentos

## 16.1. E1 — Funciones de activación

Comparar:

- ReLU;
- Tanh;
- Sigmoid.

Constantes:

- arquitectura;
- optimizer;
- learning rate;
- batch size;
- epochs;
- loss.

Analizar:

- velocidad de convergencia;
- training loss;
- validation loss;
- training accuracy;
- validation accuracy;
- estabilidad.

---

## 16.2. E2 — Funciones de pérdida

Comparación inicial:

- Categorical Crossentropy;
- Mean Squared Error.

Constantes:

- arquitectura;
- activación;
- optimizer;
- learning rate;
- batch;
- epochs.

Objetivo:

- observar comportamiento de convergencia;
- evaluar pertinencia de la loss para clasificación multiclase.

> Binary Crossentropy no será utilizada como candidata principal porque el problema no es clasificación binaria.

---

## 16.3. E3 — Learning rate

Valores iniciales:

- 0.001;
- 0.01;
- 0.1.

Hipótesis:

```text
muy pequeño
→ convergencia lenta

adecuado
→ convergencia estable

muy grande
→ oscilaciones / divergencia
```

Si los valores iniciales no permiten observar claramente el fenómeno, se podrá agregar un stress test, por ejemplo:

- 0.5.

Ese cambio deberá quedar registrado en el Decision Log.

---

## 16.4. E4 — Batch size

Valores iniciales:

- 32;
- 128;
- 512.

Analizar:

- estabilidad;
- velocidad;
- convergencia;
- accuracy;
- loss;
- generalización.

---

## 16.5. E5 — Capacidad

Arquitecturas iniciales:

```text
Pequeña
[64]

Media
[256, 128]

Grande
[512, 256, 128]
```

Analizar:

- capacidad de ajuste;
- overfitting;
- train accuracy;
- validation accuracy;
- train loss;
- validation loss;
- gap de generalización.

---

## 16.6. E6 — Optimizadores

Comparar:

- SGD;
- RMSProp;
- Adam.

Primera comparación:

- misma arquitectura;
- misma activación;
- mismo batch;
- mismas épocas;
- learning rate controlado.

Después de seleccionar un optimizador candidato se podrá realizar retuning de learning rate si la evidencia lo justifica.

---

## 16.7. E7 — Dropout

Valores iniciales:

- 0;
- 0.2;
- 0.4.

Analizar especialmente:

- diferencia train-validation;
- validation loss;
- estabilidad;
- generalización.

No se espera necesariamente que Dropout maximice training accuracy.

---

## 16.8. E8 — Batch Normalization

Comparación:

```text
configuración candidata
vs
misma configuración + BatchNormalization
```

Analizar:

- convergencia;
- estabilidad;
- loss;
- accuracy.

---

## 16.9. E9 — L2

Valores iniciales:

- 0;
- 1e-4;
- 1e-3.

Objetivo:

- estudiar penalización de pesos;
- comparar generalización;
- observar posible reducción de overfitting.

---

## 16.10. E10 — Early Stopping

Se incorporará en una etapa avanzada, no necesariamente en los experimentos iniciales.

Configuración propuesta:

```python
EarlyStopping(
    monitor="val_loss",
    mode="min",
    patience=5,
    restore_best_weights=True
)
```

El máximo final puede ampliarse, por ejemplo, a 50 épocas, dejando que Early Stopping determine el punto de detención.

---

# 17. Registro estándar de experimentos

Cada entrenamiento debe registrar al menos:

| Campo |
|---|
| experiment_id |
| date |
| author |
| seed |
| hidden_layers |
| activation |
| output_activation |
| loss |
| optimizer |
| learning_rate |
| batch_size |
| dropout |
| batch_norm |
| l2 |
| max_epochs |
| epochs_executed |
| best_epoch |
| train_loss |
| val_loss |
| train_accuracy |
| val_accuracy |
| generalization_gap |
| precision_macro |
| recall_macro |
| f1_macro |
| observations |

---

# 18. Generalization gap

Se podrá usar como indicador auxiliar:

```text
generalization_gap =
train_accuracy - validation_accuracy
```

No será tratado como una métrica oficial de la pauta, sino como una herramienta de análisis para observar diferencias entre entrenamiento y validación.

---

# 19. Visualizaciones estándar

## 19.1. Por experimento

Siempre que sea pertinente:

1. Train Loss vs Validation Loss.
2. Train Accuracy vs Validation Accuracy.

## 19.2. Comparaciones

- Validation Accuracy por configuración.
- F1 Macro por configuración.
- Validation Loss por configuración.
- Generalization Gap por configuración.

## 19.3. Modelo final

- matriz de confusión absoluta;
- matriz de confusión normalizada;
- métricas por clase;
- ejemplos correctos;
- ejemplos incorrectos;
- predicciones de baja confianza.

---

# 20. Métricas

Métricas obligatorias:

- Accuracy;
- Precision;
- Recall;
- F1-Score.

Para Fashion-MNIST se reportará principalmente:

- Precision Macro;
- Recall Macro;
- F1 Macro.

Complementariamente:

- Precision Weighted;
- Recall Weighted;
- F1 Weighted.

También:

- `classification_report`.

---

# 21. Matriz de confusión

Se generarán:

1. matriz absoluta;
2. matriz normalizada.

Debe interpretarse, no solo mostrarse.

Ejemplo de análisis esperado:

> La clase Shirt presenta mayor confusión con T-shirt/top y Pullover, lo que sugiere que el modelo tiene dificultades para separar prendas con siluetas visualmente similares.

---

# 22. Predicciones visuales

Paneles sugeridos:

## Correctas

```text
Real: Sneaker
Predicho: Sneaker
Confianza: 97.3%
```

## Incorrectas

```text
Real: Shirt
Predicho: T-shirt/top
Confianza: 61.8%
```

## Baja confianza

Casos donde la probabilidad máxima sea relativamente baja.

Objetivo:

- conectar comportamiento cuantitativo con ejemplos visuales;
- aumentar impacto de la presentación;
- explicar errores.

---

# 23. Criterios para seleccionar el modelo final

No se seleccionará únicamente por Accuracy.

Se considerará:

- Validation Accuracy;
- Macro F1;
- Validation Loss;
- Generalization Gap;
- estabilidad;
- complejidad;
- número de parámetros;
- consistencia entre ejecuciones;
- interpretabilidad de los resultados.

Una diferencia mínima de accuracy puede no justificar un aumento importante de complejidad.

---

# 24. Evaluación final sobre test

Una vez seleccionada la configuración:

1. congelar decisiones;
2. reentrenar según protocolo definido;
3. evaluar en test;
4. calcular métricas finales;
5. generar matriz de confusión;
6. analizar errores;
7. no volver a ajustar el modelo usando test.

---

# 25. Estructura definitiva sugerida del notebook

```text
0. Portada e integrantes
1. Introducción
2. Objetivos
3. Descripción de Fashion-MNIST
4. Carga de datos
5. Exploración de datos
6. Preprocesamiento
7. División train / validation / test
8. Fundamento de la MLP
9. Hipótesis y justificación del baseline
10. Baseline
11. Experimento de activaciones
12. Experimento de pérdidas
13. Experimento de learning rate
14. Experimento de batch size
15. Experimento de capacidad
16. Experimento de optimizadores
17. Experimento de Dropout
18. Experimento de Batch Normalization
19. Experimento de L2
20. Early Stopping
21. Tabla global de resultados
22. Análisis y selección de configuración final
23. Reentrenamiento
24. Evaluación sobre test
25. Accuracy / Precision / Recall / F1
26. Matriz de confusión
27. Análisis por clase
28. Aciertos, errores y baja confianza
29. Conclusiones
30. Limitaciones y mejoras futuras
31. Referencias
```

---

# 26. Patrón Markdown para cada experimento

## Antes del código

### Objetivo

¿Qué variable se estudiará?

### Hipótesis

¿Qué esperamos observar y por qué?

### Variables controladas

¿Qué permanecerá constante?

### Variable independiente

¿Qué cambia?

### Evidencia a observar

¿Qué gráficos/métricas se utilizarán?

---

## Después del código

### Resultados

¿Qué ocurrió?

### Interpretación

¿Por qué puede haber ocurrido?

### Relación con teoría

¿Cómo conecta con EA1?

### Decisión

¿Qué se mantendrá o modificará?

### Próximo paso

¿Qué experimento sigue y por qué?

---

# 27. Decision Log

Archivo sugerido:

```text
docs/DECISION_LOG.md
```

Plantilla:

```markdown
## D-XX — Nombre de la decisión

**Fecha:**  
**Responsable:**  
**Estado:** propuesta / aceptada / descartada

### Situación

### Evidencia

### Hipótesis

### Acción

### Resultado

### Conclusión

### Impacto en el plan
```

Ejemplo:

```markdown
## D-07 — Agregar learning rate 0.5

### Situación
Los valores 0.001, 0.01 y 0.1 convergen de manera estable.

### Evidencia
Las curvas no muestran oscilaciones significativas.

### Hipótesis
Un LR mayor permitirá visualizar el límite de estabilidad.

### Acción
Agregar 0.5 como stress test.

### Resultado
Pendiente.

### Impacto
Se amplía E3.
```

---

# 28. Rubric Checklist

Archivo sugerido:

```text
docs/RUBRICA_CHECKLIST.md
```

Debe mapear cada indicador de la pauta con evidencia concreta.

Ejemplo:

```markdown
## IEE 1.1.3 — Experimentos controlados

- [ ] Learning rate: un parámetro por vez
- [ ] Batch size: un parámetro por vez
- [ ] Gráficos comparativos
- [ ] Tabla de resultados
- [ ] Markdown de análisis
- [ ] Justificación técnica
```

---

# 29. Repositorio GitHub

Estructura adoptada:

```text
EP1-FashionMNIST/
│
├── README.md
├── .gitignore
│
├── configs/
│   ├── README.md
│   └── baseline.json
│
├── data/
│   └── README.md
│
├── notebooks/
│   ├── README.md
│   ├── 01_ignacio_data_baseline.ipynb
│   ├── 02_lucas_hyperparameters.ipynb
│   ├── 03_cesar_optimization_evaluation.ipynb
│   └── EP1_FashionMNIST_FINAL.ipynb
│
├── src/
│   └── ep1_fashion_mnist/
│       ├── data.py
│       ├── modeling.py
│       ├── training.py
│       ├── experiments.py
│       ├── evaluation.py
│       └── visualization.py
│
├── tests/
│
├── results/
│   ├── figures/
│   ├── tables/
│   └── README.md
│
└── docs/
    ├── GUIA_MAESTRA_EP1_FashionMNIST.md
    ├── AUDITORIA_RUBRICA_EP1.md
    ├── DECISION_LOG.md
    ├── RUBRICA_CHECKLIST.md
    ├── COLLABORATION_WORKFLOW.md
    ├── collaborators/
    ├── handoffs/
    └── reviews/
```

Los módulos todavía inexistentes se crearán cuando su colaborador responsable implemente y pruebe el contrato correspondiente. Las dependencias se fijarán después de validar el entorno mínimo común; no se versionarán listas de paquetes especulativas.

---

# 30. Git workflow

Propuesta:

```text
main
└── develop
    ├── ignacio/...
    ├── lucas/...
    └── cesar/...
```

Flujo:

```text
feature branch
→ commit
→ push
→ pull request
→ revisión de compañero
→ merge a develop
→ validación
→ merge a main
```

## Regla para notebooks

No editar simultáneamente:

```text
EP1_FashionMNIST_FINAL.ipynb
```

Los conflictos de notebooks son difíciles de resolver.

La integración final será secuencial.

---

# 31. Distribución inicial de responsabilidades

> La distribución es inicial y puede reajustarse para mantener equidad.

Cada integrante debe mantener un informe técnico en `docs/collaborators/<nombre>/REPORT.md`. Todos los handoffs establecen **metas mínimas y orientativas, ampliables con justificación técnica**; no constituyen una lista exhaustiva ni inmutable. Todo cambio relevante debe quedar respaldado en el informe y, cuando afecte al alcance, al protocolo o al proyecto completo, en el Decision Log.

## Ignacio Silva

Responsabilidad principal:

- carga;
- exploración;
- preprocesamiento;
- baseline;
- activaciones;
- pérdida;
- L2.

## Lucas Moncada

Responsabilidad principal:

- infraestructura experimental;
- learning rate;
- batch size;
- capacidad;
- Early Stopping;
- tabla comparativa de hiperparámetros.

## Cesar Rojas

Responsabilidad principal:

- optimizadores;
- Dropout;
- Batch Normalization;
- métricas;
- matriz de confusión;
- análisis de errores;
- evaluación final.

---

# 32. Revisión cruzada

Propuesta:

```text
Ignacio revisa a Lucas
Lucas revisa a Cesar
Cesar revisa a Ignacio
```

Un bloque no se considera completo hasta que otro integrante pueda:

1. leerlo;
2. ejecutarlo;
3. explicar qué hace;
4. identificar sus supuestos;
5. defender sus resultados.

El trabajo avanzará mediante handoffs secuenciales:

```text
Ignacio -> Lucas -> Cesar -> integración grupal
```

Cada handoff debe declarar entradas, entregables, evidencia, asuntos abiertos y criterios de salida. El flujo completo se define en `docs/COLLABORATION_WORKFLOW.md` y los paquetes ejecutables se mantienen en `docs/handoffs/`.

El handoff orienta el trabajo y fija el mínimo necesario para una transición segura, pero no reemplaza el criterio técnico del colaborador ni la guía maestra como delimitante del alcance.

---

# 33. Conocimiento mínimo exigido a los tres

Todos deben poder explicar:

- qué es Deep Learning;
- qué es una MLP;
- qué hace una capa Dense;
- pesos;
- bias;
- forward propagation;
- función de pérdida;
- descenso del gradiente;
- backpropagation;
- learning rate;
- batch;
- época;
- activación;
- ReLU;
- Tanh;
- Sigmoid;
- Softmax;
- Crossentropy;
- SGD;
- RMSProp;
- Adam;
- desvanecimiento del gradiente;
- explosión del gradiente;
- overfitting;
- underfitting;
- generalización;
- Dropout;
- L2;
- Batch Normalization;
- Early Stopping;
- Accuracy;
- Precision;
- Recall;
- F1;
- matriz de confusión;
- train vs validation vs test;
- por qué se eligió la configuración final.

La respuesta:

> “Eso lo hizo mi compañero”

no debe existir durante la defensa.

---

# 34. Estrategia de presentación

La presentación debe contar una historia técnica.

```text
Problema
  ↓
Fashion-MNIST
  ↓
Baseline
  ↓
¿Qué cambia cuando modificamos cómo aprende?
  ↓
Experimentos
  ↓
Problemas observados
  ↓
Optimización / Regularización
  ↓
Modelo final
  ↓
Métricas
  ↓
Errores visuales
  ↓
Conclusiones
```

No se debe recorrer el notebook celda por celda.

Priorizar:

- curvas;
- tablas;
- matriz de confusión;
- predicciones visuales;
- decisiones;
- hallazgos.

---

# 35. Riesgos identificados

## R1 — Optimizar mirando test

Mitigación:

- test reservado hasta el final.

## R2 — Cambiar múltiples variables simultáneamente

Mitigación:

- experimentos controlados;
- registro de configuración.

## R3 — Diferencias entre computadores

Mitigación:

- semillas;
- versiones;
- entorno final común;
- registrar hardware cuando corresponda.

## R4 — Conflictos de `.ipynb`

Mitigación:

- notebooks individuales;
- integración secuencial;
- funciones compartidas en `src/`.

## R5 — Mucho código y poca explicación

Mitigación:

- Markdown antes y después de cada experimento.

## R6 — Buena accuracy pero poca comprensión

Mitigación:

- revisión cruzada;
- defensa técnica;
- preguntas entre integrantes.

## R7 — Sobreexperimentación

Mitigación:

- cada experimento debe responder una pregunta;
- no agregar pruebas sin propósito.

## R8 — Diferencias marginales interpretadas como conclusiones fuertes

Mitigación:

- analizar tendencias;
- repetir experimentos críticos si es necesario;
- evitar sobreinterpretar décimas mínimas.

---

# 36. Definición de terminado

El proyecto estará completo cuando exista evidencia de:

- [ ] Fashion-MNIST cargado correctamente.
- [ ] EDA documentado.
- [ ] Normalización justificada.
- [ ] Train / validation / test separados.
- [ ] Baseline justificado antes de entrenar.
- [ ] Activaciones comparadas.
- [ ] Pérdidas comparadas.
- [ ] Learning rates comparados.
- [ ] Batch sizes comparados.
- [ ] Capacidades comparadas.
- [ ] Optimizadores comparados.
- [ ] Dropout evaluado.
- [ ] BatchNorm evaluado.
- [ ] L2 evaluado.
- [ ] Early Stopping evaluado.
- [ ] Experimentos controlados.
- [ ] Curvas train / validation.
- [ ] Tabla maestra de resultados.
- [ ] Accuracy calculada.
- [ ] Precision calculada.
- [ ] Recall calculado.
- [ ] F1 calculado.
- [ ] Matriz de confusión.
- [ ] Métricas por clase.
- [ ] Análisis visual de errores.
- [ ] Modelo final justificado con evidencia.
- [ ] Test usado solo al final.
- [ ] Conclusiones técnicas.
- [ ] Limitaciones.
- [ ] Código modularizado.
- [ ] Markdown suficiente.
- [ ] README de ejecución.
- [ ] Commits reales de los tres.
- [ ] PR/revisión cruzada.
- [x] Notebook final ejecutado correctamente en Colab sin repetir F1 ni consultar test.
- [ ] Los tres pueden defender todo el proyecto.
- [ ] Presentación construida desde hallazgos.
- [x] Autorización de grupo de tres confirmada.

---

# 37. Control de cambios de esta guía

## v0.1

Definición inicial:

- Fashion-MNIST seleccionado;
- enfoque experimental definido;
- protocolo train/validation/test;
- baseline propuesto;
- experimentos iniciales;
- metodología de justificación;
- distribución inicial de responsabilidades;
- flujo Git;
- criterios de finalización.

## v0.2

- grupo de tres confirmado;
- Colab definido como entorno final de validación y entrega;
- auditoría de alineación con la rúbrica incorporada;
- Decision Log y Rubric Checklist incorporados.

## v0.3

- documentación obligatoria por colaborador;
- metas flexibles y criterios verificables de salida;
- handoffs secuenciales Ignacio, Lucas y Cesar;
- arquitectura mínima del repositorio definida;
- material docente, datos y artefactos pesados excluidos de Git.

## v0.4

- repositorio oficial de Fashion-MNIST revisado;
- contrato de datos verificable incorporado;
- checksums, cabeceras IDX, balance y duplicados exactos documentados;
- validadores automáticos de splits y particiones incorporados;
- handoff de Ignacio actualizado con evidencia y comandos concretos.

## v0.5

- `uv venv` definido como regla obligatoria del repositorio;
- uso de Python global y otros administradores de entorno prohibido;
- política de dependencias, lock y evidencia por colaborador documentada;
- handoffs actualizados para exigir el mismo entorno reproducible.

## v0.6

- Python 3.12.x fijado como versión oficial y `.python-version` incorporado;
- comando único de creación del entorno definido;
- compatibilidad con TensorFlow y Colab documentada;
- ruta de GPU mediante WSL2 distinguida de la ejecución CPU nativa de Windows.

## v0.7

- naturaleza flexible de todos los handoffs explicitada;
- metas definidas como mínimas, orientativas y ampliables con justificación técnica;
- guía maestra reafirmada como delimitante del alcance ante ampliaciones o reajustes.

---

# 38. Principio final

> El objetivo no es encontrar una configuración “perfecta” desde el comienzo.

El objetivo es demostrar un proceso técnico:

```text
observar
→ formular hipótesis
→ experimentar
→ medir
→ interpretar
→ decidir
→ justificar
```

Si los resultados contradicen una hipótesis inicial, eso no representa un error del proyecto.

Representa evidencia.

Y esa evidencia debe utilizarse para modificar razonadamente el plan.
