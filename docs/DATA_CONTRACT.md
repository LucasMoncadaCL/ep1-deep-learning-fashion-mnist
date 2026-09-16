# Contrato de datos - Fashion-MNIST

## 1. Propósito

Este contrato define qué datos utiliza el proyecto, qué propiedades fueron verificadas y qué invariantes debe proteger el código. Su objetivo es impedir que distintas implementaciones carguen, transformen o dividan Fashion-MNIST de manera incompatible.

## 2. Fuente y alcance de la revisión

- Repositorio oficial: `https://github.com/zalandoresearch/fashion-mnist`.
- Rama revisada: `master`.
- Commit revisado: `b2617bb6d3ffa2e429640350f613e3291e10b141`.
- Fecha de verificación del proyecto: 2026-09-15.
- Licencia del repositorio: MIT.

Se revisó el árbol completo del repositorio, el código funcional, la documentación y los cuatro archivos IDX comprimidos. Los binarios fueron descomprimidos y analizados directamente; no se infirieron sus propiedades únicamente desde el README.

## 3. Evidencia verificada

### 3.1. Archivos oficiales

| Archivo | Registros | Bytes comprimidos | MD5 verificado |
|---|---:|---:|---|
| `train-images-idx3-ubyte.gz` | 60.000 imágenes | 26.421.880 | `8d4fb7e6c68d591d4c3dfef9ec88bf0d` |
| `train-labels-idx1-ubyte.gz` | 60.000 etiquetas | 29.515 | `25c81989df183df01b3e8a0aad5dffbe` |
| `t10k-images-idx3-ubyte.gz` | 10.000 imágenes | 4.422.102 | `bef4ecab320f06d8554ea6380940ec79` |
| `t10k-labels-idx1-ubyte.gz` | 10.000 etiquetas | 5.148 | `bb300cfdad3c16e7a12a480ee83cd310` |

### 3.2. Cabeceras IDX

| Archivo lógico | Magic number | Cantidad | Filas | Columnas |
|---|---:|---:|---:|---:|
| Imágenes train | 2051 | 60.000 | 28 | 28 |
| Etiquetas train | 2049 | 60.000 | - | - |
| Imágenes test | 2051 | 10.000 | 28 | 28 |
| Etiquetas test | 2049 | 10.000 | - | - |

### 3.3. Arrays crudos

| Array | Forma | dtype |
|---|---|---|
| `X_train_full` | `(60000, 28, 28)` | `uint8` |
| `y_train_full` | `(60000,)` | `uint8` |
| `X_test` | `(10000, 28, 28)` | `uint8` |
| `y_test` | `(10000,)` | `uint8` |

- Rango de píxeles: `[0, 255]`.
- Media train: aproximadamente `72,9404`.
- Desviación estándar train: aproximadamente `90,0212`.
- Media test: aproximadamente `73,1466`.
- Desviación estándar test: aproximadamente `89,8733`.

Estas estadísticas describen los archivos oficiales revisados. No son parámetros de normalización del proyecto: la transformación inicial acordada continúa siendo división por 255.

### 3.4. Distribución de clases

| ID | Clase | Train oficial | Test oficial |
|---:|---|---:|---:|
| 0 | T-shirt/top | 6.000 | 1.000 |
| 1 | Trouser | 6.000 | 1.000 |
| 2 | Pullover | 6.000 | 1.000 |
| 3 | Dress | 6.000 | 1.000 |
| 4 | Coat | 6.000 | 1.000 |
| 5 | Sandal | 6.000 | 1.000 |
| 6 | Shirt | 6.000 | 1.000 |
| 7 | Sneaker | 6.000 | 1.000 |
| 8 | Bag | 6.000 | 1.000 |
| 9 | Ankle boot | 6.000 | 1.000 |

El dataset está perfectamente balanceado en ambos splits oficiales.

### 3.5. Duplicados exactos

Se comparó el SHA-256 del contenido de cada imagen:

- grupos duplicados dentro de train: `0`;
- grupos duplicados dentro de test: `0`;
- imágenes idénticas presentes en train y test: `0`.

Esto descarta duplicados exactos, no similitud visual ni posibles ambigüedades semánticas.

