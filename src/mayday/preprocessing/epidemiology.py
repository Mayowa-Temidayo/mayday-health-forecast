import pandas as pd


class EpidemiologyPreprocessor:
    """
    Cleans epidemiological surveillance data.
    """

    DATE_COLUMNS = [
        "week_start_date",
        "week_end_date",
    ]

    NUMERIC_COLUMNS = [
        "suspected_cases",
        "confirmed_cases",
        "probable_cases",
        "deaths",
    ]

    def clean(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Clean the epidemiological dataset.
        """
        dataframe = dataframe.copy()

        # Parse dates
        for column in self.DATE_COLUMNS:
            dataframe[column] = pd.to_datetime(
                dataframe[column],
            )

        # Ensure numeric columns are numeric
        for column in self.NUMERIC_COLUMNS:
            dataframe[column] = pd.to_numeric(
                dataframe[column],
                errors="raise",
            )

        # Remove duplicate observations
        dataframe = dataframe.drop_duplicates()

        # Sort chronologically
        dataframe = dataframe.sort_values(
            by="week_start_date",
        )

        dataframe = dataframe.reset_index(drop=True)

        return dataframe
