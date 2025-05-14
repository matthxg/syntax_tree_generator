# modules/latex_exporter.py
import subprocess
import os

def save_and_open_pdf(forest_str, filename="syntactic_tree"):
    latex_template = r"""
    \documentclass[border=10pt]{standalone}
    \usepackage[edges]{forest}
    \begin{document}
    %s
    \end{document}
    """ % forest_str

    output_dir = os.path.join(os.getcwd(), "generated_pdfs")
    os.makedirs(output_dir, exist_ok=True)

    tex_path = os.path.join(output_dir, f"{filename}.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(latex_template)

    try:
        subprocess.run(["pdflatex", tex_path], cwd=output_dir, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        pdf_path = os.path.join(output_dir, f"{filename}.pdf")
        if os.name == 'nt':
            os.startfile(pdf_path)
        elif os.name == 'posix':
            subprocess.run(["xdg-open", pdf_path])
        else:
            print("✅ PDF generated:", pdf_path)
    except FileNotFoundError:
        print("❌ 'pdflatex' not found. Please install a LaTeX distribution (e.g., TeX Live, MiKTeX).")
    except subprocess.CalledProcessError:
        print("❌ LaTeX compilation failed. Please check your LaTeX setup.")