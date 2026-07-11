from pathlib import Path
from zipfile import ZipFile

from kaggle.api.kaggle_api_extended import KaggleApi

from mayday.core.paths import RAW_DATA_DIR
from mayday.core.settings import settings
from mayday.ingestion.base import BaseDataSource
from mayday.ingestion.utils.discovery import DatasetDiscovery


class KaggleDataSource(BaseDataSource):
    """
    Downloads epidemiological datasets from Kaggle.
    """

    def __init__(self) -> None:
        self.dataset = settings.kaggle.dataset
        self.download_path = RAW_DATA_DIR

    def download(self) -> Path:
        """
        Download the Kaggle dataset as a ZIP archive.
        """
        api = KaggleApi()

        try:
            api.authenticate()

            api.dataset_download_files(
                dataset=self.dataset,
                path=self.download_path,
                unzip=False,
            )

        except Exception as exc:
            raise RuntimeError(f"Failed downloading dataset '{self.dataset}'.") from exc

        dataset_name = self.dataset.split("/")[-1]

        zip_path = self.download_path / f"{dataset_name}.zip"

        if not zip_path.exists():
            raise FileNotFoundError(
                f"Expected downloaded archive was not found: {zip_path}"
            )

        return zip_path

    def extract(self, source: Path) -> Path:
        """
        Extract the downloaded archive and locate the primary dataset.
        """
        with ZipFile(source, "r") as archive:
            archive.extractall(self.download_path)

        discovery = DatasetDiscovery(self.download_path)

        return discovery.find_primary_dataset()

    def validate(self, source: Path) -> bool:
        """
        Validate that the extracted dataset exists and is a CSV file.
        """
        return source.exists() and source.suffix.lower() == ".csv"

    def prepare(self, source: Path) -> Path:
        """
        Final preparation step.

        Future preprocessing (renaming columns, schema validation,
        type coercion, etc.) will occur here.
        """
        return source
