from mayday.features.environmental import (
    EnvironmentalFeatureTransformer,
)
from mayday.features.lags import LagFeatureTransformer
from mayday.features.pipeline import FeaturePipeline
from mayday.features.rolling import (
    RollingFeatureTransformer,
)
from mayday.features.seasonal import (
    SeasonalFeatureTransformer,
)


def build_feature_pipeline() -> FeaturePipeline:
    """
    Construct the default feature pipeline
    for MayDay forecasting.
    """

    return FeaturePipeline(
        [
            LagFeatureTransformer(
                target_column="confirmed_cases",
                lags=[1, 2, 4, 8],
            ),
            RollingFeatureTransformer(
                target_column="confirmed_cases",
                windows=[2, 4, 8],
                statistic="mean",
            ),
            SeasonalFeatureTransformer(),
            EnvironmentalFeatureTransformer(),
        ]
    )
