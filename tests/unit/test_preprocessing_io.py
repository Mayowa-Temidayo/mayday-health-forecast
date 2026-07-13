from mayday.preprocessing.io import (
    load_environmental,
    load_epidemiology,
)


def test_load_epidemiology() -> None:
    dataframe = load_epidemiology()

    assert not dataframe.empty


def test_load_environmental() -> None:
    dataframe = load_environmental()

    assert not dataframe.empty
