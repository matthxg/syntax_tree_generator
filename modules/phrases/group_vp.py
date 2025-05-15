def try_group_vp(current, next1, next2, next3):
    # V + NP → V'
    if next1 and current[0] == "V" and next1[0] == "NP":
        print(f"Forming V': {current} {next1}")
        return {
            "node": ("V'", [current, next1]),
            "consumed": 2
        }

    # V' + NP → V'
    if next1 and current[0] == "V'" and next1[0] == "NP":
        print(f"Extending V' with NP: {current} {next1}")
        return {
            "node": ("V'", [*current[1], next1]),
            "consumed": 2
        }

    # V' → VP
    if current[0] == "V'":
        print(f"Forming VP: {current}")
        return {
            "node": ("VP", [current]),
            "consumed": 1
        }

    # VP + CONJ + NP → VP
    if next2 and current[0] == "VP" and next1[0] == "CONJ" and next2[0] == "NP":
        print(f"Extending VP with coordination: {current} {next1} {next2}")
        return {
            "node": ("VP", [*current[1], next1, next2]),
            "consumed": 3
        }

    return None
