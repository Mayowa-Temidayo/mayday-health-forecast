from pydantic import BaseModel

from mayday.core.config import load_config


class ForecastSettings(BaseModel):
    horizon: int
    frequency: str
    random_seed: int


class Settings(BaseModel):
    forecast: ForecastSettings


settings = Settings(**load_config())
