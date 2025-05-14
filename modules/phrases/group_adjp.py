# modules/phrases/group_adjp.py
def try_group_adjp(current, next1, next2, next3):
    # AdvP + Adj → AdjP
    if next1 and current[0] == "AdvP" and next1[0] == "Adj":
        print(f"Forming AdjP: {current} {next1}")
        return {
            "node": ("AdjP", [current, next1]),
            "consumed": 2
        }

    # Adj + PP → AdjP
    if next1 and current[0] == "Adj" and next1[0] == "PP":
        print(f"Forming AdjP with PP: {current} {next1}")
        return {
            "node": ("AdjP", [current, next1]),
            "consumed": 2
        }

    # Adj + CP → AdjP
    if next1 and current[0] == "Adj" and next1[0] == "CP":
        print(f"Forming AdjP with CP: {current} {next1}")
        return {
            "node": ("AdjP", [current, next1]),
            "consumed": 2
        }

    # AdjP + CONJ + AdjP → AdjP
    if next2 and current[0] == "AdjP" and next1[0] == "CONJ" and next2[0] == "AdjP":
        print(f"Forming coordinated AdjP: {current} {next1} {next2}")
        return {
            "node": ("AdjP", [current, next1, next2]),
            "consumed": 3
        }

        # Adj → Adj'
    if current[0] == "Adj":
        print(f"Promoting Adj to Adj': {current}")
        return {
            "node": ("Adj'", [current]),
            "consumed": 1
        }

    # Adj' → AdjP
    if current[0] == "Adj'":
        print(f"Promoting Adj' to AdjP: {current}")
        return {
            "node": ("AdjP", [current]),
            "consumed": 1
        }

    # AdvP + Adj' → Adj'
    if next1 and current[0] == "AdvP" and next1[0] == "Adj'":
        print(f"Forming recursive Adj': {current} {next1}")
        return {
            "node": ("Adj'", [current, next1]),
            "consumed": 2
        }

    # Adj' + PP → Adj'
    if next1 and current[0] == "Adj'" and next1[0] == "PP":
        print(f"Extending Adj' with PP: {current} {next1}")
        return {
            "node": ("Adj'", [current, next1]),
            "consumed": 2
        }

    # Adj' + CP → Adj'
    if next1 and current[0] == "Adj'" and next1[0] == "CP":
        print(f"Extending Adj' with CP: {current} {next1}")
        return {
            "node": ("Adj'", [current, next1]),
            "consumed": 2
        }

    # Adj' + CONJ + Adj' → Adj'
    if next2 and current[0] == "Adj'" and next1[0] == "CONJ" and next2[0] == "Adj'":
        print(f"Forming coordinated Adj': {current} {next1} {next2}")
        return {
            "node": ("Adj'", [current, next1, next2]),
            "consumed": 3
        }

    return None
