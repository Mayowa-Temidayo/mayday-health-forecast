import pandas as pd

from mayday.ingestion.utils.json_to_dataframe import (
    power_json_to_dataframe,
)


def test_json_conversion() -> None:
    sample = {
        "properties": {
            "parameter": {
                "T2M": {
                    "20240101": 28,
                    "20240102": 29,
                },
                "RH2M": {
                    "20240101": 81,
                    "20240102": 79,
                },
            }
        }
    }

    df = power_json_to_dataframe(sample)

    assert isinstance(df, pd.DataFrame)

    assert len(df) == 2

    assert "date" in df.columns

    assert "T2M" in df.columns

    assert "RH2M" in df.columns
