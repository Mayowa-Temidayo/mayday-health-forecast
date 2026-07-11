import pytest

from mayday.ingestion.sources.nasa_power import NasaPowerDataSource


@pytest.mark.integration
def test_download():
    datasource = NasaPowerDataSource()

    file = datasource.download()

    assert file.exists()
