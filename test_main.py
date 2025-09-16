import pytest

from main import calculate_minutes


@pytest.mark.parametrize(
    "mopeds,distance,expected",
    [
        # simple, single moped cases
        (["S"], [], 1),
        (["F"], [], 5),
        (["M"], [], 8),
    ],
)
def test_calculate_minutes(mopeds: list[str], distance: list[int], expected: int):
    res = calculate_minutes(mopeds, distance)
    assert res == expected
