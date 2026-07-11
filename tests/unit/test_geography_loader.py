from mayday.geography.loader import load_state_coordinates


def test_load_state_coordinates() -> None:
    df = load_state_coordinates()

    assert len(df) == 37
    assert "state" in df.columns
    assert "latitude" in df.columns
    assert "longitude" in df.columns
