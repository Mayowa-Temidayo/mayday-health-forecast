from pathlib import Path

from mayday.ingestion.utils.downloader import Downloader
from mayday.ingestion.utils.validator import DataValidator


class DataIngestionPipeline:
    """
    Executes the complete ingestion workflow.
    """

    def __init__(self, downloader: Downloader):
        self.downloader = downloader

    def run(self) -> list[Path]:
        downloaded = self.downloader.download_all()

        valid_files: list[Path] = []

        for file in downloaded:
            if DataValidator.validate(file):
                valid_files.append(file)

        return valid_files
