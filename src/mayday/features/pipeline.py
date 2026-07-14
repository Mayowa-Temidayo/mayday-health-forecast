import pandas as pd

from mayday.features.base import BaseFeatureTransformer


class FeaturePipeline:
    """
    Sequentially applies feature transformers.
    """

    def __init__(
        self,
        transformers: list[BaseFeatureTransformer],
    ) -> None:
        self.transformers = transformers

    def run(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Apply each transformer in sequence.
        """
        df = data.copy()

        for transformer in self.transformers:
            df = transformer.transform(df)

        return df
