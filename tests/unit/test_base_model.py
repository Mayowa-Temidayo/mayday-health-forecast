import pytest
from typing import Any, cast

from mayday.models.base import BaseForecastModel


def test_base_model_is_abstract() -> None:
    """
    BaseForecastModel cannot be instantiated.
    """

    AbstractModel = cast(Any, BaseForecastModel)

    with pytest.raises(TypeError):
        AbstractModel()
