import pytest

from main import calculate_minutes


@pytest.mark.parametrize(
    "mopeds,distance,expected",
    [
        # simple, single moped cases
        (["S"], [], 1),
        (["F"], [], 5),
        (["M"], [], 8),
        # multiple mopeds, independent routes
        (["S", "F"], [2], 1 + 2 + 5),
        (["M", "F"], [10], 8 + 10 + 5),
        (["F", "F", "F"], [10, 1], 5 + 10 + 5 + 1 + 5),
        (["S", "F", "SF", "FF"], [2, 4, 3], 37),  # First example from case.md
    ],
)
def test_calculate_minutes(mopeds: list[str], distance: list[int], expected: int):
    res = calculate_minutes(mopeds, distance)
    assert res == expected
