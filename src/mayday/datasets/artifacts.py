from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path


@dataclass(slots=True, frozen=True)
class DatasetMetadata:
    """
    Describes the contents of a dataset.
    """

    rows: int
    columns: int
    feature_count: int
    target: str


@dataclass(slots=True, frozen=True)
class DatasetArtifact:
    """
    Represents a persisted dataset artifact.
    """

    name: str
    path: Path
    format: str
    metadata: DatasetMetadata
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
