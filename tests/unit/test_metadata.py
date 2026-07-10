from mayday.utils.metadata import load_states


def test_load_states():
    df = load_states()

    assert len(df) == 37

    assert "state" in df.columns
    assert "latitude" in df.columns
    assert "longitude" in df.columns
