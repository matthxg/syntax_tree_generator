# modules/gui.py
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from modules.forest_builder import forest_bottom_up
from modules.utils import add_preamble

DEBUG = True

def debug(msg):
    if DEBUG:
        print(f"[DEBUG] {msg}")

def launch_gui():
    root = tk.Tk()
    root.title("X-Bar Tree Builder")
    root.geometry("800x600")

    input_label = ttk.Label(root, text="Enter sentence:")
    input_label.pack()

    input_entry = ttk.Entry(root, width=100)
    input_entry.pack(pady=5)

    output_label = ttk.Label(root, text="Output LaTeX:")
    output_label.pack()

    output_box = ScrolledText(root, height=25)
    output_box.pack(fill=tk.BOTH, expand=True)

    def generate_tree():
        sentence = input_entry.get().strip()
        debug(f"Input sentence: {sentence}")

        forest_code = forest_bottom_up(sentence)
        latex_code = add_preamble(forest_code)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, latex_code)

    generate_button = ttk.Button(root, text="Generate Tree", command=generate_tree)
    generate_button.pack(pady=10)

    root.mainloop()
