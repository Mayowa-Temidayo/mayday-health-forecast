from pathlib import Path

import pandas as pd

from mayday.core.paths import NASA_POWER_DIR
from mayday.geography.loader import load_state_coordinates
from mayday.ingestion.base import BaseDataSource
from mayday.ingestion.clients.nasa_power import NasaPowerClient


class NasaPowerDataSource(BaseDataSource):
    """
    Downloads daily environmental variables from NASA POWER.
    """

    def __init__(self) -> None:
        self.client = NasaPowerClient()

        self.output_file = NASA_POWER_DIR / "nasa_power_daily.csv"

    def download(self) -> Path:
        """
        Download NASA POWER data for every Nigerian state.
        """
        coordinates = load_state_coordinates()

        results = self.client.get_states_data(coordinates)

        rows: list[dict] = []

        for state, payload in results.items():
            parameters = payload["properties"]["parameter"]

            dates = next(iter(parameters.values())).keys()

            for date in dates:
                row = {
                    "state": state,
                    "date": date,
                }

                for variable, values in parameters.items():
                    row[variable] = values.get(date)

                rows.append(row)

        dataframe = pd.DataFrame(rows)

        dataframe.to_csv(
            self.output_file,
            index=False,
        )

        return self.output_file

    def extract(self, source: Path) -> Path:
        return source

    def validate(self, source: Path) -> bool:
        return source.exists()

    def prepare(self, source: Path) -> Path:
        return source

    def close(self) -> None:
        self.client.close()
