from typing import Any

from mayday.core.settings import settings
from mayday.ingestion.clients.http import HTTPClient


class NasaPowerClient:
    """
    Client for interacting with the NASA POWER API.
    """

    def __init__(self) -> None:
        self.config = settings.nasa_power
        self.http = HTTPClient()

    def _build_params(
        self,
        latitude: float,
        longitude: float,
    ) -> dict[str, Any]:
        return {
            "parameters": ",".join(self.config.parameters),
            "community": self.config.community,
            "longitude": longitude,
            "latitude": latitude,
            "start": f"{self.config.start_year}0101",
            "end": f"{self.config.end_year}1231",
            "format": self.config.format,
        }

    def get_point_data(
        self,
        latitude: float,
        longitude: float,
    ) -> dict[str, Any]:
        params = self._build_params(
            latitude=latitude,
            longitude=longitude,
        )

        return self.http.get(
            self.config.base_url,
            params=params,
        )

    def get_states_data(
        self,
        coordinates,
    ) -> dict[str, dict]:
        results: dict[str, dict] = {}

        for _, row in coordinates.iterrows():
            results[row["state"]] = self.get_point_data(
                latitude=row["latitude"],
                longitude=row["longitude"],
            )

        return results

    def close(self) -> None:
        self.http.close()
