import pytest

from mayday.ingestion.sources.kaggle import KaggleDataSource


@pytest.mark.integration
def test_kaggle_download():
    datasource = KaggleDataSource()

    path = datasource.download()

    assert path.exists()
