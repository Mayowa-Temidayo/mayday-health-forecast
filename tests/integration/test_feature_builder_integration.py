import pandas as pd

from mayday.features.builder import (
    build_feature_pipeline,
)


def test_feature_pipeline() -> None:
    df = pd.DataFrame(
        {
            "epi_year": [2020] * 8,
            "epi_week": list(range(1, 9)),
            "confirmed_cases": [
                10,
                12,
                15,
                20,
                25,
                30,
                28,
                26,
            ],
            "T2M": [25.0] * 8,
            "PRECTOTCORR": [0, 1, 0, 2, 3, 0, 0, 5],
        }
    )

    pipeline = build_feature_pipeline()

    result = pipeline.run(df)

    expected = [
        "confirmed_cases_lag_1",
        "confirmed_cases_lag_2",
        "confirmed_cases_lag_4",
        "confirmed_cases_lag_8",
        "confirmed_cases_rolling_mean_2",
        "confirmed_cases_rolling_mean_4",
        "confirmed_cases_rolling_mean_8",
        "epi_week_sin",
        "epi_week_cos",
        "T2M_K",
        "is_rainy_day",
    ]

    for column in expected:
        assert column in result.columns
