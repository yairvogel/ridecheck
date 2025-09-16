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

    loc_s = 0
    loc_f = 0
    loc_m = 0

    total = 0
    for idx, moped in enumerate(mopeds):
        # if employee needs to go to current moped
        # they need to travel to that moped
        if "S" in moped:
            total += sum(distance[loc_s:idx])
            loc_s = idx
        if "F" in moped:
            total += sum(distance[loc_f:idx])
            loc_f = idx
        if "M" in moped:
            total += sum(distance[loc_m:idx])
            loc_m = idx

        total += sum(map(_fix_time, moped))

    return total


if __name__ == "__main__":
    m = ["S"]
    d: list[int] = []
    res = calculate_minutes(["S"], [])
    print(f"mopeds=[{','.join(m)}]; distance=[{','.join(map(str, d))}]; result={res}")
