from pathlib import Path

from mayday.ingestion.base import BaseDataSource
from mayday.ingestion.utils.downloader import Downloader
from mayday.ingestion.pipeline import DataIngestionPipeline


class DummySource(BaseDataSource):
    def download(self) -> Path:
        path = Path("dummy.csv")
        path.write_text("test")
        return path


def test_pipeline():
    downloader = Downloader([DummySource()])

    pipeline = DataIngestionPipeline(downloader)

    files = pipeline.run()

    assert len(files) == 1

    Path("dummy.csv").unlink()
