import pandas as pd

from mayday.training.datasets import (
    TrainingDatasetBuilder,
)


def test_training_dataset_builder() -> None:
    """
    TrainingDatasetBuilder should create
    chronological datasets.
    """

    data = pd.DataFrame(
        {
            "week": range(100),
        }
    )

    datasets = TrainingDatasetBuilder().build(data)

    assert len(datasets.train) == 70

    assert len(datasets.validation) == 15

    assert len(datasets.test) == 15
