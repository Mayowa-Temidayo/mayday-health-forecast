from mayday.ingestion.clients.nasa_power import NasaPowerClient
from mayday.ingestion.sources.nasa_power import NasaPowerDataSource


def test_nasa_datasource_has_client() -> None:
    datasource = NasaPowerDataSource()

    assert isinstance(datasource.client, NasaPowerClient)

    datasource.client.close()
