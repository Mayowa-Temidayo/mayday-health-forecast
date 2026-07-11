import pytest

from mayday.ingestion.base import BaseDataSource


def test_base_datasource_cannot_be_instantiated() -> None:
    """The abstract base class cannot be instantiated directly."""
    with pytest.raises(TypeError):
        BaseDataSource()  # pyright: ignore[reportAbstractUsage]
