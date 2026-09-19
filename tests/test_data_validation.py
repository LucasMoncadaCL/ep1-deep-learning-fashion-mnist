import unittest
from pathlib import Path

import numpy as np

from ep1_fashion_mnist.data import (
    normalize_images,
    one_hot_encode,
    prepare_fashion_mnist,
)
from ep1_fashion_mnist.data_validation import (
    DataContractError,
    validate_image_classification_split,
    validate_train_validation_partition,
)
from ep1_fashion_mnist.experiment import (
    build_experiment_record,
    calculate_validation_metrics,
    load_config,
    summarize_training_history,
    validate_config,
)
from ep1_fashion_mnist.model import build_mlp, compile_model


class ValidateImageClassificationSplitTests(unittest.TestCase):
    def setUp(self):
        self.images = np.array(
            [
                [[0, 10], [20, 30]],
                [[40, 50], [60, 70]],
                [[80, 90], [100, 110]],
                [[120, 130], [140, 255]],
            ],
            dtype=np.uint8,
        )
        self.labels = np.array([0, 0, 1, 1], dtype=np.uint8)

    def test_accepts_a_valid_balanced_uint8_split(self):
        summary = validate_image_classification_split(
            self.images,
            self.labels,
            split_name="sample",
            expected_count=4,
            expected_image_shape=(2, 2),
            expected_num_classes=2,
            expected_per_class=2,
            require_full_uint8_range=True,
        )

        self.assertEqual(summary.count, 4)
        self.assertEqual(summary.image_shape, (2, 2))
        self.assertEqual(summary.pixel_range, (0, 255))
        self.assertEqual(summary.class_counts, {0: 2, 1: 2})

    def test_rejects_an_unbalanced_split_when_balance_is_required(self):
        labels = np.array([0, 0, 0, 1], dtype=np.uint8)

        with self.assertRaisesRegex(DataContractError, "distribución inesperada"):
            validate_image_classification_split(
                self.images,
                labels,
                split_name="sample",
                expected_count=4,
                expected_image_shape=(2, 2),
                expected_num_classes=2,
                expected_per_class=2,
                require_full_uint8_range=True,
            )

    def test_rejects_an_unexpected_shape(self):
        with self.assertRaisesRegex(DataContractError, "forma de imágenes"):
            validate_image_classification_split(
                self.images[:, :, :1],
                self.labels,
                split_name="sample",
                expected_count=4,
                expected_image_shape=(2, 2),
                expected_num_classes=2,
            )

    def test_rejects_non_uint8_images(self):
        with self.assertRaisesRegex(DataContractError, "esperado uint8"):
            validate_image_classification_split(
                self.images.astype(np.float32),
                self.labels,
                split_name="sample",
                expected_count=4,
                expected_image_shape=(2, 2),
                expected_num_classes=2,
            )

    def test_rejects_an_incomplete_uint8_range_when_required(self):
        with self.assertRaisesRegex(DataContractError, r"se esperaba \(0, 255\)"):
            validate_image_classification_split(
                np.clip(self.images, 1, 254),
                self.labels,
                split_name="sample",
                expected_count=4,
                expected_image_shape=(2, 2),
                expected_num_classes=2,
                expected_per_class=2,
                require_full_uint8_range=True,
            )


class ValidateTrainValidationPartitionTests(unittest.TestCase):
    def test_accepts_a_complete_disjoint_partition(self):
        summary = validate_train_validation_partition(
            np.array([0, 2, 3], dtype=np.int64),
            np.array([1], dtype=np.int64),
            source_count=4,
        )

        self.assertEqual(summary.train_count, 3)
        self.assertEqual(summary.validation_count, 1)
        self.assertEqual(summary.source_count, 4)

    def test_rejects_overlap_between_train_and_validation(self):
        with self.assertRaisesRegex(DataContractError, "solapamiento"):
            validate_train_validation_partition(
                np.array([0, 1, 2], dtype=np.int64),
                np.array([2, 3], dtype=np.int64),
                source_count=4,
            )


