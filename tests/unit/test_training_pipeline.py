from pathlib import Path

import pandas as pd

from mayday.datasets.io import DatasetIO
from mayday.training.pipeline import TrainingPipeline


def test_training_pipeline(
    tmp_path: Path,
) -> None:
    """
    TrainingPipeline should create
    train, validation and test datasets.
    """

    dataset = pd.DataFrame(
        {
            "week": range(100),
            "confirmed_cases": range(100),
        }
    )

    dataset_path = tmp_path / "features.csv"

    DatasetIO.save(
        dataset,
        dataset_path,
    )

    train_path = tmp_path / "train.csv"
    validation_path = tmp_path / "validation.csv"
    test_path = tmp_path / "test.csv"

    artifacts = TrainingPipeline().run(
        dataset_path,
        train_path,
        validation_path,
        test_path,
    )

    assert artifacts.train.path.exists()
    assert artifacts.validation.path.exists()
    assert artifacts.test.path.exists()

    assert artifacts.train.metadata.rows == 70
    assert artifacts.validation.metadata.rows == 15
    assert artifacts.test.metadata.rows == 15
