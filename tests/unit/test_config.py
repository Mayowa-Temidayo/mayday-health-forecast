from mayday.core.config import load_config


def test_load_config():
    config = load_config()

    assert isinstance(config, dict)

    assert "forecast" in config
