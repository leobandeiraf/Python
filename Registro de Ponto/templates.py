import tkinter as tk
from typing import List


def window() -> tk.Tk:
    root = tk.Tk()
    root.title('P4Pro - Registro de Ponto')
    root.config(padx=5, pady=5, background='#1f1f1f')
    root.resizable(False, False)

    return root