import numpy as np

from mayday.models.metrics import (
    ForecastMetrics,
    ModelEvaluator,
)


def test_model_evaluator() -> None:
    """
    ModelEvaluator should compute
    forecasting metrics.
    """

    y_true = np.array([10, 20, 30, 40])

    y_pred = np.array([11, 19, 29, 41])

    metrics = ModelEvaluator.evaluate(
        y_true,
        y_pred,
    )

    assert isinstance(
        metrics,
        ForecastMetrics,
    )

    assert metrics.mae >= 0

    assert metrics.rmse >= 0

    assert metrics.mape >= 0

    assert metrics.smape >= 0

    assert metrics.r2 <= 1
