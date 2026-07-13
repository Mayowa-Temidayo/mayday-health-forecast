import pandas as pd

from mayday.preprocessing.pipeline import PreprocessingPipeline


def test_preprocessing_pipeline() -> None:
    pipeline = PreprocessingPipeline()

    output = pipeline.run()

    assert output.exists()

    df = pd.read_csv(output)

    assert not df.empty

    expected_columns = {
        "epi_year",
        "epi_week",
        "state",
        "temperature_c",
        "precipitation_mm",
        "relative_humidity",
        "confirmed_cases",
    }

    assert expected_columns.issubset(df.columns)

    assert bool(df["temperature_c"].notna().all())
    assert bool(df["precipitation_mm"].notna().all())
    assert bool(df["relative_humidity"].notna().all())
