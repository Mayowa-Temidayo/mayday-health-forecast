import yaml

from mayday.core.paths import CONFIG_DIR

CONFIG_FILE = CONFIG_DIR / "config.yaml"


def load_config() -> dict:
    """
    Load the application configuration from YAML.
    """
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"Configuration file not found: {CONFIG_FILE}")

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)
