import pandas as pd

from mayday.core.paths import METADATA_DIR


def load_state_coordinates() -> pd.DataFrame:
    """
    Load Nigerian state coordinates.
    """

    return pd.read_csv(METADATA_DIR / "nigeria_states.csv")
