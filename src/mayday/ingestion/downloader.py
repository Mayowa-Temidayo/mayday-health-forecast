from pathlib import Path

from mayday.ingestion.base import BaseDataSource


class Downloader:
    """
    Coordinates downloads from one or more data sources.
    """

    def __init__(self, sources: list[BaseDataSource]) -> None:
        self.sources = sources

    def download_all(self) -> list[Path]:
        downloaded_files: list[Path] = []

        for source in self.sources:
            downloaded_files.append(source.download())

        return downloaded_files
