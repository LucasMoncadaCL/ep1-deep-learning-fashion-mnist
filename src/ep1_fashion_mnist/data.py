"""Carga y preprocesamiento reproducible de Fashion-MNIST."""

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np
from sklearn.model_selection import train_test_split

from ep1_fashion_mnist.data_validation import (
    PartitionSummary,
    SplitSummary,
    validate_image_classification_split,
    validate_train_validation_partition,
)

SEED = 42
CLASS_NAMES = (
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
)


@dataclass(frozen=True)
class FashionMnistData:
    """Particiones procesadas, con el test oficial preservado para el final."""

    X_train: np.ndarray
    X_val: np.ndarray
    X_test: np.ndarray
    y_train: np.ndarray
    y_val: np.ndarray
    y_test: np.ndarray
    train_indices: np.ndarray
    validation_indices: np.ndarray
    train_summary: SplitSummary
    test_summary: SplitSummary
    partition_summary: PartitionSummary


def load_fashion_mnist_raw() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Carga los arrays oficiales sin transformar mediante TensorFlow/Keras."""
    from tensorflow import keras

    (X_train_full, y_train_full), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
    return X_train_full, y_train_full, X_test, y_test


def normalize_images(images: np.ndarray) -> np.ndarray:
    """Convierte píxeles uint8 a float32 en el intervalo cerrado [0, 1]."""
    normalized = images.astype(np.float32) / 255.0
    if normalized.dtype != np.float32 or normalized.size == 0:
        raise ValueError("La normalización debe producir un array float32 no vacío")
    if float(normalized.min()) < 0.0 or float(normalized.max()) > 1.0:
        raise ValueError("La normalización produjo píxeles fuera de [0, 1]")
    return normalized


def one_hot_encode(labels: np.ndarray, *, num_classes: int = 10) -> np.ndarray:
    """Codifica etiquetas enteras para Softmax + categorical crossentropy."""
    if labels.ndim != 1 or not np.issubdtype(labels.dtype, np.integer):
        raise ValueError("Las etiquetas deben ser un vector de enteros")
    if labels.size == 0 or int(labels.min()) < 0 or int(labels.max()) >= num_classes:
        raise ValueError("Las etiquetas están fuera del rango de clases esperado")
    return np.eye(num_classes, dtype=np.float32)[labels]


def prepare_fashion_mnist(
    *,
    seed: int = SEED,
    validation_fraction: float = 0.1,
    loader: Callable[[], tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]] = load_fashion_mnist_raw,
) -> FashionMnistData:
    """Valida, divide y normaliza Fashion-MNIST sin tocar el test oficial."""
    if not 0.0 < validation_fraction < 1.0:
        raise ValueError("validation_fraction debe estar entre 0 y 1")

    X_full, y_full, X_test_raw, y_test = loader()
    train_summary = validate_image_classification_split(
        X_full, y_full, split_name="official_train", expected_count=60_000,
        expected_image_shape=(28, 28), expected_num_classes=10,
        expected_per_class=6_000, require_full_uint8_range=True,
    )
    test_summary = validate_image_classification_split(
        X_test_raw, y_test, split_name="official_test", expected_count=10_000,
        expected_image_shape=(28, 28), expected_num_classes=10,
        expected_per_class=1_000, require_full_uint8_range=True,
    )
    indices = np.arange(X_full.shape[0])
    train_indices, validation_indices = train_test_split(
        indices, test_size=validation_fraction, random_state=seed, stratify=y_full,
    )
    partition_summary = validate_train_validation_partition(
        train_indices, validation_indices, source_count=X_full.shape[0],
    )
    return FashionMnistData(
        X_train=normalize_images(X_full[train_indices]),
        X_val=normalize_images(X_full[validation_indices]),
        X_test=normalize_images(X_test_raw),
        y_train=one_hot_encode(y_full[train_indices]),
        y_val=one_hot_encode(y_full[validation_indices]),
        y_test=one_hot_encode(y_test),
        train_indices=train_indices,
        validation_indices=validation_indices,
        train_summary=train_summary,
        test_summary=test_summary,
        partition_summary=partition_summary,
    )
