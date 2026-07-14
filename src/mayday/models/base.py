from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class BaseForecastModel(ABC):
    """
    Abstract interface implemented by every
    forecasting model.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human-readable model name.
        """

    @abstractmethod
    def train(
        self,
        X_train: pd.DataFrame,
        y_train: pd.Series,
        X_validation: pd.DataFrame,
        y_validation: pd.Series,
    ) -> None:
        """
        Train the forecasting model.
        """

    @abstractmethod
    def predict(
        self,
        X: pd.DataFrame,
    ) -> pd.Series:
        """
        Generate predictions.
        """

    @abstractmethod
    def save(
        self,
        path: Path,
    ) -> None:
        """
        Persist the trained model.
        """

    @classmethod
    @abstractmethod
    def load(
        cls,
        path: Path,
    ) -> "BaseForecastModel":
        """
        Restore a persisted model.
        """
