from pathlib import Path


class DataValidator:
    """
    Performs basic validation on downloaded datasets.
    """

    @staticmethod
    def validate(path: Path) -> bool:
        if not path.exists():
            return False

        if path.stat().st_size == 0:
            return False

        return True
