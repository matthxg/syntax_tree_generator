# modules/phrases/group_advp.py
def try_group_advp(current, next1, next2, next3):
    # Adv + Adv → AdvP
    if next1 and current[0] == "Adv" and next1[0] == "Adv":
        print(f"Forming AdvP from Advs: {current} {next1}")
        return {"node": ("AdvP", [current, next1]), "consumed": 2}

    # Adv → AdvP
    if current[0] == "Adv":
        print(f"Promoting Adv to AdvP: {current}")
        return {"node": ("AdvP", [current]), "consumed": 1}

    # AdvP + CONJ + AdvP → AdvP (recursive coordination)
    if next2 and current[0] == "AdvP" and next1[0] == "CONJ" and next2[0] == "AdvP":
        print(f"Forming coordinated AdvP: {current} {next1} {next2}")
        return {"node": ("AdvP", [current, next1, next2]), "consumed": 3}

    # AdvP + PP → AdvP
    if next1 and current[0] == "AdvP" and next1[0] == "PP":
        print(f"Extending AdvP with PP: {current} {next1}")
        return {"node": ("AdvP", [current, next1]), "consumed": 2}

    # AdvP + CP → AdvP
    if next1 and current[0] == "AdvP" and next1[0] == "CP":
        print(f"Extending AdvP with CP: {current} {next1}")
        return {"node": ("AdvP", [current, next1]), "consumed": 2}

    # AdvP + AdvP → AdvP
    if next1 and current[0] == "AdvP" and next1[0] == "AdvP":
        print(f"Merging AdvP with AdvP: {current} {next1}")
        return {"node": ("AdvP", [current, next1]), "consumed": 2}

    # PP + AdvP → AdvP
    if next1 and current[0] == "PP" and next1[0] == "AdvP":
        print(f"Preposing PP to AdvP: {current} {next1}")
        return {"node": ("AdvP", [current, next1]), "consumed": 2}

    # CP + AdvP → AdvP
    if next1 and current[0] == "CP" and next1[0] == "AdvP":
        print(f"Preposing CP to AdvP: {current} {next1}")
        return {"node": ("AdvP", [current, next1]), "consumed": 2}

    return None
