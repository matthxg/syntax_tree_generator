# modules/phrases/group_tp.py
def try_group_tp(current, next1, next2, next3):
    # T + VP → T'
    if next1 and current[0] == "T" and next1[0] == "VP":
        print(f"Forming T': {current} {next1}")
        return {
            "node": ("T'", [current, next1]),
            "consumed": 2
        }

    # NP + T' → TP
    if next1 and current[0] == "NP" and next1[0] == "T'":
        print(f"Forming TP: {current} {next1}")
        return {
            "node": ("TP", [current, next1]),
            "consumed": 2
        }

    # TP + CONJ + TP → TP
    if next2 and current[0] == "TP" and next1[0] == "CONJ" and next2[0] == "TP":
        print(f"Forming coordinated TP: {current} {next1} {next2}")
        return {
            "node": ("TP", [current, next1, next2]),
            "consumed": 3
        }

    # AdvP + T' → T'
    if next1 and current[0] == "AdvP" and next1[0] == "T'":
        print(f"Preposing AdvP to T': {current} {next1}")
        return {
            "node": ("T'", [current, next1]),
            "consumed": 2
        }

    # T' + AdvP → T'
    if next1 and current[0] == "T'" and next1[0] == "AdvP":
        print(f"Appending AdvP to T': {current} {next1}")
        return {
            "node": ("T'", [current, next1]),
            "consumed": 2
        }

    # TP + PP → TP
    if next1 and current[0] == "TP" and next1[0] == "PP":
        print(f"Extending TP with PP: {current} {next1}")
        return {
            "node": ("TP", [current, next1]),
            "consumed": 2
        }

    # TP + CP → TP
    if next1 and current[0] == "TP" and next1[0] == "CP":
        print(f"Extending TP with CP: {current} {next1}")
        return {
            "node": ("TP", [current, next1]),
            "consumed": 2
        }

    # CP + TP → TP
    if next1 and current[0] == "CP" and next1[0] == "TP":
        print(f"Fronting CP to TP: {current} {next1}")
        return {
            "node": ("TP", [current, next1]),
            "consumed": 2
        }

    # TP + AdvP → TP
    if next1 and current[0] == "TP" and next1[0] == "AdvP":
        print(f"Appending AdvP to TP: {current} {next1}")
        return {
            "node": ("TP", [current, next1]),
            "consumed": 2
        }

    # Fallback: NP + VP → TP (inserted T = Ø)
    if next1 and current[0] == "NP" and next1[0] == "VP":
        print(f"Forming TP with inserted T: {current} {next1}")
        inserted_t = ("T", ["Ø"])
        t_bar = ("T'", [inserted_t, next1])
        return {
            "node": ("TP", [current, t_bar]),
            "consumed": 2
        }

    return None
