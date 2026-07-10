import pytest

from mayday.ingestion.kaggle import KaggleDataSource


@pytest.mark.integration
def test_kaggle_download():
    datasource = KaggleDataSource()

    path = datasource.download()

    assert path.exists()
