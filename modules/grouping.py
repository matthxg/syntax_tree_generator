from copy import deepcopy
import json

def try_group_pp(tokens):
    i = 0
    while i < len(tokens) - 1:
        if tokens[i][0] == 'P' and tokens[i+1][0] == 'NP':
            tokens = tokens[:i] + [('PP', [tokens[i], tokens[i+1]])] + tokens[i+2:]
            i = 0
        else:
            i += 1
    return tokens

def try_group_nbar(tokens):
    i = 0
    while i < len(tokens) - 1:
        if tokens[i][0] == 'Adj' and tokens[i+1][0] == 'N':
            tokens = tokens[:i] + [("N'", [tokens[i], tokens[i+1]])] + tokens[i+2:]
            i = 0
        else:
            i += 1
    return tokens

def try_group_np(tokens):
    i = 0
    while i < len(tokens) - 1:
        if tokens[i][0] == 'D' and tokens[i+1][0] in ['N', "N'"]:
            tokens = tokens[:i] + [('NP', [tokens[i], tokens[i+1]])] + tokens[i+2:]
            i = 0
        elif tokens[i][0] == 'NP' and tokens[i+1][0] == 'PP':
            tokens = tokens[:i] + [('NP', [tokens[i], tokens[i+1]])] + tokens[i+2:]
            i = 0
        else:
            i += 1
    return tokens

def try_group_nbar_coord(tokens):
    i = 0
    while i < len(tokens) - 2:
        if tokens[i][0] == "N'" and tokens[i+1][0] == 'CONJ' and tokens[i+2][0] == "N'":
            tokens = tokens[:i] + [("N'", [tokens[i], tokens[i+1], tokens[i+2]])] + tokens[i+3:]
            i = 0
        else:
            i += 1
    return tokens

def try_group_vprime(tokens):
    i = 0
    while i < len(tokens) - 1:
        if tokens[i][0] == 'V' and tokens[i+1][0] == 'NP':
            base = tokens[:i] + [("V'", [tokens[i], tokens[i+1]])] + tokens[i+2:]
            variants = [base]
            if i + 2 < len(tokens) and tokens[i+2][0] == 'PP':
                alt = tokens[:i] + [("V'", [tokens[i], tokens[i+1], tokens[i+2]])] + tokens[i+3:]
                variants.append(alt)
            return variants
        i += 1
    return [tokens]

def try_group_vp(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i][0] == "V'":
            tokens = tokens[:i] + [('VP', [tokens[i]])] + tokens[i+1:]
            i = 0
        else:
            i += 1
    return tokens

def try_group_tp(tokens):
    i = 0
    while i < len(tokens) - 1:
        if tokens[i][0] == 'NP' and tokens[i+1][0] == 'VP':
            t_node = ('T', ['Ø'])
            t_bar = ("T'", [t_node, tokens[i+1]])
            tokens = tokens[:i] + [('TP', [tokens[i], t_bar])] + tokens[i+2:]
            i = 0
        else:
            i += 1
    return tokens

def try_general_coordination(tokens):
    while True:
        new_tokens = _coord_pass(tokens)
        if new_tokens == tokens:
            return tokens
        tokens = new_tokens

def _coord_pass(tokens):
    i = 0
    while i < len(tokens) - 2:
        if not isinstance(tokens[i], tuple):
            i += 1
            continue

        label = tokens[i][0]
        group = [tokens[i]]
        j = i + 1

        while j < len(tokens) - 1:
            punct_or_conj = tokens[j]
            next_tok = tokens[j + 1]

            if punct_or_conj[0] == 'PUNCT' and punct_or_conj[1] == [',']:
                if isinstance(next_tok, tuple) and next_tok[0] == label:
                    group.append(next_tok)
                    j += 2
                    continue
                elif j + 2 < len(tokens) and tokens[j + 1][0] == 'CONJ' and tokens[j + 2][0] == label:
                    group.append(tokens[j + 1])
                    group.append(tokens[j + 2])
                    j += 3
                    break
                else:
                    break
            elif punct_or_conj[0] == 'CONJ' and next_tok[0] == label:
                group.append(punct_or_conj)
                group.append(next_tok)
                j += 2
                break
            else:
                break

        if len(group) > 1:
            new_node = (label, group)
            tokens = tokens[:i] + [new_node] + tokens[j:]
            i = 0
        else:
            i += 1

    return tokens

def apply_grouping_rules(tokens):
    all_variants = [tokens]
    final_variants = []

    for variant in all_variants:
        prev = None
        while prev != variant:
            prev = deepcopy(variant)

            # Build basic constituents first
            variant = try_group_nbar(variant)
            variant = try_group_np(variant)
            variant = try_group_pp(variant)

            # Try coordination
            variant = try_group_np(variant)
            variant = try_general_coordination(variant)
            variant = try_group_nbar(variant)
            variant = try_group_np(variant)
            variant = try_general_coordination(variant)

        variant = try_general_coordination(variant)

        high_variant = variant
        low_variant = try_group_nbar_coord(deepcopy(variant))
        low_variant = try_group_np(low_variant)

        for path in [high_variant, low_variant]:
            vprime_variants = try_group_vprime(path)
            for vprime_variant in vprime_variants:
                vprime_variant = try_group_vp(vprime_variant)
                vprime_variant = try_group_tp(vprime_variant)
                final_variants.append(vprime_variant)

    unique = []
    seen = set()
    for tree in final_variants:
        key = json.dumps(tree, sort_keys=True)
        if key not in seen:
            seen.add(key)
            unique.append(tree)

    return unique
