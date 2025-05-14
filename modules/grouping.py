# modules/grouping.py
from modules.phrases.group_np import try_group_np
from modules.phrases.group_vp import try_group_vp
from modules.phrases.group_pp import try_group_pp
from modules.phrases.group_tp import try_group_tp
from modules.phrases.group_cp import try_group_cp
from modules.phrases.group_adjp import try_group_adjp
from modules.phrases.group_advp import try_group_advp

def try_group_chunks(forest):
    round_num = 1
    while True:
        print(f"🔁 Grouping round {round_num}...")
        forest, changed = _apply_grouping_pass(forest)
        if not changed:
            break
        round_num += 1
    return forest, changed

from modules.phrases.group_coord import try_group_coord

def _apply_grouping_pass(forest):
    print("✅ Using grouping.py from canvas")

    i = 0
    changed = False
    new_forest = []

    while i < len(forest):
        current = forest[i]
        next1 = forest[i+1] if i + 1 < len(forest) else None
        next2 = forest[i+2] if i + 2 < len(forest) else None
        next3 = forest[i+3] if i + 3 < len(forest) else None

        # Handle punctuation (do not mark as changed)
        if current[0] == "PUNCT":
            print(f"Marking punctuation: {current}")
            new_forest.append(("PUNCT", current[1]))
            i += 1
            continue

        # Try coordination first
        coord_result = try_group_coord(current, next1, next2, next3)
        if coord_result:
            new_forest.append(coord_result["node"])
            i += coord_result["consumed"]
            changed = True
            continue

        # Try each phrase type
        for grouper in [
            try_group_np, try_group_vp, try_group_pp,
            try_group_tp, try_group_cp,
            try_group_adjp, try_group_advp
        ]:
            result = grouper(current, next1, next2, next3)
            if result:
                new_forest.append(result["node"])
                i += result["consumed"]
                changed = True
                break
        else:
            # Defer fallback: V → VP (intransitive) ONLY if no signs of NP/PP/CP grouping
            if current[0] == "V" and not (
                (next1 and next1[0] == "D" and next2 and next2[0] == "N") or
                (next1 and next1[0] in ["NP", "PP", "CP"])
            ):
                print(f"Deferred fallback: Forming VP (intransitive): {current}")
                new_forest.append(("VP", [current]))
                i += 1
                changed = True
            else:
                print(f"⚠️ No rule applied to token: {current}")
                new_forest.append(current)
                i += 1

    return new_forest, changed
