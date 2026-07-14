from pathlib import Path

import joblib
import lightgbm as lgb
import pandas as pd

from mayday.models.base import BaseForecastModel


class LightGBMModel(BaseForecastModel):
    """
    LightGBM forecasting model implementation.
    """

    def __init__(
        self,
        **parameters: object,
    ) -> None:

        defaults = {
            "objective": "regression",
            "metric": "rmse",
            "verbosity": -1,
            "random_state": 42,
        }

        defaults.update(parameters)

        self.parameters = defaults

        self.model: lgb.LGBMRegressor | None = None

    @property
    def name(self) -> str:
        return "LightGBM"

    def train(
        self,
        X_train: pd.DataFrame,
        y_train: pd.Series,
        X_validation: pd.DataFrame,
        y_validation: pd.Series,
    ) -> None:
        """
        Train the LightGBM model.
        """

        self.model = lgb.LGBMRegressor(
            **self.parameters,
        )

        self.model.fit(
            X_train,
            y_train,
            eval_set=[
                (
                    X_validation,
                    y_validation,
                )
            ],
        )

    def predict(
        self,
        X: pd.DataFrame,
    ) -> pd.Series:
        """
        Generate predictions.
        """

        if self.model is None:
            raise RuntimeError("Model has not been trained.")

        predictions = self.model.predict(X)

        return pd.Series(
            predictions,
            index=X.index,
            name="prediction",
        )

    def save(
        self,
        path: Path,
    ) -> None:
        """
        Persist the trained model.
        """

        if self.model is None:
            raise RuntimeError("Model has not been trained.")

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        joblib.dump(
            self.model,
            path,
        )

    @classmethod
    def load(
        cls,
        path: Path,
    ) -> "LightGBMModel":
        """
        Restore a trained model.
        """

        instance = cls()

        instance.model = joblib.load(path)

        return instance
