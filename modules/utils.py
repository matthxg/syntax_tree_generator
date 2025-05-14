# modules/utils.py
def esc(token):
    return token.replace("_", "\_")

def add_preamble(forest_code):
    return r"""\documentclass{article}
\usepackage[margin=1in]{geometry}
\usepackage{forest}
\begin{document}
""" + forest_code + "\n\\end{document}"
