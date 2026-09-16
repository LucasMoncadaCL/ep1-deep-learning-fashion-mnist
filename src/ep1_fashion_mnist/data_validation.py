"""Validaciones explícitas para proteger el contrato de Fashion-MNIST."""

from dataclasses import dataclass

import numpy as np


class DataContractError(ValueError):
    """Indica que datos o particiones incumplen el contrato declarado."""


@dataclass(frozen=True)
class SplitSummary:
    """Resumen verificable de un split de clasificación de imágenes."""

    name: str
    count: int
    image_shape: tuple[int, ...]
    image_dtype: str
    label_dtype: str
    pixel_range: tuple[int, int]
    class_counts: dict[int, int]


@dataclass(frozen=True)
class PartitionSummary:
    """Resumen de una partición completa y disjunta de índices."""

    source_count: int
    train_count: int
    validation_count: int


def validate_image_classification_split(
    images: np.ndarray,
    labels: np.ndarray,
    *,
    split_name: str,
    expected_count: int,
    expected_image_shape: tuple[int, ...],
    expected_num_classes: int,
    expected_per_class: int | None = None,
    require_full_uint8_range: bool = False,
) -> SplitSummary:
    """Valida estructura, tipos, rango y distribución de un split crudo."""

    if not isinstance(images, np.ndarray) or not isinstance(labels, np.ndarray):
        raise DataContractError(f"{split_name}: images y labels deben ser arrays de NumPy")

    expected_images_shape = (expected_count, *expected_image_shape)
    if images.shape != expected_images_shape:
        raise DataContractError(
            f"{split_name}: forma de imágenes {images.shape}; esperada {expected_images_shape}"
        )
    if labels.shape != (expected_count,):
        raise DataContractError(
            f"{split_name}: forma de etiquetas {labels.shape}; esperada {(expected_count,)}"
        )
    if images.dtype != np.uint8:
        raise DataContractError(
            f"{split_name}: dtype de imágenes {images.dtype}; esperado uint8"
        )
    if not np.issubdtype(labels.dtype, np.integer):
        raise DataContractError(
            f"{split_name}: dtype de etiquetas {labels.dtype}; se esperaba un entero"
        )

    pixel_min = int(images.min())
    pixel_max = int(images.max())
    if require_full_uint8_range and (pixel_min, pixel_max) != (0, 255):
        raise DataContractError(
            f"{split_name}: rango {(pixel_min, pixel_max)}; se esperaba (0, 255)"
        )

    unique_labels, counts = np.unique(labels, return_counts=True)
    class_counts = {
        int(label): int(count) for label, count in zip(unique_labels, counts, strict=True)
    }
    expected_labels = set(range(expected_num_classes))
    if set(class_counts) != expected_labels:
        raise DataContractError(
            f"{split_name}: clases {sorted(class_counts)}; esperadas {sorted(expected_labels)}"
        )
    if expected_per_class is not None:
        unexpected_counts = {
            label: count
            for label, count in class_counts.items()
            if count != expected_per_class
        }
        if unexpected_counts:
            raise DataContractError(
                f"{split_name}: distribución inesperada {unexpected_counts}; "
                f"se esperaban {expected_per_class} ejemplos por clase"
            )

    return SplitSummary(
        name=split_name,
        count=expected_count,
        image_shape=expected_image_shape,
        image_dtype=str(images.dtype),
        label_dtype=str(labels.dtype),
        pixel_range=(pixel_min, pixel_max),
        class_counts=class_counts,
    )


def validate_train_validation_partition(
    train_indices: np.ndarray,
    validation_indices: np.ndarray,
    *,
    source_count: int,
) -> PartitionSummary:
    """Comprueba que train y validation particionen exactamente el origen."""

    for name, indices in (
        ("train_indices", train_indices),
        ("validation_indices", validation_indices),
    ):
        if not isinstance(indices, np.ndarray):
            raise DataContractError(f"{name} debe ser un array de NumPy")
        if indices.ndim != 1 or not np.issubdtype(indices.dtype, np.integer):
            raise DataContractError(f"{name} debe ser un vector de índices enteros")
        if indices.size == 0:
            raise DataContractError(f"{name} no puede estar vacío")
        if np.unique(indices).size != indices.size:
            raise DataContractError(f"{name} contiene índices duplicados")
        if int(indices.min()) < 0 or int(indices.max()) >= source_count:
            raise DataContractError(
                f"{name} contiene índices fuera del rango [0, {source_count})"
            )

    overlap = np.intersect1d(train_indices, validation_indices)
    if overlap.size:
        raise DataContractError(
            f"train y validation presentan solapamiento en {overlap.size} índices"
        )

    combined = np.concatenate((train_indices, validation_indices))
    if combined.size != source_count or not np.array_equal(
        np.sort(combined), np.arange(source_count)
    ):
        raise DataContractError(
            "train y validation no forman una partición completa del conjunto de origen"
        )

    return PartitionSummary(
        source_count=source_count,
        train_count=int(train_indices.size),
        validation_count=int(validation_indices.size),
    )
