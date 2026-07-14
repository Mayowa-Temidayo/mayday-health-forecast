from collections.abc import Mapping


class EpidemiologicalCalendar:
    """
    Provides epidemiological calendar information.
    """

    _weeks_per_year: Mapping[int, int] = {
        2020: 53,
        2021: 52,
        2022: 52,
        2023: 52,
        2024: 52,
        2025: 52,
    }

    @classmethod
    def weeks_in_year(
        cls,
        year: int,
    ) -> int:
        return cls._weeks_per_year.get(year, 52)
