from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont


class Calculadora(Frame):
  bg_main = "#1f1f1f"
  bg_medium = "#131313"
  bg_strong = "#060606"
  fg_main = "#fff"

  def __init__(self, master):
    super().__init__(master)
    
    self.window = master
    self.window.title("Calculadora Científica")
    self.window.geometry("320x500")
    self.window.configure(background=self.bg_main)

root = Tk()
app = Calculadora(root)
app.mainloop()