# modules/phrases/group_vp.py
def try_group_vp(current, next1, next2, next3):
    # PRIORITY: Attempt all multi-token VP groupings before fallback

    # V + NP + NP → V'
    if next2 and current[0] == "V" and next1[0] == "NP" and next2[0] == "NP":
        print(f"Forming V' with double NP: {current} {next1} {next2}")
        return {"node": ("V'", [current, next1, next2]), "consumed": 3}

    # V + NP + PP → V'
    if next2 and current[0] == "V" and next1[0] == "NP" and next2[0] == "PP":
        print(f"Forming V' with NP and PP: {current} {next1} {next2}")
        return {"node": ("V'", [current, next1, next2]), "consumed": 3}

    # V + NP + CP → V'
    if next2 and current[0] == "V" and next1[0] == "NP" and next2[0] == "CP":
        print(f"Forming V' with NP and CP: {current} {next1} {next2}")
        return {"node": ("V'", [current, next1, next2]), "consumed": 3}

    # V + NP → V'
    if next1 and current[0] == "V" and next1[0] == "NP":
        print(f"Forming V': {current} {next1}")
        return {"node": ("V'", [current, next1]), "consumed": 2}

    # V + PP → V'
    if next1 and current[0] == "V" and next1[0] == "PP":
        print(f"Forming V': {current} {next1}")
        return {"node": ("V'", [current, next1]), "consumed": 2}

    # V + CP → V'
    if next1 and current[0] == "V" and next1[0] == "CP":
        print(f"Forming V' with CP: {current} {next1}")
        return {"node": ("V'", [current, next1]), "consumed": 2}

    # V' + NP → V'
    if next1 and current[0] == "V'" and next1[0] == "NP":
        print(f"Extending V' with NP: {current} {next1}")
        return {"node": ("V'", [*current[1], next1]), "consumed": 2}

    # V' + PP → V'
    if next1 and current[0] == "V'" and next1[0] == "PP":
        print(f"Extending V' with PP: {current} {next1}")
        return {"node": ("V'", [*current[1], next1]), "consumed": 2}

    # V' + CP → V'
    if next1 and current[0] == "V'" and next1[0] == "CP":
        print(f"Extending V' with CP: {current} {next1}")
        return {"node": ("V'", [*current[1], next1]), "consumed": 2}

    # V' → VP
    if current[0] == "V'":
        print(f"Forming VP: {current}")
        return {"node": ("VP", [current]), "consumed": 1}

    # VP + PP → VP
    if next1 and current[0] == "VP" and next1[0] == "PP":
        print(f"Extending VP with PP: {current} {next1}")
        return {"node": ("VP", [*current[1], next1]), "consumed": 2}

    # VP + AdvP → VP
    if next1 and current[0] == "VP" and next1[0] == "AdvP":
        print(f"Extending VP with AdvP: {current} {next1}")
        return {"node": ("VP", [*current[1], next1]), "consumed": 2}

    # VP + CONJ + VP → VP
    if next2 and current[0] == "VP" and next1[0] == "CONJ" and next2[0] == "VP":
        print(f"Forming coordinated VP: {current} {next1} {next2}")
        return {"node": ("VP", [current, next1, next2]), "consumed": 3}

    # VP + NP → VP (recovering object after intransitive fallback)
    if next1 and current[0] == "VP" and next1[0] == "NP":
        print(f"Appending NP to VP: {current} {next1}")
        return {"node": ("VP", [*current[1], next1]), "consumed": 2}

    return None
