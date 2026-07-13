from mayday.ingestion.sources.nasa_power import NasaPowerDataSource


def test_nasa_datasource_exists() -> None:
    datasource = NasaPowerDataSource()

    assert datasource is not None
