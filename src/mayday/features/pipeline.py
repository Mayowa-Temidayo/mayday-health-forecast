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
        self._transformers = transformers

    def run(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Apply every feature transformer in sequence.
        """

        dataset = data.copy()

        for transformer in self._transformers:
            dataset = transformer.transform(dataset)

        return dataset
