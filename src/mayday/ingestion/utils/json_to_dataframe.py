from __future__ import annotations

import pandas as pd


def power_json_to_dataframe(data: dict) -> pd.DataFrame:
    """
    Convert a NASA POWER JSON response into a tidy DataFrame.
    """

    parameter_block = data["properties"]["parameter"]

    df = pd.DataFrame(parameter_block)

    df.index.name = "date"

    df.reset_index(inplace=True)

    df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")

    return df
