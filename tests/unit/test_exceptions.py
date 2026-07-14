from mayday.core.exceptions import (
    DatasetError,
    DatasetFormatUnavailableError,
    DatasetValidationError,
    MayDayError,
)


def test_exception_hierarchy() -> None:
    """
    Custom exceptions should inherit from the expected base classes.
    """

    assert issubclass(MayDayError, Exception)
    assert issubclass(DatasetError, MayDayError)
    assert issubclass(
        DatasetFormatUnavailableError,
        DatasetError,
    )
    assert issubclass(
        DatasetValidationError,
        DatasetError,
    )
