from pathlib import Path

from mayday.ingestion.utils.downloader import Downloader


class DataIngestionPipeline:
    """
    Executes the complete ingestion workflow.
    """

    def __init__(self, downloader: Downloader):
        self.downloader = downloader

    def run(self) -> list[Path]:
        downloaded_files = self.downloader.download_all()

        prepared_files: list[Path] = []

        for source, downloaded in zip(
            self.downloader.sources,
            downloaded_files,
        ):
            extracted = source.extract(downloaded)

            if not source.validate(extracted):
                raise RuntimeError(f"Validation failed for {downloaded}")

            prepared = source.prepare(extracted)

            prepared_files.append(prepared)

        return prepared_files
