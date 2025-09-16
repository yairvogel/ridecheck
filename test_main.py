import pytest

from main import calculate_minutes


@pytest.mark.parametrize(
    "mopeds,distance,expected",
    [
        # simple, single moped cases
        (["S"], [], 1),
        (["F"], [], 5),
        (["M"], [], 8),
        # multiple mopeds
        (["S", "F"], [2], 1 + 2 + 5),
        (["M", "F"], [10], 8 + 10 + 5),
        (["F", "F", "F"], [10, 1], 5 + 10 + 5 + 1 + 5),
        (["S", "F", "SF", "FF"], [2, 4, 3], 37),  # First example from case.md
        (["MMM", "SMF", "FMS"], [3, 10], 91),  # Second example from case.md
        (
            ["MS", "SFF", "MS", "S", "FM", "MMMM", "FF"],
            [4, 17, 3, 6, 9, 11],
            198,
        ),  # Third example from case.md
        # Mopeds without treatments
        (["", "", "M"], [1, 2], 11),
        # Multiple tasks at same moped (all roles present):
        (["SSFFMM"], [], 28),
        (["", "SMF"], [10], 44),
    ],
)
def test_calculate_minutes(mopeds: list[str], distance: list[int], expected: int):
    res = calculate_minutes(mopeds, distance)
    assert res == expected
