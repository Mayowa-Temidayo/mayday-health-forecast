from pathlib import Path

import pandas as pd

from mayday.models.lightgbm import LightGBMModel


def test_lightgbm_training(
    tmp_path: Path,
) -> None:
    """
    LightGBM should train,
    predict and save successfully.
    """

    X_train = pd.DataFrame(
        {
            "temperature": [30, 31, 29, 28],
            "humidity": [70, 75, 72, 69],
        }
    )

    y_train = pd.Series(
        [10, 12, 9, 8],
    )

    X_validation = pd.DataFrame(
        {
            "temperature": [32, 27],
            "humidity": [74, 68],
        }
    )

    y_validation = pd.Series(
        [13, 7],
    )

    model = LightGBMModel()

    model.train(
        X_train,
        y_train,
        X_validation,
        y_validation,
    )

    predictions = model.predict(
        X_validation,
    )

    assert len(predictions) == len(
        X_validation,
    )

    model_path = tmp_path / "lightgbm.pkl"

    model.save(
        model_path,
    )

    assert model_path.exists()

    restored = LightGBMModel.load(
        model_path,
    )

    restored_predictions = restored.predict(
        X_validation,
    )

    assert len(restored_predictions) == len(
        predictions,
    )