## 4. Carga adoptada

La carga principal utilizará la API moderna incluida en TensorFlow/Keras:

```python
from tensorflow import keras

(X_train_full, y_train_full), (X_test, y_test) = (
    keras.datasets.fashion_mnist.load_data()
)
```

No se clonará el repositorio de Zalando durante la ejecución y no se versionarán copias de los datos. El loader IDX de Zalando queda como referencia del formato, no como dependencia del proyecto.

## 5. Política de particiones

Los splits tienen responsabilidades diferentes:

```text
train oficial (60.000)
    -> train del proyecto (54.000)
    -> validation del proyecto (6.000)

test oficial (10.000)
    -> test final sellado
```

La división train/validation debe usar:

- índices derivados únicamente del train oficial;
- `test_size=0.10`;
- `random_state=42`;
- `stratify=y_train_full`.

Con esas condiciones se esperan 5.400 ejemplos por clase en train y 600 por clase en validation.

### Prohibición

No se puede usar test para:

- escoger arquitectura;
- seleccionar funciones;
- ajustar hiperparámetros;
- decidir regularización;
- elegir época;
- descartar configuraciones.

Test se evalúa después de congelar el protocolo y la configuración final.

## 6. Estados de representación

### 6.1. Estado crudo

```text
images: uint8, (N, 28, 28), [0, 255]
labels: enteros, (N,), [0, 9]
```

### 6.2. Estado normalizado

```python
X = X.astype("float32") / 255.0
```

Resultado esperado:

```text
images: float32, (N, 28, 28), [0.0, 1.0]
```

### 6.3. Entrada de la MLP

La transformación a 784 características debe realizarse con una capa `Flatten` del modelo, salvo que una decisión posterior justifique explícitamente otro contrato.

### 6.4. Etiquetas del baseline

El baseline propone one-hot encoding junto con:

- salida Softmax de diez unidades;
- `categorical_crossentropy`.

Si se cambia a etiquetas enteras, la pérdida coherente sería `sparse_categorical_crossentropy`. No se puede cambiar una de estas piezas sin revisar las otras.

## 7. Validaciones automatizadas

El módulo `src/ep1_fashion_mnist/data_validation.py` ofrece:

- `validate_image_classification_split(...)`;
- `validate_train_validation_partition(...)`.

Uso mínimo sobre los splits oficiales:

```python
from ep1_fashion_mnist.data_validation import (
    validate_image_classification_split,
)

train_summary = validate_image_classification_split(
    X_train_full,
    y_train_full,
    split_name="official_train",
    expected_count=60_000,
    expected_image_shape=(28, 28),
    expected_num_classes=10,
    expected_per_class=6_000,
    require_full_uint8_range=True,
)

test_summary = validate_image_classification_split(
    X_test,
    y_test,
    split_name="official_test",
    expected_count=10_000,
    expected_image_shape=(28, 28),
    expected_num_classes=10,
    expected_per_class=1_000,
    require_full_uint8_range=True,
)
```

Después de generar índices train/validation:

```python
from ep1_fashion_mnist.data_validation import (
    validate_train_validation_partition,
)

partition_summary = validate_train_validation_partition(
    train_indices,
    validation_indices,
    source_count=60_000,
)
```

Comando actual de pruebas:

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m unittest tests.test_data_validation -v
```

El `.venv` debe haber sido creado con `uv venv`, según `docs/ENVIRONMENT.md`.

## 8. Evidencia que debe producir Ignacio

Ignacio debe dejar respaldados:

1. summaries devueltos por las validaciones;
2. conteos por clase después del split;
3. seed y parámetros exactos del split;
4. demostración de que train y validation son disjuntos y cubren el train oficial;
5. código de normalización y verificación del nuevo rango/dtype;
6. cuadrícula visual etiquetada;
7. distribución por clase;
8. explicación de por qué test permanece sellado.

## 9. Límites del contrato

Este documento no demuestra que:

- una arquitectura sea óptima;
- una función produzca mejor convergencia;
- una técnica de regularización sea necesaria;
- una clase sea más difícil que otra.

Esas conclusiones requieren experimentos del proyecto.
