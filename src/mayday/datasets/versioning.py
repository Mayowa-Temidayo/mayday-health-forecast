from pathlib import Path

from mayday.core.paths import PROCESSED_DATA_DIR


class DatasetVersionManager:
    """
    Manages versioned dataset names.
    """

    def __init__(
        self,
        directory: Path = PROCESSED_DATA_DIR,
    ) -> None:
        self.directory = directory

    def next_version(
        self,
        prefix: str = "modeling_dataset",
    ) -> int:
        """
        Returns the next dataset version.
        """

        versions: list[int] = []

        for file in self.directory.glob(f"{prefix}_v*.csv"):
            stem = file.stem

            try:
                version = int(stem.split("_v")[-1])
                versions.append(version)

            except ValueError:
                continue

        if not versions:
            return 1

        return max(versions) + 1
