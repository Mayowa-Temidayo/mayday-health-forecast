from dataclasses import dataclass


@dataclass(slots=True)
class Coordinate:
    latitude: float
    longitude: float


@dataclass(slots=True)
class StateCoordinate:
    state: str
    latitude: float
    longitude: float
