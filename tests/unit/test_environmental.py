from mayday.preprocessing.environmental import (
    EnvironmentalPreprocessor,
)
from mayday.preprocessing.io import (
    load_environmental,
)


def test_clean_environmental() -> None:
    df = load_environmental()

    cleaned = EnvironmentalPreprocessor().clean(df)

    assert not cleaned.empty

    assert cleaned["date"].dtype.kind == "M"

    assert cleaned.duplicated().sum() == 0

    assert cleaned["state"].isna().sum() == 0

    expected_columns = {
        "state",
        "date",
        "precipitation_mm",
        "temperature_c",
        "relative_humidity",
    }

    assert expected_columns.issubset(cleaned.columns)
