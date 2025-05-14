def try_group_coord(current, next1, next2, next3):
    # Base case: X + CONJ + X => X
    if next2 and current[0] == next2[0] and next1[0] == "CONJ":
        print(f"Forming coordinated {current[0]}: {current} {next1} {next2}")
        return {
            "node": (current[0], [current, next1, next2]),
            "consumed": 3
        }

    # Recursive case: X + CONJ + X + CONJ + X ...
    if next3 and current[0] == next2[0] == next3[0] and next1[0] == "CONJ":
        print(f"Forming recursively coordinated {current[0]}: {current} {next1} {next2} {next3}")
        return {
            "node": (current[0], [current, next1, next2, next3]),
            "consumed": 4
        }

    return None
