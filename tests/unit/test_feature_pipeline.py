import pandas as pd

from mayday.features.lags import LagFeatureTransformer
from mayday.features.pipeline import FeaturePipeline
from mayday.features.rolling import RollingFeatureTransformer


def test_feature_pipeline_single_transformer() -> None:
    df = pd.DataFrame(
        {
            "confirmed_cases": [10, 20, 30],
        }
    )

    pipeline = FeaturePipeline(
        [
            LagFeatureTransformer(
                target_column="confirmed_cases",
                lags=[1],
            )
        ]
    )

    result = pipeline.run(df)

    assert "confirmed_cases_lag_1" in result.columns


def test_feature_pipeline_multiple_transformers() -> None:
    df = pd.DataFrame(
        {
            "confirmed_cases": [10, 20, 30, 40],
        }
    )

    pipeline = FeaturePipeline(
        [
            LagFeatureTransformer(
                target_column="confirmed_cases",
                lags=[1],
            ),
            RollingFeatureTransformer(
                target_column="confirmed_cases",
                windows=[2],
            ),
        ]
    )

    result = pipeline.run(df)

    assert "confirmed_cases_lag_1" in result.columns

    assert "confirmed_cases_rolling_mean_2" in result.columns
