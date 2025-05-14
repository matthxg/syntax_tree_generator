# modules/grouping.py
def try_group_chunks(forest):
    print("✅ Using grouping.py from canvas")

    i = 0
    changed = False
    new_forest = []

    while i < len(forest):
        current = forest[i]
        next1 = forest[i+1] if i + 1 < len(forest) else None
        next2 = forest[i+2] if i + 2 < len(forest) else None
        next3 = forest[i+3] if i + 3 < len(forest) else None

        # Handle punctuation
        if current[0] == "PUNCT":
            print(f"Marking punctuation: {current}")
            new_forest.append(("PUNCT", current[1]))
            i += 1
            changed = True
            continue

        # Coordinated NP
        if next2 and current[0] == "NP" and next1[0] == "CONJ" and next2[0] == "NP":
            print(f"Forming coordinated NP: {current} {next1} {next2}")
            new_forest.append(("NP", [current, next1, next2]))
            i += 3
            changed = True
            continue

        # Coordinated VP
        if next2 and current[0] == "VP" and next1[0] == "CONJ" and next2[0] == "VP":
            print(f"Forming coordinated VP: {current} {next1} {next2}")
            new_forest.append(("VP", [current, next1, next2]))
            i += 3
            changed = True
            continue

        # NP: D + N
        if next1:
            if current[0] == "D" and next1[0] == "N":
                print(f"Forming NP: {current} {next1}")
                new_forest.append(("NP", [current, next1]))
                i += 2
                changed = True
                continue

        # NP: D + Adj + N
        if next2:
            if current[0] == "D" and next1[0] == "Adj" and next2[0] == "N":
                print(f"Forming NP: {current} {next1} {next2}")
                new_forest.append(("NP", [current, next1, next2]))
                i += 3
                changed = True
                continue

        # PP: P + NP
        if next1:
            if current[0] == "P" and next1[0] == "NP":
                print(f"Forming PP: {current} {next1}")
                new_forest.append(("PP", [current, next1]))
                i += 2
                changed = True
                continue

        # VP: V + NP or V + PP (must come before VP intransitive)
        if next1 and current[0] == "V" and next1[0] in ("NP", "PP"):
            print(f"Forming VP: {current} {next1}")
            new_forest.append(("VP", [current, next1]))
            i += 2
            changed = True
            continue

        
        # TP: NP + VP
        if next1:
            if current[0] == "NP" and next1[0] == "VP":
                print(f"Forming TP with inserted T: {current} {next1}")
                t_node = ("T", ["Ø"])
                new_forest.append(("TP", [current, t_node, next1]))
                i += 2
                changed = True
                continue

        # VP: V alone (intransitive) – moved later to avoid greedy match
        if current[0] == "V":
            print(f"Forming VP (intransitive): {current}")
            new_forest.append(("VP", [current]))
            i += 1
            changed = True
            continue

        print(f"⚠️ No rule applied to token: {current}")
        new_forest.append(current)
        i += 1

    return new_forest, changed
