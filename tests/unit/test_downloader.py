from pathlib import Path

from mayday.ingestion.base import BaseDataSource
from mayday.ingestion.downloader import Downloader


class DummySource(BaseDataSource):
    def download(self) -> Path:
        return Path("dummy.csv")


def test_downloader():
    downloader = Downloader([DummySource()])

    files = downloader.download_all()

    assert len(files) == 1
    assert files[0].name == "dummy.csv"
