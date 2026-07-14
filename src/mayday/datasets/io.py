from pathlib import Path
from typing import Literal

import pandas as pd

from mayday.core.exceptions import DatasetFormatUnavailableError
from mayday.datasets.artifacts import (
    DatasetArtifact,
    DatasetMetadata,
)

DatasetFormat = Literal["csv", "parquet"]


class DatasetIO:
    """
    Handles dataset persistence.
    """

    @staticmethod
    def save(
        dataframe: pd.DataFrame,
        path: Path,
        format: DatasetFormat = "csv",
    ) -> DatasetArtifact:
        """
        Save a dataset to disk.
        """
        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if format == "csv":
            dataframe.to_csv(
                path,
                index=False,
            )

        elif format == "parquet":
            raise DatasetFormatUnavailableError(
                "Parquet support is unavailable on this development machine."
            )

        else:
            raise ValueError(f"Unsupported format: {format}")

        return DatasetArtifact(
            name=path.stem,
            path=path,
            format=format,
            metadata=DatasetMetadata(
                rows=len(dataframe),
                columns=len(dataframe.columns),
                feature_count=len(dataframe.columns) - 1,
                target="confirmed_cases",
            ),
        )

    @staticmethod
    def load(
        path: Path,
        format: DatasetFormat = "csv",
    ) -> pd.DataFrame:
        """
        Load a dataset from disk.
        """

        if format == "csv":
            return pd.read_csv(path)

        if format == "parquet":
            raise DatasetFormatUnavailableError(
                "Parquet support is unavailable on this development machine."
            )

        raise ValueError(f"Unsupported format: {format}")
