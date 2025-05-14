# modules/phrases/group_np.py
def try_group_np(current, next1, next2, next3):
    # Adj + N → N'
    if next1 and current[0] == "Adj" and next1[0] == "N":
        print(f"Forming N': {current} {next1}")
        return {"node": ("N'", [current, next1]), "consumed": 2}

    # D + N' → NP
    if next1 and current[0] == "D" and next1[0] == "N'":
        print(f"Forming NP: {current} {next1}")
        return {"node": ("NP", [current, next1]), "consumed": 2}

    # D + N → NP (simple fallback)
    if next1 and current[0] == "D" and next1[0] == "N":
        print(f"Forming NP: {current} {next1}")
        return {"node": ("NP", [current, next1]), "consumed": 2}

    # D + Adj + N → NP (expanded fallback)
    if next2 and current[0] == "D" and next1[0] == "Adj" and next2[0] == "N":
        print(f"Forming NP: {current} {next1} {next2}")
        return {"node": ("NP", [current, next1, next2]), "consumed": 3}

    # NP + CONJ + NP → NP (recursive coordination)
    if next2 and current[0] == "NP" and next1[0] == "CONJ" and next2[0] == "NP":
        print(f"Forming coordinated NP: {current} {next1} {next2}")
        return {"node": ("NP", [("NP", current[1]), next1, next2]), "consumed": 3}

    # Recursive Adj + N' → N'
    if next1 and current[0] == "Adj" and next1[0] == "N'":
        print(f"Forming N': {current} {next1}")
        return {"node": ("N'", [current, next1]), "consumed": 2}

    # N' + PP → N'
    if next1 and current[0] == "N'" and next1[0] == "PP":
        print(f"Forming N' with PP: {current} {next1}")
        return {"node": ("N'", [current, next1]), "consumed": 2}

    # N' + CONJ + N' → N'
    if next2 and current[0] == "N'" and next1[0] == "CONJ" and next2[0] == "N'":
        print(f"Forming coordinated N': {current} {next1} {next2}")
        return {"node": ("N'", [current, next1, next2]), "consumed": 3}

    # N' + N' → N'
    if next1 and current[0] == "N'" and next1[0] == "N'":
        print(f"Merging N' + N': {current} {next1}")
        return {"node": ("N'", [current, next1]), "consumed": 2}

    # N' + NP → N'
    if next1 and current[0] == "N'" and next1[0] == "NP":
        print(f"Attaching NP to N': {current} {next1}")
        return {"node": ("N'", [current, next1]), "consumed": 2}

    # NP + NP → NP
    if next1 and current[0] == "NP" and next1[0] == "NP":
        print(f"Merging NP + NP: {current} {next1}")
        return {"node": ("NP", [current, next1]), "consumed": 2}

    # NP + PP → NP (postmodification)
    if next1 and current[0] == "NP" and next1[0] == "PP":
        print(f"Postmodifying NP with PP: {current} {next1}")
        return {"node": ("NP", [current, next1]), "consumed": 2}

    # NP + CP → NP
    if next1 and current[0] == "NP" and next1[0] == "CP":
        print(f"Postmodifying NP with CP: {current} {next1}")
        return {"node": ("NP", [current, next1]), "consumed": 2}

    # N → N'
    if current[0] == "N":
        print(f"Promoting N to N': {current}")
        return {"node": ("N'", [current]), "consumed": 1}

    # N' → NP (bare NP)
    if current[0] == "N'":
        print(f"Promoting N' to NP: {current}")
        return {"node": ("NP", [current]), "consumed": 1}

    return None
