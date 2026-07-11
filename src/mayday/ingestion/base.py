from abc import ABC, abstractmethod
from pathlib import Path


class BaseDataSource(ABC):
    """Abstract interface for every external data source."""

    @abstractmethod
    def download(self) -> Path:
        """Download the raw source."""
        raise NotImplementedError

    @abstractmethod
    def extract(self, source: Path) -> Path:
        """Extract the downloaded content if necessary."""
        raise NotImplementedError

    @abstractmethod
    def validate(self, source: Path) -> bool:
        """Validate the extracted data."""
        raise NotImplementedError

    @abstractmethod
    def prepare(self, source: Path) -> Path:
        """Prepare the dataset for downstream processing."""
        raise NotImplementedError
