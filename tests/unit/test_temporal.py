from mayday.preprocessing.environmental import (
    EnvironmentalPreprocessor,
)
from mayday.preprocessing.io import (
    load_environmental,
)
from mayday.preprocessing.temporal import (
    TemporalAggregator,
)


def test_temporal_aggregation() -> None:
    environmental = load_environmental()

    cleaned = EnvironmentalPreprocessor().clean(environmental)

    weekly = TemporalAggregator().aggregate(cleaned)

    assert not weekly.empty

    expected_columns = {
        "state",
        "epi_year",
        "epi_week",
        "precipitation_mm",
        "temperature_c",
        "relative_humidity",
    }

    assert expected_columns.issubset(weekly.columns)

    assert weekly.duplicated(subset=["state", "epi_year", "epi_week"]).sum() == 0
