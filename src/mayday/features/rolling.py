import pandas as pd

from mayday.features.base import GroupedFeatureTransformer


class RollingFeatureTransformer(GroupedFeatureTransformer):
    """
    Creates rolling statistical features.
    """

    def __init__(
        self,
        target_column: str,
        windows: list[int],
        statistic: str = "mean",
        group_by: list[str] | None = None,
    ) -> None:
        super().__init__(group_by)

        self.target_column = target_column
        self.windows = sorted(windows)
        self.statistic = statistic

    def transform(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Create rolling statistical features.
        """
        df = data.copy()

        for window in self.windows:
            column_name = f"{self.target_column}_rolling_{self.statistic}_{window}"

            if self.has_groups:
                rolling = df.groupby(self.group_by)[self.target_column].rolling(window)

                if self.statistic == "mean":
                    values = rolling.mean()

                elif self.statistic == "sum":
                    values = rolling.sum()

                else:
                    raise ValueError(f"Unsupported statistic: {self.statistic}")

                df[column_name] = pd.Series(values).reset_index(
                    level=self.group_by, drop=True
                )

            else:
                rolling = df[self.target_column].rolling(window)

                if self.statistic == "mean":
                    df[column_name] = rolling.mean()

                elif self.statistic == "sum":
                    df[column_name] = rolling.sum()

                else:
                    raise ValueError(f"Unsupported statistic: {self.statistic}")

        return df
