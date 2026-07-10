import pandas as pd

from mayday.core.paths import PROJECT_ROOT

METADATA_DIR = PROJECT_ROOT / "data" / "metadata"
STATES_FILE = METADATA_DIR / "states.csv"


def load_states() -> pd.DataFrame:
    """
    Load Nigerian state metadata.
    """
    if not STATES_FILE.exists():
        raise FileNotFoundError(f"{STATES_FILE} not found.")

    return pd.read_csv(STATES_FILE)
