from pydantic import BaseModel

from mayday.core.config import load_config


class ForecastSettings(BaseModel):
    horizon: int
    frequency: str
    random_seed: int
    train_ratio: float


class KaggleSettings(BaseModel):
    dataset: str


class NASAPowerSettings(BaseModel):
    base_url: str
    community: str
    parameters: list[str]
    format: str
    start: str
    end: str


class DataSettings(BaseModel):
    raw: str
    interim: str
    processed: str
    external: str
    downloads: str
    metadata: str


class LoggingSettings(BaseModel):
    level: str


class Settings(BaseModel):
    forecast: ForecastSettings
    kaggle: KaggleSettings
    nasa_power: NASAPowerSettings
    data: DataSettings
    logging: LoggingSettings


settings = Settings(**load_config())
