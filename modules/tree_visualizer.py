# modules/tree_visualizer.py
from nltk.tree import Tree
from modules.utils import esc

# Recursively convert forest node into an nltk.Tree

def forest_to_nltk_tree(label, children):
    if isinstance(children, str):
        return Tree(label, [esc(children)])
    elif isinstance(children, list):
        child_trees = []
        for child in children:
            if isinstance(child, tuple) and len(child) == 2:
                child_trees.append(forest_to_nltk_tree(child[0], child[1]))
            elif isinstance(child, str):
                child_trees.append(Tree("", [esc(child)]))
            else:
                raise ValueError(f"Unexpected child format: {child}")
        return Tree(label, child_trees)
    else:
        raise ValueError(f"Invalid children type: {type(children)}")

def draw_forest(forest):
    from nltk.draw.util import CanvasFrame
    from nltk.draw.tree import TreeWidget
    import tkinter as tk

    for label, children in forest:
        tree = forest_to_nltk_tree(label, children)
        cf = CanvasFrame()
        tc = TreeWidget(cf.canvas(), tree)
        cf.add_widget(tc, 10, 10)
        cf.canvas().update()
        cf.mainloop()