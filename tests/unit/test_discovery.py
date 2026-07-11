from pathlib import Path

import pytest

from mayday.ingestion.utils.discovery import DatasetDiscovery


def test_find_csv_files(tmp_path: Path) -> None:
    (tmp_path / "a.csv").write_text("a")
    (tmp_path / "b.csv").write_text("b")
    (tmp_path / "notes.txt").write_text("ignore")

    discovery = DatasetDiscovery(tmp_path)

    files = discovery.find_csv_files()

    assert len(files) == 2


def test_find_primary_dataset(tmp_path: Path) -> None:
    (tmp_path / "dataset.csv").write_text("test")

    discovery = DatasetDiscovery(tmp_path)

    dataset = discovery.find_primary_dataset()

    assert dataset.name == "dataset.csv"


def test_find_primary_dataset_raises(tmp_path: Path) -> None:
    discovery = DatasetDiscovery(tmp_path)

    with pytest.raises(FileNotFoundError):
        discovery.find_primary_dataset()
