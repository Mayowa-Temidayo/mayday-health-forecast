from mayday.core.settings import settings


def test_forecast_horizon():
    assert settings.forecast.horizon == 12