from typing import cast

import pandas as pd


class TemporalAggregator:
    """
    Aggregate daily environmental observations into
    epidemiological weeks.
    """

    def aggregate(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        dataframe = dataframe.copy()

        iso = dataframe["date"].dt.isocalendar()

        dataframe["epi_year"] = iso.year.astype(int)
        dataframe["epi_week"] = iso.week.astype(int)

        weekly = dataframe.groupby(
            [
                "state",
                "epi_year",
                "epi_week",
            ],
            as_index=False,
        ).agg(
            precipitation_mm=("precipitation_mm", "sum"),
            temperature_c=("temperature_c", "mean"),
            relative_humidity=("relative_humidity", "mean"),
        )

        return cast(pd.DataFrame, weekly)
