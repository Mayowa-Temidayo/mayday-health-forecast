from pathlib import Path

import pandas as pd

from mayday.models.base import BaseForecastModel
from mayday.models.pipeline import ModelPipeline
from mayday.training.selectors import TrainingData


class DummyModel(BaseForecastModel):
    @property
    def name(self) -> str:
        return "Dummy"

    def train(
        self,
        X_train: pd.DataFrame,
        y_train: pd.Series,
        X_validation: pd.DataFrame,
        y_validation: pd.Series,
    ) -> None:
        pass

    def predict(
        self,
        X: pd.DataFrame,
    ) -> pd.Series:

        return pd.Series(
            [1.0] * len(X),
            index=X.index,
        )

    def save(
        self,
        path: Path,
    ) -> None:
        path.touch()

    @classmethod
    def load(
        cls,
        path: Path,
    ) -> "DummyModel":
        return cls()


def test_model_pipeline(
    tmp_path: Path,
) -> None:

    training_data = TrainingData(
        X_train=pd.DataFrame({"x": [1, 2, 3]}),
        y_train=pd.Series([1, 2, 3]),
        X_validation=pd.DataFrame({"x": [4, 5]}),
        y_validation=pd.Series([1, 1]),
        X_test=pd.DataFrame({"x": [6]}),
        y_test=pd.Series([1]),
    )

    pipeline = ModelPipeline(
        DummyModel(),
    )

    artifact = pipeline.run(
        training_data,
        tmp_path / "dummy.pkl",
    )

    assert artifact.path.exists()

    assert artifact.name == "Dummy"

    assert artifact.metrics.mae >= 0
