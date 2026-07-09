from abc import ABC, abstractmethod
from pathlib import Path


class BaseDataSource(ABC):
    """Abstract base class for all data sources."""

    @abstractmethod
    def download(self) -> Path:
        """Download data and return the local file path."""
        raise NotImplementedError
