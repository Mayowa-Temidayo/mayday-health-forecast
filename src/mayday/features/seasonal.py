import numpy as np
import pandas as pd

from mayday.features.base import BaseFeatureTransformer
from mayday.utils.epi_calendar import EpidemiologicalCalendar


class SeasonalFeatureTransformer(BaseFeatureTransformer):
    """
    Creates cyclical seasonal features from an epidemiological week.
    """

    def __init__(
        self,
        week_column: str = "epi_week",
        year_column: str = "epi_year",
    ) -> None:
        self.week_column = week_column
        self.year_column = year_column

    def transform(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        df = data.copy()
        required_columns = {
            self.week_column,
            self.year_column,
        }

        missing = required_columns - set(df.columns)

        if missing:
            raise KeyError(f"Missing required columns: {sorted(missing)}")

        periods = df[self.year_column].map(EpidemiologicalCalendar.weeks_in_year)

        angle = 2 * np.pi * df[self.week_column] / periods

        df["epi_week_sin"] = np.sin(angle)
        df["epi_week_cos"] = np.cos(angle)

        return df
