import pandas as pd


class EnvironmentalPreprocessor:
    """
    Cleans NASA POWER environmental data.
    """

    COLUMN_MAPPING = {
        "PRECTOTCORR": "precipitation_mm",
        "T2M": "temperature_c",
        "RH2M": "relative_humidity",
    }

    NUMERIC_COLUMNS = [
        "precipitation_mm",
        "temperature_c",
        "relative_humidity",
    ]

    def clean(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        dataframe = dataframe.copy()

        dataframe["date"] = pd.to_datetime(
            dataframe["date"],
            format="%Y%m%d",
        )

        dataframe = dataframe.rename(
            columns=self.COLUMN_MAPPING,
        )

        for column in self.NUMERIC_COLUMNS:
            dataframe[column] = pd.to_numeric(
                dataframe[column],
                errors="raise",
            )

        dataframe = dataframe.drop_duplicates()

        dataframe = dataframe.sort_values(
            ["state", "date"],
        )

        dataframe = dataframe.reset_index(drop=True)

        return dataframe
