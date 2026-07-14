from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

from mayday.models.metrics import ForecastMetrics


@dataclass(slots=True, frozen=True)
class ModelArtifact:
    """
    Represents a trained forecasting model.
    """

    name: str

    path: Path

    metrics: ForecastMetrics

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )
