from abc import ABC, abstractmethod

import pandas as pd


class BaseFeatureTransformer(ABC):
    """
    Base interface for all feature transformers.
    """

    @abstractmethod
    def transform(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        raise NotImplementedError


class GroupedFeatureTransformer(BaseFeatureTransformer):
    """
    Base class for feature transformers that optionally operate
    within groups (for example, one Nigerian state at a time).
    """

    def __init__(
        self,
        group_by: list[str] | None = None,
    ) -> None:
        self.group_by = group_by or []

    @property
    def has_groups(self) -> bool:
        return len(self.group_by) > 0
