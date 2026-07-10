from pathlib import Path

from mayday.ingestion.validator import DataValidator


def test_validator_accepts_existing_file(tmp_path: Path):
    file = tmp_path / "sample.csv"
    file.write_text("data")

    assert DataValidator.validate(file)


def test_validator_rejects_missing_file(tmp_path: Path):
    file = tmp_path / "missing.csv"

    assert not DataValidator.validate(file)


def test_validator_rejects_empty_file(tmp_path: Path):
    file = tmp_path / "empty.csv"
    file.touch()

    assert not DataValidator.validate(file)
