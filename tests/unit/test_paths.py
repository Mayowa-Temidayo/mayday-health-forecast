from mayday.core.paths import PROJECT_ROOT, RAW_DATA_DIR


def test_project_root_exists():
    assert PROJECT_ROOT.exists()


def test_raw_directory_exists():
    assert RAW_DATA_DIR.exists()
