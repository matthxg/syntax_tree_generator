# modules/forest_builder.py
from modules.grouping import try_group_chunks
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

    round_count = 0
    while True:
        round_count += 1
        print(f"\n🔁 Grouping round {round_count}...")
        new_forest, changed = try_group_chunks(forest)

        if new_forest == forest:
            print("🔁 No structural change — breaking loop.")
            break

        debug(f"After round {round_count}: {new_forest}")
        forest = new_forest

    forest_str = "\\begin{forest}\nfor tree={grow'=south,parent anchor=south,child anchor=north,"
    forest_str += "l=1.3cm,s sep=6pt,anchor=center,calign=center,tier/.option=level}\n"

    for label, children in forest:
        forest_str += tree_to_latex(label, children) + "\n"

    if len(forest) > 1:
        print("⚠️ Final forest has multiple top-level nodes:")
        for node in forest:
            print(f"⚠️ Unmerged: {node}")

    forest_str += "\\end{forest}"

    # 🖨 Export LaTeX as PDF
    save_and_open_pdf(forest_str)

    return forest_str

def tree_to_latex(label, children):
    if isinstance(children, str):
        return f"[{label} [{esc(children)}]]"
    elif isinstance(children, list):
        subtrees = []
        for child in reversed(children):  # ⬅ reverse the order of children
            if isinstance(child, tuple) and len(child) == 2:
                subtrees.append(tree_to_latex(*child))
            elif isinstance(child, str):
                subtrees.append(f"[{esc(child)}]")
            else:
                raise ValueError(f"Unexpected child format: {child}")
        return f"[{label} {' '.join(subtrees)}]"
    else:
        raise ValueError(f"Invalid children type: {type(children)}")
