from pathlib import Path


class DatasetDiscovery:
    """Locate datasets within a directory."""

    def __init__(self, root: Path) -> None:
        self.root = root

    def find_csv_files(self) -> list[Path]:
        """Return every CSV found recursively."""
        return sorted(self.root.rglob("*.csv"))

    def find_primary_dataset(self) -> Path:
        """
        Return the primary dataset.

        Raises:
            FileNotFoundError:
                If no CSV files are found.
        """
        csv_files = self.find_csv_files()

        if not csv_files:
            raise FileNotFoundError(f"No CSV files found in {self.root}")

        return csv_files[0]
