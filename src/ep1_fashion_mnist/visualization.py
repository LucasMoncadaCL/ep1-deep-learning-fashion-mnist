"""Visualizaciones reproducibles para exploración y evidencia experimental."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def _class_ids(labels: np.ndarray) -> np.ndarray:
    return labels.argmax(axis=1) if labels.ndim == 2 else labels


def plot_sample_grid(
    images: np.ndarray,
    labels: np.ndarray,
    class_names: tuple[str, ...],
    *,
    count: int = 25,
    output_path: str | Path | None = None,
) -> None:
    """Crea una cuadrícula determinista de imágenes etiquetadas."""
    if count <= 0 or count > images.shape[0]:
        raise ValueError("count debe estar entre 1 y el número de imágenes")
    side = int(np.ceil(np.sqrt(count)))
    ids = _class_ids(labels)
    figure, axes = plt.subplots(side, side, figsize=(10, 10))
    for axis, image, class_id in zip(axes.flat, images[:count], ids[:count], strict=False):
        axis.imshow(image, cmap="gray", vmin=0, vmax=1)
        axis.set_title(class_names[int(class_id)], fontsize=8)
        axis.axis("off")
    for axis in axes.flat[count:]:
        axis.axis("off")
    figure.suptitle("Fashion-MNIST — ejemplos de train", y=0.99)
    figure.tight_layout(rect=(0, 0, 1, 0.96))
    if output_path:
        figure.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(figure)


def plot_class_distribution(
    labels: np.ndarray,
    class_names: tuple[str, ...],
    *,
    output_path: str | Path | None = None,
) -> None:
    """Grafica la cantidad de ejemplos por clase de una partición."""
    ids = _class_ids(labels)
    counts = np.bincount(ids, minlength=len(class_names))
    figure, axis = plt.subplots(figsize=(10, 4.5))
    axis.bar(class_names, counts)
    axis.set(title="Fashion-MNIST — distribución de clases en train", ylabel="Ejemplos")
    axis.tick_params(axis="x", rotation=35)
    axis.grid(axis="y", alpha=0.25)
    figure.tight_layout()
    if output_path:
        figure.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(figure)
