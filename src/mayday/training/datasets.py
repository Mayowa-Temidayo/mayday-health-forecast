from dataclasses import dataclass

import pandas as pd

from mayday.training.splitter import (
    SplitConfig,
    TimeSeriesSplitter,
)


@dataclass(slots=True, frozen=True)
class TrainingDatasets:
    """
    Chronological datasets used during training.
    """

    train: pd.DataFrame

    validation: pd.DataFrame

    test: pd.DataFrame


class TrainingDatasetBuilder:
    """
    Builds chronological training datasets.
    """

    def __init__(
        self,
        config: SplitConfig | None = None,
    ) -> None:

        self._splitter = TimeSeriesSplitter(config)

    def build(
        self,
        dataset: pd.DataFrame,
    ) -> TrainingDatasets:
        """
        Build train, validation and test datasets.
        """

        train, validation, test = self._splitter.split(dataset)

        return TrainingDatasets(
            train=train,
            validation=validation,
            test=test,
        )
