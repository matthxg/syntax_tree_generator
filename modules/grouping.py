def try_group_np(tokens):
    i = 0
    while i < len(tokens) - 1:
        if tokens[i][0] == 'D' and tokens[i+1][0] == 'N':
            tokens = tokens[:i] + [('NP', [tokens[i], tokens[i+1]])] + tokens[i+2:]
            i = 0
        else:
            i += 1
    return tokens

def try_group_vprime(tokens):
    i = 0
    while i < len(tokens) - 1:
        if tokens[i][0] == 'V' and tokens[i+1][0] == 'NP':
            tokens = tokens[:i] + [("V'", [tokens[i], tokens[i+1]])] + tokens[i+2:]
            i = 0
        else:
            i += 1
    return tokens

def try_group_vp(tokens):
    i = 0
    while i < len(tokens) - 1:
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
    """
    Detects and merges repeated phrases of the same label with coordination tokens.
    Supports flat (n-ary) coordination across all categories: NP, VP, etc.
    Also handles comma-, semicolon-, and colon-separated coordination (Oxford comma supported).
    """
    i = 0
    while i < len(tokens) - 2:
        coord_group = []
        label = None
        j = i

        while j < len(tokens) - 2:
            first, sep, second = tokens[j], tokens[j+1], tokens[j+2]

            if not (isinstance(first, tuple) and isinstance(second, tuple)):
                break

            if first[0] != second[0]:
                break

            if sep[0] == 'PUNCT' and sep[1] in [[','], [';'], [':']]:
                # Accept separator, continue
                if label is None:
                    label = first[0]
                if not coord_group:
                    coord_group.extend([first, sep, second])
                else:
                    coord_group.extend([sep, second])
                j += 2
            elif sep[0] == 'PUNCT' and sep[1] == [','] and j + 3 < len(tokens):
                # Check for Oxford comma: X , CONJ X
                next_conj, next_token = tokens[j+2], tokens[j+3]
                if next_conj[0] == 'CONJ' and next_token[0] == first[0]:
                    if label is None:
                        label = first[0]
                    if not coord_group:
                        coord_group.extend([first, sep, next_conj, next_token])
                    else:
                        coord_group.extend([sep, next_conj, next_token])
                    j += 3
                    break
                else:
                    break
            elif sep[0] == 'CONJ':
                # Regular conjunction (no Oxford comma)
                if label is None:
                    label = first[0]
                if not coord_group:
                    coord_group.extend([first, sep, second])
                else:
                    coord_group.extend([sep, second])
                j += 2
                break
            else:
                break

        if coord_group:
            new_node = (label, coord_group)
            tokens = tokens[:i] + [new_node] + tokens[j+1:]
            i = 0
        else:
            i += 1

    return tokens

def apply_grouping_rules(tokens):
    tokens = try_general_coordination(tokens)
    tokens = try_group_np(tokens)
    tokens = try_group_vprime(tokens)
    tokens = try_group_vp(tokens)
    tokens = try_group_tp(tokens)
    return 
