"""Ejecución reproducible de experimentos de validation para Fashion-MNIST."""

import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from ep1_fashion_mnist.data import prepare_fashion_mnist
from ep1_fashion_mnist.model import build_mlp, compile_model


@dataclass(frozen=True)
class ValidationMetrics:
    """Métricas agregadas de una ejecución sobre validation, nunca sobre test."""

    accuracy: float
    precision_weighted: float
    recall_weighted: float
    f1_weighted: float


def load_config(config_path: str | Path) -> dict:
    """Carga una configuración JSON y comprueba los campos mínimos de un experimento."""
    with Path(config_path).open(encoding="utf-8") as config_file:
        config = json.load(config_file)
    required = {
        "experiment_id", "seed", "validation_fraction", "hidden_layers",
        "hidden_activation", "dropout", "batch_normalization", "l2_strength",
        "optimizer", "learning_rate", "loss", "batch_size", "epochs",
        "output_units", "output_activation", "label_encoding",
    }
    missing = required.difference(config)
    if missing:
        raise ValueError(f"Configuración incompleta; faltan: {', '.join(sorted(missing))}")
    if config["output_units"] != 10 or config["output_activation"] != "softmax":
        raise ValueError("La configuración requiere 10 salidas Softmax para Fashion-MNIST")
    if config["label_encoding"] != "one_hot":
        raise ValueError("El pipeline actual requiere etiquetas one-hot")
    if config["loss"] not in {"categorical_crossentropy", "mse"}:
        raise ValueError("La loss debe ser categorical_crossentropy o mse en este pipeline")
    return config


def set_reproducible_seed(seed: int) -> None:
    """Fija las semillas del proceso antes de construir y entrenar un modelo."""
    import tensorflow as tf

    random.seed(seed)
    np.random.seed(seed)
    tf.keras.utils.set_random_seed(seed)


def plot_history(history: dict[str, list[float]], *, experiment_id: str, output_path: Path) -> None:
    """Guarda curvas de loss y accuracy claramente identificadas."""
    epochs = range(1, len(history["loss"]) + 1)
    figure, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    for axis, metric, title in (
        (axes[0], "loss", "Pérdida"),
        (axes[1], "accuracy", "Accuracy"),
    ):
        axis.plot(epochs, history[metric], label="train")
        axis.plot(epochs, history[f"val_{metric}"], label="validation")
        axis.set(title=title, xlabel="Época", ylabel=title)
        axis.legend()
        axis.grid(alpha=0.25)
    figure.suptitle(f"{experiment_id} — curvas de entrenamiento")
    figure.tight_layout()
    figure.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(figure)


def plot_validation_comparison(
    histories: dict[str, str | Path], *, metric: str, output_path: str | Path
) -> None:
    """Compara una métrica de validation desde historiales CSV identificados."""
    figure, axis = plt.subplots(figsize=(8, 4.5))
    for experiment_id, history_path in histories.items():
        history = pd.read_csv(history_path)
        axis.plot(history["epoch"] + 1, history[f"val_{metric}"], label=experiment_id)
    axis.set(xlabel="Época", ylabel=f"Validation {metric}")
    figure.suptitle(f"Comparación de validation — {metric}")
    axis.legend()
    axis.grid(alpha=0.25)
    figure.tight_layout(rect=(0, 0, 1, 0.95))
    figure.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(figure)


def run_validation_experiment(
    config_path: str | Path,
    *,
    output_directory: str | Path,
) -> ValidationMetrics:
    """Entrena una configuración y guarda solo evidencia basada en validation."""
    config = load_config(config_path)
    experiment_id = config["experiment_id"]
    set_reproducible_seed(config["seed"])
    data = prepare_fashion_mnist(
        seed=config["seed"], validation_fraction=config["validation_fraction"]
    )
    model = compile_model(
        build_mlp(
            config["hidden_layers"], hidden_activation=config["hidden_activation"],
            dropout=config["dropout"], batch_normalization=config["batch_normalization"],
            l2_strength=config["l2_strength"], seed=config["seed"],
        ),
        optimizer=config["optimizer"], learning_rate=config["learning_rate"], loss=config["loss"],
    )
    history = model.fit(
        data.X_train, data.y_train, validation_data=(data.X_val, data.y_val),
        batch_size=config["batch_size"], epochs=config["epochs"], verbose=2,
    ).history
    probabilities = model.predict(data.X_val, verbose=0)
    actual = data.y_val.argmax(axis=1)
    predicted = probabilities.argmax(axis=1)
    metrics = ValidationMetrics(
        accuracy=float(accuracy_score(actual, predicted)),
        precision_weighted=float(precision_score(actual, predicted, average="weighted", zero_division=0)),
        recall_weighted=float(recall_score(actual, predicted, average="weighted", zero_division=0)),
        f1_weighted=float(f1_score(actual, predicted, average="weighted", zero_division=0)),
    )
    output_path = Path(output_directory)
    output_path.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(history).rename_axis("epoch").to_csv(output_path / f"{experiment_id}_history.csv")
    with (output_path / f"{experiment_id}_validation_metrics.json").open("w", encoding="utf-8") as metrics_file:
        json.dump({"experiment_id": experiment_id, "model_parameters": model.count_params(),
                   "metrics": asdict(metrics)}, metrics_file, indent=2)
    plot_history(history, experiment_id=experiment_id, output_path=output_path / f"{experiment_id}_curves.png")
    return metrics
