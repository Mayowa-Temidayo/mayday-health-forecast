import pandas as pd
import pytest

from mayday.features.environmental import (
    EnvironmentalFeatureTransformer,
)


def test_environmental_features_created() -> None:
    df = pd.DataFrame(
        {
            "T2M": [20.0],
            "PRECTOTCORR": [5.0],
        }
    )

    transformer = EnvironmentalFeatureTransformer()

    result = transformer.transform(df)

    assert "T2M_K" in result.columns
    assert "is_rainy_day" in result.columns


def test_temperature_conversion() -> None:
    df = pd.DataFrame(
        {
            "T2M": [25.0],
            "PRECTOTCORR": [0.0],
        }
    )

    transformer = EnvironmentalFeatureTransformer()

    result = transformer.transform(df)

    assert result.loc[0, "T2M_K"] == pytest.approx(298.15)


def test_rain_indicator() -> None:
    df = pd.DataFrame(
        {
            "T2M": [20.0, 21.0],
            "PRECTOTCORR": [0.0, 3.4],
        }
    )

    transformer = EnvironmentalFeatureTransformer()

    result = transformer.transform(df)

    assert result["is_rainy_day"].tolist() == [0, 1]
