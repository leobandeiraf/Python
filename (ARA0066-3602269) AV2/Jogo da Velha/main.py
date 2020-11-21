from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont


class App(Frame):
  def __init__(self, master):
    super().__init__(master)
    
    self.bg_main = "#535251"
    self.bg_medium = "#313130"
    self.bg_strong = "#111110"
    self.fg_main = "#fff"

    self.master = master
    self.master.title("Jogo da Velha")
    self.master.geometry("300x300")
    self.master.configure(background=self.bg_main)
    
    self.window = Frame(self.master, bg=self.bg_medium, width=280, height=280)
    self.window.place(relx=0.025, rely=0.025)

    self.font = tkFont.Font(family="Segoe UI", size="10")
    self.font_strong = tkFont.Font(family="Segoe UI", size="14", weight="bold")

    self.start()


  def start(self):
    self.plays = 0
    
    self.player = ['X' , 'O']
    self.grid = ["", "", "", "", "", "", "", "", ""]

    self.select_player()


  def select_player(self):
    self.select_player_label = Label(self.window, text="Selecione o jogador:", bg=self.bg_main, fg=self.fg_main, font=self.font)
    self.select_player_label.place(width=182, height=30, relx=0.16, rely=0.25)

    self.select_player_X = Button(self.window, text="X", command=lambda: [self.register_click(self.player[0]), self.select_player_label.destroy() ,self.select_player_X.destroy(), self.select_player_O.destroy(), self.widgets()], bg=self.bg_medium, fg=self.fg_main, font=self.font_strong)
    self.select_player_X.place(width=55, height=55, relx=0.285, rely=0.38)

    self.select_player_O = Button(self.window, text="O", command=lambda: [self.register_click(self.player[1]), self.select_player_label.destroy() ,self.select_player_X.destroy(), self.select_player_O.destroy(), self.widgets()], bg=self.bg_medium, fg=self.fg_main, font=self.font_strong)
    self.select_player_O.place(width=55, height=55, relx=0.485, rely=0.38)


  def register_click(self, value):
    self.start_player = value


  def widgets(self):        
    self.acctualy_player = self.start_player

    self.banner_menssage = f"O jogador {self.start_player} começa!"
    
    self.banner = Label(self.window, text=self.banner_menssage, bg=self.bg_main, fg=self.fg_main, relief="sunken", font=self.font)
    self.banner.place(width=182, height=30, relx=0.16, rely=0.1)

    self.A1 = Button(self.window, command=lambda: [self.add_position(0), self.A1.configure(state=DISABLED)], activebackground=self.bg_strong, bg=self.bg_medium, fg=self.fg_main, font=self.font_strong)
    self.A1.place(width=55, height=55, relx=0.19, rely=0.3)

    self.A2 = Button(self.window, command=lambda: [self.add_position(1), self.A2.configure(state=DISABLED)], activebackground=self.bg_strong, bg=self.bg_medium, fg=self.fg_main, font=self.font_strong)
    self.A2.place(width=55, height=55, relx=0.39, rely=0.3)

    self.A3 = Button(self.window, command=lambda: [self.add_position(2), self.A3.configure(state=DISABLED)], activebackground=self.bg_strong, bg=self.bg_medium, fg=self.fg_main, font=self.font_strong)
    self.A3.place(width=55, height=55, relx=0.59, rely=0.3)

    self.B1 = Button(self.window, command=lambda: [self.add_position(3), self.B1.configure(state=DISABLED)], activebackground=self.bg_strong, bg=self.bg_medium, fg=self.fg_main, font=self.font_strong)
    self.B1.place(width=55, height=55, relx=0.19, rely=0.5)
    
    self.B2 = Button(self.window, command=lambda: [self.add_position(4), self.B2.configure(state=DISABLED)], activebackground=self.bg_strong, bg=self.bg_medium, fg=self.fg_main, font=self.font_strong)
    self.B2.place(width=55, height=55, relx=0.39, rely=0.5)

    self.B3 = Button(self.window, command=lambda: [self.add_position(5), self.B3.configure(state=DISABLED)], activebackground=self.bg_strong, bg=self.bg_medium, fg=self.fg_main, font=self.font_strong)
    self.B3.place(width=55, height=55, relx=0.59, rely=0.5)

    self.C1 = Button(self.window, command=lambda: [self.add_position(6), self.C1.configure(state=DISABLED)], activebackground=self.bg_strong, bg=self.bg_medium, fg=self.fg_main, font=self.font_strong)
    self.C1.place(width=55, height=55, relx=0.19, rely=0.7)

    self.C2 = Button(self.window, command=lambda: [self.add_position(7), self.C2.configure(state=DISABLED)], activebackground=self.bg_strong, bg=self.bg_medium, fg=self.fg_main, font=self.font_strong)
    self.C2.place(width=55, height=55, relx=0.39, rely=0.7)

    self.C3 = Button(self.window, command=lambda: [self.add_position(8), self.C3.configure(state=DISABLED)], activebackground=self.bg_strong, bg=self.bg_medium, fg=self.fg_main, font=self.font_strong)
    self.C3.place(width=55, height=55, relx=0.59, rely=0.7)


  def add_position(self, position):
    self.position = position
    self.grid[position] = self.acctualy_player

    self.plays += 1

    self.refresh()


  def refresh(self):
    self.A1.configure(text=self.grid[0], disabledforeground="white")    
    self.A2.configure(text=self.grid[1], disabledforeground="white")
    self.A3.configure(text=self.grid[2], disabledforeground="white")

    self.B1.configure(text=self.grid[3], disabledforeground="white")    
    self.B2.configure(text=self.grid[4], disabledforeground="white")
    self.B3.configure(text=self.grid[5], disabledforeground="white")

    self.C1.configure(text=self.grid[6], disabledforeground="white")    
    self.C2.configure(text=self.grid[7], disabledforeground="white")
    self.C3.configure(text=self.grid[8], disabledforeground="white")

    self.game_over()


  def game_over(self):
      count = [0, 0]

      for i in range(3):
        if (self.grid[count[0]] == "X" and self.grid[count[0] + 1] == "X" and self.grid[count[0] + 2] == "X") or (self.grid[count[0]] == "O" and self.grid[count[0] + 1] == "O" and self.grid[count[0] + 2] == "O"):
          messagebox.showinfo("Você venceu!", f"Parabéns! O jogando {self.acctualy_player} venceu!", command=self.master.quit())
        count[0] += 3

      for i in range(3):
        if (self.grid[count[1]] == "X" and self.grid[count[1] + 3] == "X" and self.grid[count[1] + 6] == "X") or (self.grid[count[1]] == "O" and self.grid[count[1] + 3] == "O" and self.grid[count[1] + 6] == "O"):
          messagebox.showinfo("Você venceu!", f"Parabéns! O jogando {self.acctualy_player} venceu!", command=self.master.quit())
        count[1] += 1

      if (self.grid[0] == "X" and self.grid[4] == "X" and self.grid[8] == "X") or (self.grid[0] == "O" and self.grid[4] == "O" and self.grid[8] == "O"):
        messagebox.showinfo("Você venceu!", f"Parabéns! O jogando {self.acctualy_player} venceu!", command=self.master.quit())
      elif (self.grid[2] == "X" and self.grid[4] == "X" and self.grid[6] == "X") or (self.grid[2] == "O" and self.grid[4] == "O" and self.grid[6] == "O"):
        messagebox.showinfo("Você venceu!", f"Parabéns! O jogando {self.acctualy_player} venceu!", command=self.master.quit())
      elif self.plays == 9:
        messagebox.showwarning("Empate", "Todos os campos foram preenchidos não havendo vencedor!", command=self.master.quit())

      self.change_player()


  def change_player(self):
    if self.acctualy_player == self.player[0]:
      self.acctualy_player = self.player[1]
    else:
      self.acctualy_player = self.player[0]

    self.banner.configure(text=f'O jogador {self.acctualy_player} está jogando...')


root = Tk()
game = App(root)
game.mainloop()