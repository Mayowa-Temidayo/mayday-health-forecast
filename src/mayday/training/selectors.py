from dataclasses import dataclass
from typing import cast

import pandas as pd

from mayday.training.datasets import TrainingDatasets


@dataclass(slots=True, frozen=True)
class TrainingData:
    """
    Container holding feature matrices and target vectors.
    """

    X_train: pd.DataFrame
    y_train: pd.Series

    X_validation: pd.DataFrame
    y_validation: pd.Series

    X_test: pd.DataFrame
    y_test: pd.Series


class FeatureSelector:
    """
    Builds model-ready feature matrices and target vectors
    from chronological training datasets.
    """

    def __init__(
        self,
        target_column: str = "confirmed_cases",
        drop_columns: list[str] | None = None,
    ) -> None:
        self.target_column = target_column
        self.drop_columns = drop_columns or []

    def build(
        self,
        datasets: TrainingDatasets,
    ) -> TrainingData:
        """
        Convert chronological datasets into model-ready
        feature matrices and target vectors.
        """

        return TrainingData(
            X_train=self._features(datasets.train),
            y_train=self._target(datasets.train),
            X_validation=self._features(datasets.validation),
            y_validation=self._target(datasets.validation),
            X_test=self._features(datasets.test),
            y_test=self._target(datasets.test),
        )

    def _features(
        self,
        dataset: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Extract predictor columns.
        """

        columns = [
            self.target_column,
            *self.drop_columns,
        ]

        return dataset.drop(
            columns=columns,
            errors="ignore",
        )

    def _target(
        self,
        dataset: pd.DataFrame,
    ) -> pd.Series:
        """
        Extract the prediction target.
        """

        return cast(
            pd.Series,
            dataset[self.target_column],
        )
