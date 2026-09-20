"""Evaluación final única sobre test para una configuración previamente congelada."""

import json
from argparse import ArgumentParser
from dataclasses import asdict, dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_recall_fscore_support,
    precision_score,
    recall_score,
)

from ep1_fashion_mnist.data import CLASS_NAMES, prepare_fashion_mnist
from ep1_fashion_mnist.experiment import load_config, set_reproducible_seed
from ep1_fashion_mnist.model import build_mlp, compile_model


@dataclass(frozen=True)
class FinalMetrics:
    accuracy: float
    precision_macro: float
    recall_macro: float
    f1_macro: float
    precision_weighted: float
    recall_weighted: float
    f1_weighted: float


def validate_frozen_config(config: dict) -> dict:
    """Protege que F1 use solamente el protocolo cerrado en F0."""
    if config.get("status") != "frozen_pre_test":
        raise ValueError("F1 requiere una configuración con estado frozen_pre_test")
    if config.get("test_evaluation_budget") != 1:
        raise ValueError("F1 requiere un presupuesto de evaluación de test igual a 1")
    if config.get("final_evaluation_strategy") != "evaluate_selected_54k_model":
        raise ValueError("La estrategia final congelada no está soportada")
    return config


def calculate_final_metrics(actual: np.ndarray, predicted: np.ndarray) -> FinalMetrics:
    return FinalMetrics(
        accuracy=float(accuracy_score(actual, predicted)),
        precision_macro=float(precision_score(actual, predicted, average="macro", zero_division=0)),
        recall_macro=float(recall_score(actual, predicted, average="macro", zero_division=0)),
        f1_macro=float(f1_score(actual, predicted, average="macro", zero_division=0)),
        precision_weighted=float(precision_score(actual, predicted, average="weighted", zero_division=0)),
        recall_weighted=float(recall_score(actual, predicted, average="weighted", zero_division=0)),
        f1_weighted=float(f1_score(actual, predicted, average="weighted", zero_division=0)),
    )


def save_confusion_matrix(actual, predicted, output_path: Path) -> None:
    matrix = confusion_matrix(actual, predicted, labels=range(len(CLASS_NAMES)))
    figure, axis = plt.subplots(figsize=(10, 8))
    image = axis.imshow(matrix, cmap="Blues")
    figure.colorbar(image, ax=axis)
    axis.set(xticks=range(10), yticks=range(10), xticklabels=CLASS_NAMES, yticklabels=CLASS_NAMES,
             xlabel="Predicción", ylabel="Clase real", title="F1 — matriz de confusión en test")
    plt.setp(axis.get_xticklabels(), rotation=45, ha="right")
    for row, values in enumerate(matrix):
        for column, value in enumerate(values):
            axis.text(column, row, str(value), ha="center", va="center", fontsize=7)
    figure.tight_layout()
    figure.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(figure)


def save_error_examples(images, actual, predicted, probabilities, output_path: Path) -> None:
    incorrect = np.flatnonzero(actual != predicted)
    selected = incorrect[np.argsort(probabilities[incorrect, predicted[incorrect]])[:12]]
    figure, axes = plt.subplots(3, 4, figsize=(10, 8))
    for axis, index in zip(axes.flat, selected, strict=False):
        confidence = probabilities[index, predicted[index]]
        axis.imshow(images[index], cmap="gray")
        axis.set_title(f"real: {CLASS_NAMES[actual[index]]}\npred: {CLASS_NAMES[predicted[index]]} ({confidence:.2f})", fontsize=8)
        axis.axis("off")
    for axis in axes.flat[len(selected):]:
        axis.axis("off")
    figure.suptitle("F1 — errores de menor confianza en test")
    figure.tight_layout(rect=(0, 0, 1, 0.95))
    figure.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(figure)


def run_final_test_evaluation(config_path, *, output_directory, selected_figures_directory) -> dict:
    """Entrena la configuración congelada y consulta test una sola vez."""
    config = validate_frozen_config(load_config(config_path))
    output_directory = Path(output_directory)
    record_path = output_directory / "F1_final_test_record.json"
    if record_path.exists():
        raise FileExistsError("F1 ya fue ejecutado; no se permite una segunda evaluación de test")
    output_directory.mkdir(parents=True, exist_ok=True)
    figures = Path(selected_figures_directory)
    figures.mkdir(parents=True, exist_ok=True)

    set_reproducible_seed(config["seed"])
    data = prepare_fashion_mnist(seed=config["seed"], validation_fraction=config["validation_fraction"])
    model = compile_model(
        build_mlp(config["hidden_layers"], hidden_activation=config["hidden_activation"],
                  dropout=config["dropout"], batch_normalization=config["batch_normalization"],
                  l2_strength=config["l2_strength"], seed=config["seed"]),
        optimizer=config["optimizer"], learning_rate=config["learning_rate"], loss=config["loss"],
    )
    model.fit(data.X_train, data.y_train, validation_data=(data.X_val, data.y_val),
              batch_size=config["batch_size"], epochs=config["epochs"], verbose=2)
    probabilities = model.predict(data.X_test, verbose=0)
    actual, predicted = data.y_test.argmax(axis=1), probabilities.argmax(axis=1)
    metrics = calculate_final_metrics(actual, predicted)
    precision, recall, f1, support = precision_recall_fscore_support(actual, predicted, labels=range(10), zero_division=0)
    pd.DataFrame({"class_id": range(10), "class_name": CLASS_NAMES, "precision": precision,
                  "recall": recall, "f1": f1, "support": support}).to_csv(output_directory / "F1_per_class_metrics.csv", index=False)
    save_confusion_matrix(actual, predicted, figures / "F1_test_confusion_matrix.png")
    save_error_examples(data.X_test, actual, predicted, probabilities, figures / "F1_test_low_confidence_errors.png")
    record = {"experiment_id": "F1_final_test", "config": config, "metrics": asdict(metrics),
              "model_parameters": model.count_params(), "test_examples": int(actual.size)}
    record_path.write_text(json.dumps(record, indent=2), encoding="utf-8")
    return record


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("config")
    parser.add_argument("--output", required=True)
    parser.add_argument("--selected-figures", required=True)
    parser.add_argument("--allow-test-evaluation", action="store_true")
    args = parser.parse_args()
    if not args.allow_test_evaluation:
        raise SystemExit("F1 requiere --allow-test-evaluation de forma explícita")
    print(json.dumps(run_final_test_evaluation(args.config, output_directory=args.output,
                                               selected_figures_directory=args.selected_figures), indent=2))


if __name__ == "__main__":
    main()
