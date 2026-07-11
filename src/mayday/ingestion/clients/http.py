from typing import Any

import httpx


class HTTPClient:
    """
    Lightweight HTTP client wrapper.
    """

    def __init__(self, timeout: float = 30.0):
        self.client = httpx.Client(timeout=timeout)

    def get(
        self,
        url: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        response = self.client.get(
            url,
            params=params,
        )

        response.raise_for_status()

        return response.json()

    def close(self) -> None:
        self.client.close()
