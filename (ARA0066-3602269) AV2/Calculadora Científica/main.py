from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont


class Calculadora(Frame):
  bg_main = "#1f1f1f"
  bg_medium = "#131313"
  bg_strong = "#060606"
  bg_equal = "#254550"
  bg_C = "#990000"

  fg_main = "#ffffff"

  def __init__(self, master):
    super().__init__(master)

    self.font_main = tkFont.Font(family="Segoe UI", size="10")
    self.font_medium = tkFont.Font(family="Segoe UI", size="21")
    self.font_strong = tkFont.Font(family="Segoe UI", size="32")
    
    self.window = master
    self.window.title("Calculadora Científica")
    self.window.geometry("320x500")
    self.window.configure(background=self.bg_main)

    self.history_variable = IntVar()
    self.history = Label(self.window, text="Teste", textvariable=self.history_variable, height=1, bg=self.bg_main, fg=self.fg_main, font=self.font_main, anchor="e")
    self.history.pack(padx=5, pady=5, ipadx=5, fill= X, side=TOP)

    self.screen = Entry(self.window, text="0", bg=self.bg_main, fg=self.fg_main, font=self.font_strong, justify="right", relief="flat")
    self.screen.pack(padx=5, ipadx=5, fill= X, side=TOP)

    self.percentage = Button(self.window, text="%", bg=self.bg_medium, fg=self.fg_main, font=self.font_medium, width=2, height=1, relief="flat")
    self.percentage.pack(padx=1, ipadx=2, side=LEFT)

    self.plus = Button(self.window, text="+", bg=self.bg_medium, fg=self.fg_main, font=self.font_medium, width=2, height=1, relief="flat")
    self.plus.pack(padx=1, ipadx=2, side=LEFT)

    self.minus = Button(self.window, text="-", bg=self.bg_medium, fg=self.fg_main, font=self.font_medium, width=2, height=1, relief="flat")
    self.minus.pack(padx=1, ipadx=2, side=LEFT)

    self.multiplication = Button(self.window, text="x", bg=self.bg_medium, fg=self.fg_main, font=self.font_medium, width=2, height=1, relief="flat")
    self.multiplication.pack(padx=1, ipadx=2, side=LEFT)

    self.division = Button(self.window, text="÷", bg=self.bg_medium, fg=self.fg_main, font=self.font_medium, width=2, height=1, relief="flat")
    self.division.pack(padx=1, ipadx=2, side=LEFT)
    



root = Tk()
app = Calculadora(root)
app.mainloop()