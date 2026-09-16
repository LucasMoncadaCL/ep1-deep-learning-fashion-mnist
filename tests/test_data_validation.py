import unittest

import numpy as np

from ep1_fashion_mnist.data_validation import (
    DataContractError,
    validate_image_classification_split,
    validate_train_validation_partition,
)


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

    def test_rejects_an_incomplete_partition(self):
        with self.assertRaisesRegex(DataContractError, "partición completa"):
            validate_train_validation_partition(
                np.array([0, 1], dtype=np.int64),
                np.array([3], dtype=np.int64),
                source_count=4,
            )


if __name__ == "__main__":
    unittest.main()
