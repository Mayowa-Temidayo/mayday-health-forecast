from mayday.preprocessing.environmental import (
    EnvironmentalPreprocessor,
)
from mayday.preprocessing.epidemiology import (
    EpidemiologyPreprocessor,
)
from mayday.preprocessing.io import (
    load_environmental,
    load_epidemiology,
)
from mayday.preprocessing.merge import (
    DatasetMerger,
)
from mayday.preprocessing.temporal import (
    TemporalAggregator,
)


def test_merge() -> None:
    epi = load_epidemiology()
    env = load_environmental()

    epi = EpidemiologyPreprocessor().clean(epi)

    env = EnvironmentalPreprocessor().clean(env)

    env = TemporalAggregator().aggregate(env)

    merged = DatasetMerger().merge(
        epi,
        env,
    )

    assert not merged.empty

    expected_columns = {
        "epi_year",
        "epi_week",
        "state",
        "precipitation_mm",
        "temperature_c",
        "relative_humidity",
    }

    assert expected_columns.issubset(merged.columns)

    # Merge keys should always exist
    assert merged[["epi_year", "epi_week"]].isna().sum().sum() == 0

    # Environmental variables should be populated
    assert bool(
        merged["temperature_c"].notna().all()
    ), "Temperature contains missing values."

    assert bool(
        merged["precipitation_mm"].notna().all()
    ), "Precipitation contains missing values."

    assert bool(
        merged["relative_humidity"].notna().all()
    ), "Relative humidity contains missing values."
