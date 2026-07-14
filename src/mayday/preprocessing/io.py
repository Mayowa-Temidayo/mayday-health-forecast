"""
Input/output utilities for preprocessing.
"""

from pathlib import Path
from mayday.datasets.versioning import DatasetVersionManager
import shutil

import pandas as pd

from mayday.core.paths import (
    EXTERNAL_DATA_DIR,
    PROCESSED_DATA_DIR,
    RAW_DATA_DIR,
)
from mayday.datasets.io import DatasetIO


def load_epidemiology() -> pd.DataFrame:
    """
    Load the primary epidemiological dataset.
    """
    return pd.read_csv(RAW_DATA_DIR / "lassa_fever_timeseries_full.csv")


def load_environmental() -> pd.DataFrame:
    """
    Load the NASA POWER environmental dataset.
    """
    return pd.read_csv(EXTERNAL_DATA_DIR / "nasa_power" / "nasa_power_daily.csv")


def save_processed(
    dataframe: pd.DataFrame,
    filename: str = "modeling_dataset",
) -> Path:
    """
    Save the processed dataset using an automatically
    incremented dataset version.

    Returns the versioned CSV path.
    """

    version_manager = DatasetVersionManager()

    version = version_manager.next_version(
        prefix=filename,
    )

    versioned_name = f"{filename}_v{version}"

    csv_path = PROCESSED_DATA_DIR / f"{versioned_name}.csv"

    DatasetIO.save(
        dataframe=dataframe,
        path=csv_path,
        format="csv",
    )
    latest_path = PROCESSED_DATA_DIR / f"{filename}_latest.csv"

    shutil.copy2(
        csv_path,
        latest_path,
    )

    return csv_path
