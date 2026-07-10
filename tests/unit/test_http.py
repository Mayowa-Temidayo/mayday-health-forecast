from mayday.ingestion.clients.http import HTTPClient


def test_http_client_creation():
    client = HTTPClient()

    assert client.client is not None

    client.close()
