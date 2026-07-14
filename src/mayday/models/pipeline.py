from pathlib import Path

from mayday.models.artifacts import ModelArtifact
from mayday.models.base import BaseForecastModel
from mayday.models.metrics import ModelEvaluator
from mayday.training.selectors import TrainingData


class ModelPipeline:
    """
    Orchestrates model training, evaluation,
    persistence, and artifact creation.
    """

    def __init__(
        self,
        model: BaseForecastModel,
    ) -> None:
        self.model = model

    def run(
        self,
        data: TrainingData,
        output_path: Path,
    ) -> ModelArtifact:
        """
        Train, evaluate and persist the model.
        """

        self.model.train(
            data.X_train,
            data.y_train,
            data.X_validation,
            data.y_validation,
        )

        predictions = self.model.predict(
            data.X_validation,
        )

        metrics = ModelEvaluator.evaluate(
            data.y_validation.to_numpy(),
            predictions.to_numpy(),
        )

        self.model.save(
            output_path,
        )

        return ModelArtifact(
            name=self.model.name,
            path=output_path,
            metrics=metrics,
        )
