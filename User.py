from Utils import Utils
import tkinter as tk

class User:
    def __init__(self, name, role, wins, loses):
        self.name = name
        self.role = role
        self.wins = wins
        self.loses = loses

class Player(User):
    def __init__(self, name, wins, loses):
        super().__init__(name, 'jogador', wins, loses)

    def play(self, hangman, userSystem):
        playing = True
        while playing == True:
            result = hangman.start_game()
            userSystem.update_score(self.name, result)
            userSystem.show_ranking()
            playing = Utils.confirm_action("Deseja jogar novamente? ")

class Admin(User):
    def __init__(self, name, wins, loses):
        super().__init__(name, 'admin', wins, loses)

    def add_word(self, wordSystem, word):
        if len(word) < 3:
            tk.messagebox.showwarning("Aviso", "A palavra deve ter 3 ou mais caracteres.")
        elif word.lower() in wordSystem.df_words['word'].str.lower().values:
            tk.messagebox.showwarning("Aviso", f"A palavra '{word}' já está na lista.")
        else:
            wordSystem.add_word(word)
            tk.messagebox.showinfo("Sucesso", "Palavra adicionada com sucesso!")
