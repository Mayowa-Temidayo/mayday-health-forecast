import pandas as pd

from mayday.features.base import GroupedFeatureTransformer


class LagFeatureTransformer(GroupedFeatureTransformer):
    """
    Creates lag features for a target column.
    """

    def __init__(
        self,
        target_column: str,
        lags: list[int],
        group_by: list[str] | None = None,
    ) -> None:
        super().__init__(group_by)

        self.target_column = target_column
        self.lags = sorted(lags)

    def transform(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Create lagged features.
        """
        df = data.copy()

        for lag in self.lags:
            column_name = f"{self.target_column}_lag_{lag}"

            if self.has_groups:
                df[column_name] = df.groupby(self.group_by)[self.target_column].shift(
                    lag
                )
            else:
                df[column_name] = df[self.target_column].shift(lag)

        return df
