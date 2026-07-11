from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Configuration
CONFIG_DIR = PROJECT_ROOT / "configs"

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

METADATA_DIR = PROJECT_ROOT / "data" / "metadata"

# Models
MODELS_DIR = PROJECT_ROOT / "models"

# Reports
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
FORECASTS_DIR = REPORTS_DIR / "forecasts"
EVALUATION_DIR = REPORTS_DIR / "evaluation"

# Notebooks
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

# Tests
TESTS_DIR = PROJECT_ROOT / "tests"

# Logs
LOGS_DIR = PROJECT_ROOT / "logs"

# Source
SRC_DIR = PROJECT_ROOT / "src"
PACKAGE_DIR = SRC_DIR / "mayday"

# Ensure required directories exist
REQUIRED_DIRECTORIES = [
    DATA_DIR,
    RAW_DATA_DIR,
    INTERIM_DATA_DIR,
    PROCESSED_DATA_DIR,
    EXTERNAL_DATA_DIR,
    MODELS_DIR,
    REPORTS_DIR,
    FIGURES_DIR,
    FORECASTS_DIR,
    EVALUATION_DIR,
    NOTEBOOKS_DIR,
    TESTS_DIR,
    LOGS_DIR,
]

for directory in REQUIRED_DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)
