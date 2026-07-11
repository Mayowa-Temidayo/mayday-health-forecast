from mayday.ingestion.clients.nasa_power import NasaPowerClient


def test_client_creation() -> None:
    client = NasaPowerClient()

    assert client is not None

    client.close()
