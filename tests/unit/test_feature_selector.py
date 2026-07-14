import pandas as pd

from mayday.training.datasets import TrainingDatasets
from mayday.training.selectors import (
    FeatureSelector,
)


def test_feature_selector() -> None:
    """
    FeatureSelector should separate
    predictors from the target.
    """

    train = pd.DataFrame(
        {
            "confirmed_cases": [1, 2],
            "temperature": [30, 31],
            "humidity": [70, 72],
        }
    )

    datasets = TrainingDatasets(
        train=train,
        validation=train.copy(),
        test=train.copy(),
    )

    selector = FeatureSelector()

    data = selector.build(
        datasets,
    )

    assert "confirmed_cases" not in data.X_train.columns

    assert list(data.y_train) == [1, 2]

    assert len(data.X_train.columns) == 2
