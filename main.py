FIX_TIMES = {"S": 1, "F": 5, "M": 8}


def calculate_minutes(mopeds: list[str], distance: list[int]) -> int:
    assert len(mopeds) == len(distance) + 1, (
        "distance between mopeds must match number of mopeds"
    )

    loc_s, loc_f, loc_m = 0, 0, 0

    # prefix-sum of the distances.
    # Computed such that dist_sum[i] - dist_sum[j] == sum(distance[j:i])
    dist_sum: list[int] = []
    t = 0
    for d in distance:
        dist_sum.append(t)
        t += d
    dist_sum.append(t)

    total = 0
    for idx, moped in enumerate(mopeds):
        # if employee needs to go to current moped
        # they need to travel to that moped
        if "S" in moped:
            total += dist_sum[idx] - dist_sum[loc_s]
            loc_s = idx
        if "F" in moped:
            total += dist_sum[idx] - dist_sum[loc_f]
            loc_f = idx
        if "M" in moped:
            total += dist_sum[idx] - dist_sum[loc_m]
            loc_m = idx

        total += sum(FIX_TIMES[c] for c in moped)

    return total


if __name__ == "__main__":
    m = ["S"]
    d: list[int] = []
    res = calculate_minutes(["S"], [])
    print(f"mopeds=[{','.join(m)}]; distance=[{','.join(map(str, d))}]; result={res}")
