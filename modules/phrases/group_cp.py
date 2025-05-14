# modules/phrases/group_cp.py
def try_group_cp(current, next1, next2, next3):
    # C + TP → CP
    if next1 and current[0] == "C" and next1[0] == "TP":
        print(f"Forming CP: {current} {next1}")
        return {
            "node": ("CP", [current, next1]),
            "consumed": 2
        }

    # CP + AdvP → CP
    if next1 and current[0] == "CP" and next1[0] == "AdvP":
        print(f"Appending AdvP to CP: {current} {next1}")
        return {
            "node": ("CP", [current, next1]),
            "consumed": 2
        }

    # AdvP + CP → CP
    if next1 and current[0] == "AdvP" and next1[0] == "CP":
        print(f"Preposing AdvP to CP: {current} {next1}")
        return {
            "node": ("CP", [current, next1]),
            "consumed": 2
        }

    # CP + CONJ + CP → CP
    if next2 and current[0] == "CP" and next1[0] == "CONJ" and next2[0] == "CP":
        print(f"Forming coordinated CP: {current} {next1} {next2}")
        return {
            "node": ("CP", [current, next1, next2]),
            "consumed": 3
        }

        # C + TP → C'
    if next1 and current[0] == "C" and next1[0] == "TP":
        print(f"Forming C': {current} {next1}")
        return {
            "node": ("C'", [current, next1]),
            "consumed": 2
        }

    # C' → CP
    if current[0] == "C'":
        print(f"Promoting C' to CP: {current}")
        return {
            "node": ("CP", [current]),
            "consumed": 1
        }

    # C' + AdvP → C'
    if next1 and current[0] == "C'" and next1[0] == "AdvP":
        print(f"Appending AdvP to C': {current} {next1}")
        return {
            "node": ("C'", [current, next1]),
            "consumed": 2
        }

    # AdvP + C' → C'
    if next1 and current[0] == "AdvP" and next1[0] == "C'":
        print(f"Preposing AdvP to C': {current} {next1}")
        return {
            "node": ("C'", [current, next1]),
            "consumed": 2
        }

    # CP + PP → CP
    if next1 and current[0] == "CP" and next1[0] == "PP":
        print(f"Extending CP with PP: {current} {next1}")
        return {
            "node": ("CP", [current, next1]),
            "consumed": 2
        }

    # CP + CP → CP
    if next1 and current[0] == "CP" and next1[0] == "CP":
        print(f"Combining CP with CP: {current} {next1}")
        return {
            "node": ("CP", [current, next1]),
            "consumed": 2
        }

    return None
