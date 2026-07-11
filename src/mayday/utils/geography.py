import pandas as pd

from mayday.core.paths import METADATA_DIR


def load_state_coordinates() -> pd.DataFrame:
    """
    Load latitude and longitude for Nigerian states.
    """
    file = METADATA_DIR / "state_coordinates.csv"

    return pd.read_csv(file)
