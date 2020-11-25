import tkinter as tk
from typing import List, Callable

from templates import window


class Application:
    def __init__(self):
        self.root = window()

    def start(self) -> None:
        self.root.mainloop()