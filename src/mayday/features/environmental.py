import pandas as pd

from mayday.features.base import BaseFeatureTransformer


class EnvironmentalFeatureTransformer(BaseFeatureTransformer):
    """
    Creates derived environmental features.
    """

    def transform(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        df = data.copy()

        # Temperature in Kelvin
        df["T2M_K"] = df["T2M"] + 273.15

        # Rain indicator
        df["is_rainy_day"] = (df["PRECTOTCORR"] > 0).astype(int)

        return df
