import pandas as pd


class DatasetMerger:
    """
    Merge epidemiological and environmental datasets.

    Notes
    -----
    The current epidemiological dataset is national-level, so the merge
    is performed using epidemiological year and week only.

    When state-level surveillance data becomes available, simply add
    "state" to MERGE_KEYS.
    """

    MERGE_KEYS = (
        "epi_year",
        "epi_week",
    )

    def merge(
        self,
        epidemiology: pd.DataFrame,
        environmental: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Merge cleaned epidemiological and environmental datasets.
        """

        merged = epidemiology.merge(
            environmental,
            on=list(self.MERGE_KEYS),
            how="left",
            validate="one_to_many",
        )

        merged = merged.sort_values(
            [
                *self.MERGE_KEYS,
                "state",
            ]
        ).reset_index(drop=True)

        return merged
