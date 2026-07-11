from mayday.geography.loader import load_state_coordinates


def test_number_of_states() -> None:
    df = load_state_coordinates()

    assert len(df) == 37
