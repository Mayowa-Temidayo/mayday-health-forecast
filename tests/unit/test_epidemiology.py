from mayday.preprocessing.epidemiology import EpidemiologyPreprocessor
from mayday.preprocessing.io import load_epidemiology


def test_clean_epidemiology() -> None:
    df = load_epidemiology()

    cleaned = EpidemiologyPreprocessor().clean(df)

    assert not cleaned.empty

    # Dates should be parsed
    assert cleaned["week_start_date"].dtype.kind == "M"
    assert cleaned["week_end_date"].dtype.kind == "M"

    # No duplicate rows
    assert cleaned.duplicated().sum() == 0

    # Current source dataset should not lose rows
    assert len(cleaned) == len(df)

    # Chronological order
    assert cleaned["week_start_date"].is_monotonic_increasing

    # Required columns must exist
    expected_columns = {
        "week_start_date",
        "week_end_date",
        "epi_year",
        "epi_week",
        "suspected_cases",
        "confirmed_cases",
        "probable_cases",
        "deaths",
    }

    assert expected_columns.issubset(cleaned.columns)
