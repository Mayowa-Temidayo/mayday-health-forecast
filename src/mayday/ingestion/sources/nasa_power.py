from pathlib import Path

import pandas as pd

from mayday.core.paths import EXTERNAL_DATA_DIR
from mayday.geography.loader import load_state_coordinates
from mayday.ingestion.clients.nasa_power import NasaPowerClient
from mayday.ingestion.utils.json_to_dataframe import power_json_to_dataframe


class NasaPowerDataSource(BaseDataSource):
    """
    Downloads environmental variables from the NASA POWER API.
    """

    def __init__(self) -> None:
        self.client = NasaPowerClient()

    def download(self) -> Path:
        """
        Download NASA POWER data for every Nigerian state.
        """

        output_dir = EXTERNAL_DATA_DIR / "nasa_power"
        output_dir.mkdir(parents=True, exist_ok=True)

        states = load_state_coordinates()

        dataframes: list[pd.DataFrame] = []

        for _, state in states.iterrows():
            response = self.client.get_daily_data(
                latitude=state["latitude"],
                longitude=state["longitude"],
            )

            df = power_json_to_dataframe(response)

            df["state"] = state["state"]

            dataframes.append(df)

        final_df = pd.concat(dataframes, ignore_index=True)

        output_file = output_dir / "nasa_power_daily.csv"

        final_df.to_csv(output_file, index=False)

        return output_file

    def extract(self, source: Path) -> Path:
        return source

    def validate(self, source: Path) -> bool:
        return source.exists() and source.stat().st_size > 0

    def prepare(self, source: Path) -> Path:
        return source
