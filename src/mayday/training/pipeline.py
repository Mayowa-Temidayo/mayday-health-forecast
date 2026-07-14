from pathlib import Path

from mayday.datasets.artifacts import (
    DatasetArtifact,
    DatasetMetadata,
    TrainingDatasetArtifacts,
)
from mayday.datasets.io import DatasetIO
from mayday.training.datasets import (
    TrainingDatasetBuilder,
)


class TrainingPipeline:
    """
    Executes the complete training dataset workflow.

    Workflow
    --------
    1. Load engineered feature dataset.
    2. Split chronologically.
    3. Persist train/validation/test datasets.
    4. Return dataset artifacts.
    """

    def __init__(
        self,
        builder: TrainingDatasetBuilder | None = None,
    ) -> None:
        self._builder = builder or TrainingDatasetBuilder()

    def run(
        self,
        dataset_path: Path,
        train_path: Path,
        validation_path: Path,
        test_path: Path,
    ) -> TrainingDatasetArtifacts:

        dataset = DatasetIO.load(dataset_path)

        datasets = self._builder.build(dataset)

        DatasetIO.save(
            datasets.train,
            train_path,
        )

        DatasetIO.save(
            datasets.validation,
            validation_path,
        )

        DatasetIO.save(
            datasets.test,
            test_path,
        )

        train_metadata = DatasetMetadata(
            rows=len(datasets.train),
            columns=len(datasets.train.columns),
            feature_count=len(datasets.train.columns) - 1,
            target="confirmed_cases",
        )

        validation_metadata = DatasetMetadata(
            rows=len(datasets.validation),
            columns=len(datasets.validation.columns),
            feature_count=len(datasets.validation.columns) - 1,
            target="confirmed_cases",
        )

        test_metadata = DatasetMetadata(
            rows=len(datasets.test),
            columns=len(datasets.test.columns),
            feature_count=len(datasets.test.columns) - 1,
            target="confirmed_cases",
        )

        return TrainingDatasetArtifacts(
            train=DatasetArtifact(
                name=train_path.stem,
                path=train_path,
                format=train_path.suffix.removeprefix("."),
                metadata=train_metadata,
            ),
            validation=DatasetArtifact(
                name=validation_path.stem,
                path=validation_path,
                format=validation_path.suffix.removeprefix("."),
                metadata=validation_metadata,
            ),
            test=DatasetArtifact(
                name=test_path.stem,
                path=test_path,
                format=test_path.suffix.removeprefix("."),
                metadata=test_metadata,
            ),
        )
