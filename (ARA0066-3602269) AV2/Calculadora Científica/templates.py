import tkinter as tk
from typing import List


def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculator')
    root.config(padx=5, pady=5, background='#1f1f1f')
    root.resizable(False, False)
    return root


def make_label(root, **grid_options) -> tk.Label:
    label = tk.Label(root, text='Sem histórico', anchor='e', justify='right', bg='#1f1f1f', fg="#fff")
    label.grid(**grid_options)
    return label


def make_display(root, **grid_options) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(**grid_options)
    display.config(font=('Helvetica', 40, 'bold'), justify='right', bd=1, bg="#1f1f1f", fg="#fff", relief='flat')
    display.bind('<Control-a>', _display_control_a)
    return display


def _display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'


def make_button(root, text, **grid_options) -> tk.Button:
    button = tk.Button(root, text=text)
    button.grid(**grid_options)
    button.config(font=('Helvetica', 21, 'normal'), pady=30, width=1, bg='#131313', fg="#fff", bd=0, cursor='hand2', highlightthickness=0, highlightcolor='#ccc', activebackground='#ccc', highlightbackground='#ccc')
    return button


def make_buttons(root, starting_row) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ['sen', 'cos', 'tg', 'C'],
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['=', '0', '.', '+'],
    ]

    buttons: List[List[tk.Button]] = []

    for row, row_value in enumerate(button_texts, start=starting_row):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = make_button(
                root, text=col_value,
                row=row, column=col_index, sticky='news', padx=2, pady=2
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons