"""Ejecución reproducible de experimentos de validation para Fashion-MNIST."""

import json
import random
from argparse import ArgumentParser
from dataclasses import asdict, dataclass
from pathlib import Path
from time import perf_counter

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
    precision_macro: float
    recall_macro: float
    f1_macro: float
    precision_weighted: float
    recall_weighted: float
    f1_weighted: float


@dataclass(frozen=True)
class TrainingSummary:
    """Resumen de convergencia y costo calculado únicamente desde el historial."""

    duration_seconds: float
    epochs_completed: int
    best_epoch_by_validation_loss: int
    best_validation_loss: float
    best_epoch_by_validation_accuracy: int
    best_validation_accuracy: float
    final_train_loss: float
    final_validation_loss: float
    final_train_accuracy: float
    final_validation_accuracy: float
    final_accuracy_gap: float
    final_loss_gap: float


def validate_config(config: dict) -> dict:
    """Valida anticipadamente el contrato estructural y numérico de una corrida."""
    required = {
        "experiment_id", "dataset", "input_shape", "stratified_split",
        "seed", "validation_fraction", "hidden_layers",
        "hidden_activation", "dropout", "batch_normalization", "l2_strength",
        "optimizer", "learning_rate", "loss", "batch_size", "epochs",
        "output_units", "output_activation", "label_encoding", "early_stopping",
    }
    missing = required.difference(config)
    if missing:
        raise ValueError(f"Configuración incompleta; faltan: {', '.join(sorted(missing))}")
    if not isinstance(config["experiment_id"], str):
        raise TypeError("experiment_id debe ser texto")
    if not config["experiment_id"].strip():
        raise ValueError("experiment_id debe ser un texto no vacío")
    if config["dataset"] != "fashion_mnist":
        raise ValueError("dataset debe ser fashion_mnist")
    if config["input_shape"] != [28, 28]:
        raise ValueError("input_shape debe ser [28, 28]")
    if config["stratified_split"] is not True:
        raise ValueError("stratified_split debe ser true")
    if not isinstance(config["seed"], int) or isinstance(config["seed"], bool):
        raise TypeError("seed debe ser un entero")
    if not isinstance(config["validation_fraction"], (int, float)) or isinstance(
        config["validation_fraction"], bool
    ):
        raise TypeError("validation_fraction debe ser numérico")
    if not 0.0 < config["validation_fraction"] < 1.0:
        raise ValueError("validation_fraction debe estar entre 0 y 1")
    if not isinstance(config["hidden_layers"], list):
        raise TypeError("hidden_layers debe ser una lista")
    if any(
        not isinstance(units, int) or isinstance(units, bool)
        for units in config["hidden_layers"]
    ):
        raise TypeError("hidden_layers debe contener enteros")
    if not config["hidden_layers"] or any(units <= 0 for units in config["hidden_layers"]):
        raise ValueError("hidden_layers debe ser una lista no vacía de enteros positivos")
    if not isinstance(config["learning_rate"], (int, float)) or isinstance(
        config["learning_rate"], bool
    ):
        raise TypeError("learning_rate debe ser numérico")
    if config["learning_rate"] <= 0:
        raise ValueError("learning_rate debe ser positivo")
    for field in ("batch_size", "epochs"):
        if not isinstance(config[field], int) or isinstance(config[field], bool):
            raise TypeError(f"{field} debe ser un entero")
        if config[field] <= 0:
            raise ValueError(f"{field} debe ser un entero positivo")
    if not isinstance(config["dropout"], (int, float)) or isinstance(
        config["dropout"], bool
    ):
        raise TypeError("dropout debe ser numérico")
    if not 0.0 <= config["dropout"] < 1.0:
        raise ValueError("dropout debe estar en [0, 1)")
    if not isinstance(config["l2_strength"], (int, float)) or isinstance(
        config["l2_strength"], bool
    ):
        raise TypeError("l2_strength debe ser numérico")
    if config["l2_strength"] < 0:
        raise ValueError("l2_strength no puede ser negativo")
    for field in ("batch_normalization", "early_stopping"):
        if not isinstance(config[field], bool):
            raise TypeError(f"{field} debe ser booleano")
    if config["early_stopping"]:
        raise NotImplementedError(
            "Early Stopping aún no está implementado en el ejecutor; "
            "no se acepta una configuración que lo declare activo"
        )
    if config["output_units"] != 10 or config["output_activation"] != "softmax":
        raise ValueError("La configuración requiere 10 salidas Softmax para Fashion-MNIST")
    if config["label_encoding"] != "one_hot":
        raise ValueError("El pipeline actual requiere etiquetas one-hot")
    if config["loss"] not in {"categorical_crossentropy", "mse"}:
        raise ValueError("La loss debe ser categorical_crossentropy o mse en este pipeline")
    if str(config["optimizer"]).lower() not in {"sgd", "adam", "rmsprop"}:
        raise ValueError("optimizer debe ser sgd, adam o rmsprop")
    return config


