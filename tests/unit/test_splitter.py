import pandas as pd

from mayday.training.splitter import (
    TimeSeriesSplitter,
)


def test_time_series_split() -> None:
    """
    Dataset should be split chronologically.
    """

    data = pd.DataFrame(
        {
            "week": range(100),
        }
    )

    splitter = TimeSeriesSplitter()

    train, validation, test = splitter.split(
        data,
    )

    assert len(train) == 70

    assert len(validation) == 15

    assert len(test) == 15

    assert train["week"].max() == 69

    assert validation["week"].min() == 70

    assert validation["week"].max() == 84

    assert test["week"].min() == 85
