import pandas as pd
import numpy as np

from mayday.features.seasonal import (
    SeasonalFeatureTransformer,
)


def test_seasonal_features_created() -> None:
    df = pd.DataFrame(
        {
            "epi_year": [2020, 2020, 2021],
            "epi_week": [1, 2, 1],
        }
    )

    transformer = SeasonalFeatureTransformer()

    result = transformer.transform(df)

    assert "epi_week_sin" in result.columns

    assert "epi_week_cos" in result.columns


def test_seasonal_values_are_bounded() -> None:
    df = pd.DataFrame(
        {
            "epi_year": [2020, 2020, 2021],
            "epi_week": [1, 2, 1],
        }
    )

    transformer = SeasonalFeatureTransformer()

    result = transformer.transform(df)

    assert (result["epi_week_sin"].abs() <= 1).all()

    assert (result["epi_week_cos"].abs() <= 1).all()

    assert np.isfinite(result["epi_week_sin"]).all()

    assert np.isfinite(result["epi_week_cos"]).all()
