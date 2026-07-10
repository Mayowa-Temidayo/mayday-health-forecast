from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi

from mayday.core.paths import RAW_DATA_DIR
from mayday.core.settings import settings
from mayday.ingestion.base import BaseDataSource


class KaggleDataSource(BaseDataSource):
    """
    Downloads datasets from Kaggle.
    """

    def __init__(self) -> None:
        self.dataset = settings.kaggle.dataset

    def download(self) -> Path:
        api = KaggleApi()

        try:
            api.authenticate()

            api.dataset_download_files(
                dataset=self.dataset,
                path=RAW_DATA_DIR,
                unzip=True,
            )

        except Exception as exc:
            raise RuntimeError(f"Failed downloading dataset '{self.dataset}'.") from exc

        return RAW_DATA_DIR
