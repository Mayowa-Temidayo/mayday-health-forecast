from pathlib import Path

import pandas as pd
import pytest

from mayday.core.exceptions import DatasetFormatUnavailableError
from mayday.datasets.io import DatasetIO


def test_save_and_load_csv(
    tmp_path: Path,
) -> None:
    """
    CSV datasets should be saved and loaded correctly.
    """

    dataframe = pd.DataFrame(
        {
            "x": [1, 2],
            "y": [3, 4],
        }
    )

    path = tmp_path / "dataset.csv"

    artifact = DatasetIO.save(
        dataframe=dataframe,
        path=path,
    )

    loaded = DatasetIO.load(path)

    assert artifact.path == path
    assert artifact.name == "dataset"
    assert loaded.equals(dataframe)


def test_parquet_not_supported(
    tmp_path: Path,
) -> None:
    """
    Parquet should raise a platform-specific exception.
    """

    dataframe = pd.DataFrame(
        {
            "x": [1],
        }
    )

    with pytest.raises(
        DatasetFormatUnavailableError,
    ):
        DatasetIO.save(
            dataframe=dataframe,
            path=tmp_path / "dataset.parquet",
            format="parquet",
        )


def test_invalid_format(
    tmp_path: Path,
) -> None:
    """
    Unsupported formats should raise ValueError.
    """

    dataframe = pd.DataFrame(
        {
            "x": [1],
        }
    )

    with pytest.raises(ValueError):
        DatasetIO.save(
            dataframe=dataframe,
            path=tmp_path / "dataset.bin",
            format="binary",  # type: ignore[arg-type]
        )
