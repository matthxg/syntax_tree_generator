# modules/forest_builder.py
from modules.grouping import apply_grouping_rules
from modules.utils import esc
from modules.labeling import label_sentence
from modules.latex_exporter import save_and_open_pdf

DEBUG = True

def debug(msg):
    if DEBUG:
        print(f"[DEBUG] {msg}")

def forest_bottom_up(sentence):
    print("✅ forest_bottom_up() called")

    labeled = label_sentence(sentence)
    forest = [(label, [token]) for label, token in labeled]
    debug(f"Initial forest: {forest}")

    # Apply all possible grouping interpretations
    forest_variants = apply_grouping_rules(forest)

    forest_strings = []
    for i, tree in enumerate(forest_variants):
        print(f"\n--- Tree variant {i + 1} ---")

        forest_str = "\n\\begin{forest}\nfor tree={grow'=south,parent anchor=south,child anchor=north,"
        forest_str += "l=1.3cm,s sep=6pt,anchor=center,calign=center,tier/.option=level}\n"

        for label, children in tree:
            forest_str += tree_to_latex(label, children) + "\n"

        forest_str += "\\end{forest}"
        forest_strings.append(forest_str)

        if len(tree) > 1:
            print("⚠️ Final forest has multiple top-level nodes:")
            for node in tree:
                print(f"⚠️ Unmerged: {node}")

    # 🖨 Export combined LaTeX as one PDF with all interpretations
    full_latex = "\n\n".join(forest_strings)
    save_and_open_pdf(full_latex)

    return forest_variants

def tree_to_latex(label, children):
    if isinstance(children, str):
        return f"[{label} [{esc(children)}]]"
    elif isinstance(children, list):
        subtrees = []
        for child in reversed(children):
            if isinstance(child, tuple) and len(child) == 2:
                subtrees.append(tree_to_latex(*child))
            elif isinstance(child, str):
                escaped = "$\\emptyset$" if label == "T" and child == "Ø" else esc(child)
                subtrees.append(f"[{escaped}]")
            else:
                raise ValueError(f"Unexpected child format: {child}")
        return f"[{label} {' '.join(subtrees)}]"
    else:
        raise ValueError(f"Invalid children type: {type(children)}")