# modules/phrases/group_pp.py
def try_group_pp(current, next1, next2, next3):
    # P + NP → PP
    if next1 and current[0] == "P" and next1[0] == "NP":
        print(f"Forming PP: {current} {next1}")
        return {
            "node": ("PP", [current, next1]),
            "consumed": 2
        }

    # PP + PP → PP (stacked modifiers like "in front of")
    if next1 and current[0] == "PP" and next1[0] == "PP":
        print(f"Merging PP: {current} {next1}")
        return {
            "node": ("PP", [current, next1]),
            "consumed": 2
        }

    # PP + CONJ + PP → PP
    if next2 and current[0] == "PP" and next1[0] == "CONJ" and next2[0] == "PP":
        print(f"Forming coordinated PP: {current} {next1} {next2}")
        return {
            "node": ("PP", [current, next1, next2]),
            "consumed": 3
        }

        # P + NP → P'
    if next1 and current[0] == "P" and next1[0] == "NP":
        print(f"Forming P': {current} {next1}")
        return {
            "node": ("P'", [current, next1]),
            "consumed": 2
        }

    # P' → PP
    if current[0] == "P'":
        print(f"Forming PP from P': {current}")
        return {
            "node": ("PP", [current]),
            "consumed": 1
        }

    # P' + CP → P'
    if next1 and current[0] == "P'" and next1[0] == "CP":
        print(f"Extending P' with CP: {current} {next1}")
        return {
            "node": ("P'", [current, next1]),
            "consumed": 2
        }

    # PP + AdvP → PP
    if next1 and current[0] == "PP" and next1[0] == "AdvP":
        print(f"Extending PP with AdvP: {current} {next1}")
        return {
            "node": ("PP", [current, next1]),
            "consumed": 2
        }

    return None
