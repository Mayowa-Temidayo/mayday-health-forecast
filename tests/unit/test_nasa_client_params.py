from mayday.ingestion.clients.nasa_power import NasaPowerClient


def test_build_params() -> None:
    client = NasaPowerClient()

    params = client._build_params(
        latitude=6.5244,
        longitude=3.3792,
    )

    assert params["latitude"] == 6.5244
    assert params["longitude"] == 3.3792

    assert params["start"] == "20200101"
    assert params["end"] == "20251231"

    assert params["community"] == "AG"
    assert "PRECTOTCORR" in params["parameters"]

    client.close()
