def _fix_time(s: str):
    match s:
        case "S":
            return 1
        case "F":
            return 5
        case "M":
            return 8
        case _:
            raise ValueError(f"{s} is not a valid action")


def calculate_minutes(mopeds: list[str], distance: list[int]) -> int:
    assert len(mopeds) == len(distance) + 1, (
        "distance between mopeds must match number of mopeds"
    )

    # assuming single moped
    assert len(mopeds) == 1
    return sum(map(_fix_time, mopeds[0]))


if __name__ == "__main__":
    m = ["S"]
    d: list[int] = []
    res = calculate_minutes(["S"], [])
    print(f"mopeds=[{','.join(m)}]; distance=[{','.join(map(str, d))}]; result={res}")
