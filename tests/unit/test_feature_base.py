import pytest

from mayday.features.base import BaseFeatureTransformer


def test_base_feature_transformer_cannot_be_instantiated() -> None:
    with pytest.raises(TypeError):
        BaseFeatureTransformer()  # pyright: ignore[reportAbstractUsage]
