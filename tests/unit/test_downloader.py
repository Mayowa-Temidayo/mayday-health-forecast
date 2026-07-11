from pathlib import Path

from mayday.ingestion.base import BaseDataSource
from mayday.ingestion.utils.downloader import Downloader


class DummySource(BaseDataSource):
    def download(self) -> Path:
        return Path("dummy.csv")

    def extract(self, source: Path) -> Path:
        return source

    def validate(self, source: Path) -> bool:
        return True

    def prepare(self, source: Path) -> Path:
        return source


def test_downloader() -> None:
    downloader = Downloader([DummySource()])

    files = downloader.download_all()

    assert len(files) == 1
    assert files[0].name == "dummy.csv"