def load_config(config_path: str | Path) -> dict:
    """Carga una configuración JSON y valida el contrato del experimento."""
    with Path(config_path).open(encoding="utf-8") as config_file:
        config = json.load(config_file)
    return validate_config(config)


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


def calculate_validation_metrics(actual: np.ndarray, predicted: np.ndarray) -> ValidationMetrics:
    """Calcula métricas macro y ponderadas sin consultar el conjunto de test.

    Las macro dan el mismo peso a cada clase; las ponderadas conservan el peso de
    su soporte. Ambas se registran para que el contrato de resultados sea explícito.
    """
    return ValidationMetrics(
        accuracy=float(accuracy_score(actual, predicted)),
        precision_macro=float(precision_score(actual, predicted, average="macro", zero_division=0)),
        recall_macro=float(recall_score(actual, predicted, average="macro", zero_division=0)),
        f1_macro=float(f1_score(actual, predicted, average="macro", zero_division=0)),
        precision_weighted=float(precision_score(actual, predicted, average="weighted", zero_division=0)),
        recall_weighted=float(recall_score(actual, predicted, average="weighted", zero_division=0)),
        f1_weighted=float(f1_score(actual, predicted, average="weighted", zero_division=0)),
    )


def summarize_training_history(
    history: dict[str, list[float]], *, duration_seconds: float
) -> TrainingSummary:
    """Resume convergencia, costo y gaps finales de un entrenamiento."""
    required_metrics = ("loss", "val_loss", "accuracy", "val_accuracy")
    missing = [metric for metric in required_metrics if metric not in history]
    if missing:
        raise ValueError(f"Historial incompleto; faltan: {', '.join(missing)}")
    lengths = {len(history[metric]) for metric in required_metrics}
    if lengths == {0} or len(lengths) != 1:
        raise ValueError("Las series del historial deben ser no vacías y tener igual longitud")
    if duration_seconds < 0:
        raise ValueError("La duración del entrenamiento no puede ser negativa")

    best_loss_index = int(np.argmin(history["val_loss"]))
    best_accuracy_index = int(np.argmax(history["val_accuracy"]))
    final_train_loss = float(history["loss"][-1])
    final_validation_loss = float(history["val_loss"][-1])
    final_train_accuracy = float(history["accuracy"][-1])
    final_validation_accuracy = float(history["val_accuracy"][-1])
    return TrainingSummary(
        duration_seconds=float(duration_seconds),
        epochs_completed=lengths.pop(),
        best_epoch_by_validation_loss=best_loss_index + 1,
        best_validation_loss=float(history["val_loss"][best_loss_index]),
        best_epoch_by_validation_accuracy=best_accuracy_index + 1,
        best_validation_accuracy=float(history["val_accuracy"][best_accuracy_index]),
        final_train_loss=final_train_loss,
        final_validation_loss=final_validation_loss,
        final_train_accuracy=final_train_accuracy,
        final_validation_accuracy=final_validation_accuracy,
        final_accuracy_gap=final_train_accuracy - final_validation_accuracy,
        final_loss_gap=final_validation_loss - final_train_loss,
    )


def build_experiment_record(
    *,
    config: dict,
    model_parameters: int,
    metrics: ValidationMetrics,
    training: TrainingSummary,
) -> dict:
    """Construye el registro autocontenido que se persiste para comparar corridas."""
    return {
        "experiment_id": config["experiment_id"],
        "config": dict(config),
        "model_parameters": int(model_parameters),
        "training": asdict(training),
        "metrics": asdict(metrics),
    }


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
    training_started = perf_counter()
    history = model.fit(
        data.X_train, data.y_train, validation_data=(data.X_val, data.y_val),
        batch_size=config["batch_size"], epochs=config["epochs"], verbose=2,
    ).history
    training_summary = summarize_training_history(
        history, duration_seconds=perf_counter() - training_started
    )
    probabilities = model.predict(data.X_val, verbose=0)
    actual = data.y_val.argmax(axis=1)
    predicted = probabilities.argmax(axis=1)
    metrics = calculate_validation_metrics(actual, predicted)
    output_path = Path(output_directory)
    output_path.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(history).rename_axis("epoch").to_csv(output_path / f"{experiment_id}_history.csv")
    with (output_path / f"{experiment_id}_validation_metrics.json").open("w", encoding="utf-8") as metrics_file:
        json.dump(
            build_experiment_record(
                config=config,
                model_parameters=model.count_params(),
                metrics=metrics,
                training=training_summary,
            ),
            metrics_file,
            indent=2,
        )
    plot_history(history, experiment_id=experiment_id, output_path=output_path / f"{experiment_id}_curves.png")
    return metrics


def main() -> None:
    """Expone la ejecución reproducible como comando para los colaboradores."""
    parser = ArgumentParser(description="Ejecuta un experimento sobre validation de Fashion-MNIST")
    parser.add_argument("config", help="Ruta al archivo JSON de configuración")
    parser.add_argument("--output", required=True, help="Directorio local para historia, métricas y curva")
    arguments = parser.parse_args()
    print(run_validation_experiment(arguments.config, output_directory=arguments.output))


if __name__ == "__main__":
    main()
