import pandas as pd

from mayday.features.rolling import RollingFeatureTransformer


def test_rolling_mean() -> None:
    df = pd.DataFrame(
        {
            "confirmed_cases": [10, 20, 30, 40],
        }
    )

    transformer = RollingFeatureTransformer(
        target_column="confirmed_cases",
        windows=[2],
    )

    result = transformer.transform(df)

    column = "confirmed_cases_rolling_mean_2"

    assert column in result.columns

    assert pd.isna(result.loc[0, column])

    assert result.loc[1, column] == 15

    assert result.loc[2, column] == 25


def test_grouped_rolling_mean() -> None:
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

    transformer = RollingFeatureTransformer(
        target_column="confirmed_cases",
        windows=[2],
        group_by=["state"],
    )

    result = transformer.transform(df)

    column = "confirmed_cases_rolling_mean_2"

    assert pd.isna(result.loc[0, column])

    assert result.loc[1, column] == 15

    assert result.loc[2, column] == 25

    assert pd.isna(result.loc[3, column])

    assert result.loc[4, column] == 150

    assert result.loc[5, column] == 250
