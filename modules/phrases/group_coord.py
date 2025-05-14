# modules/phrases/group_coord.py
def try_group_coord(current, next1, next2, next3):
    # General rule: X + CONJ + X → X (recursive coordination)
    if next2 and current[0] == next2[0] and next1[0] == "CONJ":
        print(f"[Coordination] Forming {current[0]}: {current} {next1} {next2}")
        # Flatten left subtree if it’s already coordinated
        left = current[1] if current[0] == current[0] and isinstance(current[1], list) else [current]
        return {
            "node": (current[0], left + [next1, next2]),
            "consumed": 3
        }
    return None