class PrepareFashionMnistTests(unittest.TestCase):
    @staticmethod
    def _official_like_loader():
        """Genera arrays con el contrato oficial sin descargar el dataset en el test."""
        train_images = np.zeros((60_000, 28, 28), dtype=np.uint8)
        test_images = np.zeros((10_000, 28, 28), dtype=np.uint8)
        train_images[:, 0, 0] = 255
        test_images[:, 0, 0] = 255
        train_labels = np.repeat(np.arange(10, dtype=np.uint8), 6_000)
        test_labels = np.repeat(np.arange(10, dtype=np.uint8), 1_000)
        return train_images, train_labels, test_images, test_labels

    def test_normalization_and_one_hot_encoding(self):
        images = np.array([[[0, 255]]], dtype=np.uint8)
        labels = np.array([2], dtype=np.uint8)

        normalized = normalize_images(images)
        encoded = one_hot_encode(labels, num_classes=3)

        self.assertEqual(normalized.dtype, np.float32)
        self.assertEqual(normalized.tolist(), [[[0.0, 1.0]]])
        self.assertEqual(encoded.dtype, np.float32)
        self.assertEqual(encoded.tolist(), [[0.0, 0.0, 1.0]])

    def test_preparation_makes_the_required_stratified_partition(self):
        data = prepare_fashion_mnist(loader=self._official_like_loader)

        self.assertEqual(data.X_train.shape, (54_000, 28, 28))
        self.assertEqual(data.X_val.shape, (6_000, 28, 28))
        self.assertEqual(data.X_test.shape, (10_000, 28, 28))
        self.assertEqual(data.y_train.shape, (54_000, 10))
        self.assertEqual(data.y_val.shape, (6_000, 10))
        self.assertEqual(data.y_test.shape, (10_000, 10))
        self.assertEqual(data.partition_summary.train_count, 54_000)
        self.assertEqual(data.partition_summary.validation_count, 6_000)
        self.assertTrue(np.all(data.y_train.sum(axis=0) == 5_400))
        self.assertTrue(np.all(data.y_val.sum(axis=0) == 600))
        self.assertEqual(float(data.X_train.min()), 0.0)
        self.assertEqual(float(data.X_train.max()), 1.0)

    def test_preparation_repeats_the_same_partition_with_the_same_seed(self):
        first = prepare_fashion_mnist(loader=self._official_like_loader, seed=42)
        first_train_indices = first.train_indices.copy()
        first_validation_indices = first.validation_indices.copy()
        del first
        second = prepare_fashion_mnist(loader=self._official_like_loader, seed=42)

        np.testing.assert_array_equal(first_train_indices, second.train_indices)
        np.testing.assert_array_equal(first_validation_indices, second.validation_indices)

    def test_rejects_an_incomplete_partition(self):
        with self.assertRaisesRegex(DataContractError, "partición completa"):
            validate_train_validation_partition(
                np.array([0, 1], dtype=np.int64),
                np.array([3], dtype=np.int64),
                source_count=4,
            )


class ModelAndConfigurationTests(unittest.TestCase):
    def test_e0_builds_ten_probabilities_and_compiles(self):
        model = compile_model(
            build_mlp([256, 128], seed=42),
            optimizer="sgd", learning_rate=0.01, loss="categorical_crossentropy",
        )
        probabilities = model(np.zeros((2, 28, 28), dtype=np.float32), training=False).numpy()

        self.assertEqual(model.count_params(), 235_146)
        self.assertEqual(probabilities.shape, (2, 10))
        np.testing.assert_allclose(probabilities.sum(axis=1), np.ones(2), atol=1e-6)

    def test_e0_config_matches_the_supported_label_output_loss_contract(self):
        root = Path(__file__).resolve().parents[1]
        config = load_config(root / "configs" / "baseline.json")

        self.assertEqual(config["label_encoding"], "one_hot")
        self.assertEqual(config["output_activation"], "softmax")
        self.assertEqual(config["loss"], "categorical_crossentropy")

    def test_rejects_invalid_numeric_and_structural_configuration_values(self):
        root = Path(__file__).resolve().parents[1]
        baseline = load_config(root / "configs" / "baseline.json")
        invalid_cases = (
            ("learning_rate", 0, ValueError, "learning_rate"),
            ("batch_size", 0, ValueError, "batch_size"),
            ("epochs", 0, ValueError, "epochs"),
            ("validation_fraction", 1.0, ValueError, "validation_fraction"),
            ("hidden_layers", [], ValueError, "hidden_layers"),
            ("dropout", 1.0, ValueError, "dropout"),
            ("l2_strength", -0.1, ValueError, "l2_strength"),
            ("early_stopping", "false", TypeError, "early_stopping"),
        )

        for field, invalid_value, exception, message in invalid_cases:
            with self.subTest(field=field), self.assertRaisesRegex(exception, message):
                config = dict(baseline)
                config[field] = invalid_value
                validate_config(config)

    def test_e3_configs_change_only_the_learning_rate(self):
        root = Path(__file__).resolve().parents[1]
        baseline = load_config(root / "configs" / "baseline.json")
        expected_learning_rates = {
            "E3_lr_0_001": 0.001,
            "E3_lr_0_01": 0.01,
            "E3_lr_0_1": 0.1,
        }
        ignored_fields = {"experiment_id", "status", "learning_rate"}
        baseline_control = {
            key: value for key, value in baseline.items() if key not in ignored_fields
        }

        for experiment_id, expected_learning_rate in expected_learning_rates.items():
            with self.subTest(experiment_id=experiment_id):
                config = load_config(root / "configs" / f"{experiment_id}.json")
                controlled_fields = {
                    key: value for key, value in config.items() if key not in ignored_fields
                }
                self.assertEqual(controlled_fields, baseline_control)
                self.assertEqual(config["experiment_id"], experiment_id)
                self.assertEqual(config["learning_rate"], expected_learning_rate)

    def test_e4_configs_change_only_the_batch_size(self):
        root = Path(__file__).resolve().parents[1]
        e3_control = load_config(root / "configs" / "E3_lr_0_1.json")
        expected_batch_sizes = {
            "E4_batch_32": 32,
            "E4_batch_128": 128,
            "E4_batch_512": 512,
        }
        ignored_fields = {"experiment_id", "status", "batch_size"}
        baseline_control = {
            key: value for key, value in e3_control.items() if key not in ignored_fields
        }

        for experiment_id, expected_batch_size in expected_batch_sizes.items():
            with self.subTest(experiment_id=experiment_id):
                config = load_config(root / "configs" / f"{experiment_id}.json")
                controlled_fields = {
                    key: value for key, value in config.items() if key not in ignored_fields
                }
                self.assertEqual(controlled_fields, baseline_control)
                self.assertEqual(config["experiment_id"], experiment_id)
                self.assertEqual(config["batch_size"], expected_batch_size)


