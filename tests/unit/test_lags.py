import pandas as pd

from mayday.features.lags import LagFeatureTransformer


def test_single_lag() -> None:
    df = pd.DataFrame(
        {
            "confirmed_cases": [10, 20, 30, 40],
        }
    )

    transformer = LagFeatureTransformer(
        target_column="confirmed_cases",
        lags=[1],
    )

    result = transformer.transform(df)

    assert "confirmed_cases_lag_1" in result.columns

    assert pd.isna(result.loc[0, "confirmed_cases_lag_1"])

    assert result.loc[1, "confirmed_cases_lag_1"] == 10

    assert result.loc[2, "confirmed_cases_lag_1"] == 20


def test_multiple_lags() -> None:
    df = pd.DataFrame(
        {
            "confirmed_cases": [5, 10, 15, 20, 25],
        }
    )

    transformer = LagFeatureTransformer(
        target_column="confirmed_cases",
        lags=[1, 2],
    )

    result = transformer.transform(df)

    assert "confirmed_cases_lag_1" in result.columns
    assert "confirmed_cases_lag_2" in result.columns

    assert result.loc[3, "confirmed_cases_lag_1"] == 15

    assert result.loc[3, "confirmed_cases_lag_2"] == 10


def test_grouped_lag() -> None:
    df = pd.DataFrame(
        {
            "state": [
                "Abia",
                "Abia",
                "Abia",
                "Adamawa",
                "Adamawa",
                "Adamawa",
            ],
            "confirmed_cases": [
                10,
                20,
                30,
                100,
                200,
                300,
            ],
        }
    )

    transformer = LagFeatureTransformer(
        target_column="confirmed_cases",
        lags=[1],
        group_by=["state"],
    )

    result = transformer.transform(df)

    assert pd.isna(result.loc[0, "confirmed_cases_lag_1"])

    assert result.loc[1, "confirmed_cases_lag_1"] == 10

    assert result.loc[2, "confirmed_cases_lag_1"] == 20

    assert pd.isna(result.loc[3, "confirmed_cases_lag_1"])

    assert result.loc[4, "confirmed_cases_lag_1"] == 100

    assert result.loc[5, "confirmed_cases_lag_1"] == 200
