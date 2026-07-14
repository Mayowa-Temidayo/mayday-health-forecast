from dataclasses import dataclass

import pandas as pd


@dataclass(slots=True, frozen=True)
class SplitConfig:
    """
    Configuration for chronological dataset splitting.
    """

    train_ratio: float = 0.70
    validation_ratio: float = 0.15
    test_ratio: float = 0.15


class TimeSeriesSplitter:
    """
    Splits a dataset chronologically.
    """

    def __init__(
        self,
        config: SplitConfig | None = None,
    ) -> None:
        self.config = config or SplitConfig()

    def split(
        self,
        data: pd.DataFrame,
    ) -> tuple[
        pd.DataFrame,
        pd.DataFrame,
        pd.DataFrame,
    ]:

        n = len(data)

        train_end = int(n * self.config.train_ratio)

        validation_end = train_end + int(n * self.config.validation_ratio)

        train = data.iloc[:train_end].copy()

        validation = data.iloc[train_end:validation_end].copy()

        test = data.iloc[validation_end:].copy()

        return (
            train,
            validation,
            test,
        )
