import pandas as pd


class DatasetValidator:
    """
    Validates datasets before training.
    """

    def validate(
        self,
        data: pd.DataFrame,
    ) -> None:

        if data.empty:
            raise ValueError("Dataset is empty.")

        if data.duplicated().any():
            raise ValueError("Duplicate rows detected.")
