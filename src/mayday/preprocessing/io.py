"""
Input/output utilities for preprocessing.
"""

from pathlib import Path

import pandas as pd

from mayday.core.paths import (
    EXTERNAL_DATA_DIR,
    PROCESSED_DATA_DIR,
    RAW_DATA_DIR,
)


def load_epidemiology() -> pd.DataFrame:
    """
    Load the primary epidemiological dataset.
    """
    path = RAW_DATA_DIR / "lassa_fever_timeseries_full.csv"

    return pd.read_csv(path)


def load_environmental() -> pd.DataFrame:
    """
    Load the NASA POWER environmental dataset.
    """
    path = EXTERNAL_DATA_DIR / "nasa_power" / "nasa_power_daily.csv"

    return pd.read_csv(path)


def save_processed(
    dataframe: pd.DataFrame,
    filename: str = "modeling_dataset.parquet",
) -> Path:
    """
    Save the processed dataset as a Parquet file.
    """
    output_path = PROCESSED_DATA_DIR / "modeling_dataset.csv"

    dataframe.to_csv(
        output_path,
        index=False,
    )

    return output_path
