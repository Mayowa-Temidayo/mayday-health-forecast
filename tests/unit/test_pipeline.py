from pathlib import Path

from mayday.ingestion.base import BaseDataSource
from mayday.ingestion.pipeline import DataIngestionPipeline
from mayday.ingestion.utils.downloader import Downloader


class DummySource(BaseDataSource):
    def download(self) -> Path:
        path = Path("dummy.csv")
        path.write_text("test")
        return path

    def extract(self, source: Path) -> Path:
        return source

    def validate(self, source: Path) -> bool:
        return True

    def prepare(self, source: Path) -> Path:
        return source


def test_pipeline() -> None:
    downloader = Downloader([DummySource()])

    pipeline = DataIngestionPipeline(downloader)

    files = pipeline.run()

    assert len(files) == 1
    assert files[0].name == "dummy.csv"

    Path("dummy.csv").unlink()
