from datetime import datetime

import random as rd

from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont


class HangmanGame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("500x350")
        self.master.configure(background="#2D3239")

        self.font = tkFont.Font(family="Segoe UI", size="10")
        self.fontWord = tkFont.Font(
            family="Segoe UI", size="16", weight=tkFont.BOLD)

        self.frame = Frame(bg="#2D3239", width=500, height=350)
        self.frame.place(relx=0.02, rely=0.02)

        self.trial = 7
        self.state = 0
        self.image = [
            PhotoImage(file="images/forca[0].png"),
            PhotoImage(file="images/forca[1].png"),
            PhotoImage(file="images/forca[2].png"),
            PhotoImage(file="images/forca[3].png"),
            PhotoImage(file="images/forca[4].png"),
            PhotoImage(file="images/forca[5].png"),
            PhotoImage(file="images/forca[6].png"),
        ]

        self.options = [
            "javascript", "python", "java", "php", "c++", "ruby",
            "typescript", "swift", "scala", "shell", "powershell",
            "perl", "kotlin", "haskell"
        ]

        self.randomOption = rd.choice(self.options)

        self.optionSplit = []
        for i in range(0, len(self.randomOption)):
            self.optionSplit.append(self.randomOption[i])

        self.text = "" 

        self.optionHash = []
        for i in range(0, len(self.optionSplit)):
            self.optionHash.append("_ ")
            self.text += self.optionHash[i]

        self.widgetHangman()
        self.widgetTip()
        self.widgetWord()
        self.widgetLog()
        self.widgetInput()

    def widgetHangman(self):
        self.window = Label(
            self.frame, image=self.image[self.state], bg="#363B41", font=self.font)
        self.window.photo = self.image[self.state]
        self.window.place(x=0, y=0)

    def widgetTip(self):
        self.tipText = "Linguagens de programação"
        text = "Dica: " + self.tipText

        self.tip = Label(self.frame, text=text, bg="#363B41",
                         fg="#fff", pady=5, font=self.font)
        self.tip.place(relx=0.455, relwidth=0.5, relheight=0.1)

    def widgetWord(self):
        self.word = Label(
            self.frame,
            text=self.text,
            bg="#2D3239",
            fg="#fff",
            font=self.fontWord
        )
        self.word.place(
            relx=0.455,
            rely=0.11,
            relwidth=0.5,
            relheight=0.1
        )

    def widgetLog(self):
        scrollbar = Scrollbar(self.frame)
        self.log = Listbox(self.frame)

        self.log.configure(wrap=None, bg="#292D31", fg="#fff",
                           font=self.font, yscrollcommand=scrollbar.set)
        self.log.place(relx=0.455, rely=0.23, relwidth=0.4659, relheight=0.62)

        scrollbar.configure(command=self.log.yview)
        scrollbar.place(relx=0.922, rely=0.23, relheight=0.62)

    def widgetInput(self):
        
        self.input = Entry(self.frame, bg="#292D31", fg="#fff", font=self.font)
        self.input.place(relx=0.455, rely=0.865, relwidth=0.4, relheight=0.1)

        self.button = Button(self.frame, command=self.registerLog,
                             bg="#2D3239", fg="#fff", font=self.font)
        self.button.place(relx=0.86, rely=0.865, relwidth=0.1, relheight=0.1)

        self.wdInputHistory = [""]

    def registerLog(self):
        now = datetime.now()
        hh = now.hour
        mm = now.minute
        ss = now.second

        self.wdInput = self.input.get()

        self.registerWord()

        self.validateTrial()

        if self.exists:
            if len(self.wdInput) == 1:
                messagebox.showwarning(
                    "Letra já digitada!", f"A letra: '{self.wdInput}' já foi digitada.")
            elif len(self.wdInput) > 1:
                messagebox.showwarning(
                    "Palavra já digitada!", f"A palavra: '{self.wdInput}' já foi digitada.")
            else:
                messagebox.showwarning(
                    "Caractere Inválido", "Caractere Inválido! Tente novamente!")
        else:
            self.log.insert(END, f"[{hh}:{mm}:{ss}]: {self.wdInput}")

        self.wdInputHistory.append(self.wdInput.lower())

        self.log.see(END)

    def registerWord(self):
        if self.wdInput.lower() in self.wdInputHistory:
            self.exists = True
        else:
            self.exists = False

        self.textModifier = ""
        
        if not self.exists:
            for i in range(0, len(self.optionSplit)):
                if self.wdInput.lower() == self.optionSplit[i]:
                    self.optionHash[i] = str(self.wdInput.lower()) + " "

            for i in range(0, len(self.optionHash)):
                if self.optionHash[i] == "_ ":
                    self.textModifier += "_ "
                else:
                    self.textModifier += self.optionHash[i]  

        self.word.configure(text=self.textModifier)

    def validateTrial(self):
        if not self.wdInput.lower() in self.optionSplit:
            self.trial -= 1
            self.state += 1

            self.window.configure(image=self.image[self.state])
            self.log.insert(END, f"Você possui {self.trial} tentativa(s) restante(s).")

        if self.trial != 0:
            self.winCase()
        else:
            self.loseCase()

    def winCase(self):
        self.textWin = ""
        
        if self.wdInput.lower() == self.randomOption:
            for i in range(0, len(self.optionSplit)):
                self.textWin += self.optionSplit[i] + " "

            self.word.configure(text=self.textWin)

            messagebox.showinfo("You win the Hangman Game!",
                                "Congratulations! You win the Hangman Game!", command=self.master.quit())
        elif self.randomOption == self.textModifier.replace(" ", ""):
            messagebox.showinfo("You win the Hangman Game!",
                                "Congratulations! You win the Hangman Game!", command=self.master.quit())

    def loseCase(self):
        if self.trial == 0:
            messagebox.showalert("Game Over!", "Sorry! Your attempts are over.", command=self.master.quit()) 


root = Tk()
app = HangmanGame(master=root)
app.mainloop()