class ValidationMetricsTests(unittest.TestCase):
    def test_reports_macro_and_weighted_metrics(self):
        actual = np.array([0, 0, 0, 1])
        predicted = np.array([0, 0, 1, 1])

        metrics = calculate_validation_metrics(actual, predicted)

        self.assertAlmostEqual(metrics.accuracy, 0.75)
        self.assertAlmostEqual(metrics.precision_macro, 0.75)
        self.assertAlmostEqual(metrics.recall_macro, 5 / 6)
        self.assertAlmostEqual(metrics.f1_macro, 11 / 15)
        self.assertAlmostEqual(metrics.precision_weighted, 0.875)
        self.assertAlmostEqual(metrics.recall_weighted, 0.75)
        self.assertAlmostEqual(metrics.f1_weighted, 23 / 30)
        self.assertNotEqual(metrics.f1_macro, metrics.f1_weighted)


class TrainingSummaryTests(unittest.TestCase):
    def test_rejects_incomplete_or_misaligned_history(self):
        with self.assertRaisesRegex(ValueError, "faltan: val_accuracy"):
            summarize_training_history(
                {"loss": [0.5], "val_loss": [0.4], "accuracy": [0.8]},
                duration_seconds=1.0,
            )

        with self.assertRaisesRegex(ValueError, "igual longitud"):
            summarize_training_history(
                {
                    "loss": [0.5, 0.4],
                    "val_loss": [0.4],
                    "accuracy": [0.8, 0.9],
                    "val_accuracy": [0.9, 0.91],
                },
                duration_seconds=1.0,
            )

    def test_summarizes_convergence_cost_and_final_gaps(self):
        history = {
            "loss": [0.8, 0.5, 0.3],
            "val_loss": [0.7, 0.4, 0.45],
            "accuracy": [0.6, 0.8, 0.9],
            "val_accuracy": [0.65, 0.85, 0.84],
        }

        summary = summarize_training_history(history, duration_seconds=12.5)

        self.assertEqual(summary.epochs_completed, 3)
        self.assertEqual(summary.best_epoch_by_validation_loss, 2)
        self.assertAlmostEqual(summary.best_validation_loss, 0.4)
        self.assertEqual(summary.best_epoch_by_validation_accuracy, 2)
        self.assertAlmostEqual(summary.best_validation_accuracy, 0.85)
        self.assertAlmostEqual(summary.final_train_loss, 0.3)
        self.assertAlmostEqual(summary.final_validation_loss, 0.45)
        self.assertAlmostEqual(summary.final_train_accuracy, 0.9)
        self.assertAlmostEqual(summary.final_validation_accuracy, 0.84)
        self.assertAlmostEqual(summary.final_accuracy_gap, 0.06)
        self.assertAlmostEqual(summary.final_loss_gap, 0.15)
        self.assertAlmostEqual(summary.duration_seconds, 12.5)

    def test_builds_a_self_contained_experiment_record(self):
        root = Path(__file__).resolve().parents[1]
        config = load_config(root / "configs" / "baseline.json")
        metrics = calculate_validation_metrics(
            np.array([0, 1]), np.array([0, 1])
        )
        training = summarize_training_history(
            {
                "loss": [0.5],
                "val_loss": [0.4],
                "accuracy": [0.8],
                "val_accuracy": [0.9],
            },
            duration_seconds=2.0,
        )

        record = build_experiment_record(
            config=config,
            model_parameters=235_146,
            metrics=metrics,
            training=training,
        )

        self.assertEqual(record["experiment_id"], "E0")
        self.assertEqual(record["config"], config)
        self.assertEqual(record["model_parameters"], 235_146)
        self.assertEqual(record["training"]["epochs_completed"], 1)
        self.assertEqual(record["metrics"]["f1_macro"], 1.0)


if __name__ == "__main__":
    unittest.main()
