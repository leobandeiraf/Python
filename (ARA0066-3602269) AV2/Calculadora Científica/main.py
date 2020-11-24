from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont


class Calculadora(Frame):
  bg_main = "#1f1f1f"
  bg_medium = "#131313"
  bg_strong = "#060606"
  bg_equal = "#254550"

  fg_main = "#ffffff"

  def __init__(self, master):
    super().__init__(master)

    self.font_main = tkFont.Font(family="Segoe UI", size="12")
    self.font_medium = tkFont.Font(family="Segoe UI", size="16")
    self.font_strong = tkFont.Font(family="Segoe UI", size="32")
    
    self.window = master
    self.window.title("Calculadora Científica")
    self.window.geometry("320x366")
    self.window.configure(background=self.bg_main)

    self.history_variable = IntVar()
    self.history = Label(self.window, text="Teste", textvariable=self.history_variable, bg=self.bg_main, fg=self.fg_main, height=1, font=self.font_main, anchor="e")
    self.history.place(width=310, height=32, x=5, y=5)

    self.screen = Entry(self.window, text="1", font=self.font_strong, bg=self.bg_main, fg=self.fg_main, justify="right", relief="flat")
    self.screen.place(width=310, height=52, x=5, y=38)

    self.sen = Button(self.window, text="sen", font=self.font_main, bg=self.bg_medium, fg=self.fg_main, justify="right", relief="flat")
    self.sen.place(width=76, height=52, x=5, y=91)

    self.cos = Button(self.window, text="cos", font=self.font_main, bg=self.bg_medium, fg=self.fg_main, justify="right", relief="flat")
    self.cos.place(width=76, height=52, x=83, y=91)

    self.tg = Button(self.window, text="tg", font=self.font_main, bg=self.bg_medium, fg=self.fg_main, justify="right", relief="flat")
    self.tg.place(width=76, height=52, x=161, y=91)

    self.clear = Button(self.window, text="C", font=self.font_main, bg=self.bg_medium, fg=self.fg_main, justify="right", relief="flat")
    self.clear.place(width=76, height=52, x=239, y=91)

    self.division = Button(self.window, text="÷", font=self.font_medium, bg=self.bg_medium, fg=self.fg_main, justify="right", relief="flat")
    self.division.place(width=76, height=52, x=239, y=145)

    self.seven = Button(self.window, text="7", font=self.font_medium, bg=self.bg_strong, fg=self.fg_main, justify="right", relief="flat")
    self.seven.place(width=76, height=52, x=5, y=145)

    self.eight = Button(self.window, text="8", font=self.font_medium, bg=self.bg_strong, fg=self.fg_main, justify="right", relief="flat")
    self.eight.place(width=76, height=52, x=83, y=145)

    self.nine = Button(self.window, text="9", font=self.font_medium, bg=self.bg_strong, fg=self.fg_main, justify="right", relief="flat")
    self.nine.place(width=76, height=52, x=161, y=145)

    self.multiplication = Button(self.window, text="x", font=self.font_medium, bg=self.bg_medium, fg=self.fg_main, justify="right", relief="flat")
    self.multiplication.place(width=76, height=52, x=239, y=199)

    self.four = Button(self.window, text="4", font=self.font_medium, bg=self.bg_strong, fg=self.fg_main, justify="right", relief="flat")
    self.four.place(width=76, height=52, x=5, y=199)

    self.five = Button(self.window, text="5", font=self.font_medium, bg=self.bg_strong, fg=self.fg_main, justify="right", relief="flat")
    self.five.place(width=76, height=52, x=83, y=199)

    self.six = Button(self.window, text="6", font=self.font_medium, bg=self.bg_strong, fg=self.fg_main, justify="right", relief="flat")
    self.six.place(width=76, height=52, x=161, y=199)

    self.minus = Button(self.window, text="-", font=self.font_medium, bg=self.bg_medium, fg=self.fg_main, justify="right", relief="flat")
    self.minus.place(width=76, height=52, x=239, y=253)

    self.one = Button(self.window, text="1", font=self.font_medium, bg=self.bg_strong, fg=self.fg_main, justify="right", relief="flat")
    self.one.place(width=76, height=52, x=5, y=253)

    self.two = Button(self.window, text="2", font=self.font_medium, bg=self.bg_strong, fg=self.fg_main, justify="right", relief="flat")
    self.two.place(width=76, height=52, x=83, y=253)

    self.three = Button(self.window, text="3", font=self.font_medium, bg=self.bg_strong, fg=self.fg_main, justify="right", relief="flat")
    self.three.place(width=76, height=52, x=161, y=253)

    self.plus = Button(self.window, text="+", font=self.font_medium, bg=self.bg_medium, fg=self.fg_main, justify="right", relief="flat")
    self.plus.place(width=76, height=52, x=239, y=307)

    self.equal = Button(self.window, text="=", font=self.font_medium, bg=self.bg_strong, fg=self.fg_main, justify="right", relief="flat")
    self.equal.place(width=76, height=52, x=5, y=307)

    self.zero = Button(self.window, text="0", font=self.font_medium, bg=self.bg_strong, fg=self.fg_main, justify="right", relief="flat")
    self.zero.place(width=76, height=52, x=83, y=307)

    self.dot = Button(self.window, text=",", font=self.font_medium, bg=self.bg_strong, fg=self.fg_main, justify="right", relief="flat")
    self.dot.place(width=76, height=52, x=161, y=307)


root = Tk()
app = Calculadora(root)
app.mainloop()