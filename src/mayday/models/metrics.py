from dataclasses import dataclass

import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


@dataclass(slots=True, frozen=True)
class ForecastMetrics:
    """
    Standard forecasting evaluation metrics.
    """

    mae: float
    rmse: float
    mape: float
    smape: float
    r2: float


class ModelEvaluator:
    """
    Computes forecasting evaluation metrics.
    """

    @staticmethod
    def evaluate(
        y_true: np.ndarray,
        y_pred: np.ndarray,
    ) -> ForecastMetrics:

        mae = mean_absolute_error(
            y_true,
            y_pred,
        )

        rmse = float(
            np.sqrt(
                mean_squared_error(
                    y_true,
                    y_pred,
                )
            )
        )

        epsilon = 1e-8

        mape = float(np.mean(np.abs((y_true - y_pred) / (y_true + epsilon))) * 100)

        smape = float(
            np.mean(
                2
                * np.abs(y_pred - y_true)
                / (np.abs(y_true) + np.abs(y_pred) + epsilon)
            )
            * 100
        )

        r2 = float(
            r2_score(
                y_true,
                y_pred,
            )
        )

        return ForecastMetrics(
            mae=mae,
            rmse=rmse,
            mape=mape,
            smape=smape,
            r2=r2,
        )
