"""
Custom exceptions used throughout the project.
"""


class MayDayError(Exception):
    """
    Base exception for the project.
    """


class DatasetError(MayDayError):
    """
    Base exception for dataset-related errors.
    """


class DatasetFormatUnavailableError(DatasetError):
    """
    Raised when a dataset format is unavailable on
    the current platform.
    """


class DatasetValidationError(DatasetError):
    """
    Raised when dataset validation fails.
    """
