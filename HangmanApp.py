import tkinter as tk
from tkinter import messagebox
from Hangman import Hangman
from UserSystem import UserSystem
from Utils import Utils

class HangmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")

        # Setup game logic
        self.game = Hangman('words.json')
        self.userSystem = UserSystem('users.json')
        self.logged_user = self.userSystem.auth()

        self.remaining_tries = 0
        self.actual_word = ""
        self.guessed_letters = set()

        # Setup GUI elements
        self.word_label = tk.Label(root, text="Palavra: ", font=("Helvetica", 20))
        self.word_label.pack(pady=10)

        self.tries_label = tk.Label(root, text="Tentativas Restantes: ", font=("Helvetica", 16))
        self.tries_label.pack(pady=5)

        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=10)
        
        self.letter_entry = tk.Entry(self.entry_frame, font=("Helvetica", 18), width=5)
        self.letter_entry.grid(row=0, column=0, padx=5)
        
        self.guess_button = tk.Button(self.entry_frame, text="Adivinhar", font=("Helvetica", 16), command=self.guess_letter)
        self.guess_button.grid(row=0, column=1, padx=5)
        
        self.guessed_label = tk.Label(root, text="Letras Adivinhadas: ", font=("Helvetica", 14))
        self.guessed_label.pack(pady=5)

        # Start the game if user is a player
        if self.logged_user.role == 'jogador':
            self.start_game()
        elif self.logged_user.role == 'admin':
            self.add_words()

    def start_game(self):
        self.actual_word = self.game.df_words.sample(n=1)['word'].iloc[0]
        self.remaining_tries = 6
        self.guessed_letters = set()
        self.update_display()

    def update_display(self):
        displayed_word = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.actual_word])
        self.word_label.config(text=f"Palavra: {displayed_word}")
        self.tries_label.config(text=f"Tentativas Restantes: {self.remaining_tries}")
        self.guessed_label.config(text=f"Letras Adivinhadas: {', '.join(self.guessed_letters)}")

    def guess_letter(self):
        guess = self.letter_entry.get().lower()
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Palpite Inválido", "Por favor, insira uma única letra.")
        elif guess in self.guessed_letters:
            messagebox.showwarning("Letra Repetida", "Você já adivinhou essa letra. Tente outra.")
        else:
            self.guessed_letters.add(guess)
            if guess not in self.actual_word:
                self.remaining_tries -= 1
            self.update_display()
            self.check_game_end()
        self.letter_entry.delete(0, tk.END)

    def check_game_end(self):
        if "_" not in self.word_label.cget("text"):
            messagebox.showinfo("Vitória", "Parabéns! Você ganhou!")
            self.userSystem.update_score(self.logged_user.name, 'win')
            self.userSystem.show_ranking()
            if messagebox.askyesno("Jogar Novamente", "Deseja jogar novamente?"):
                self.start_game()
            else:
                self.root.quit()
        elif self.remaining_tries == 0:
            messagebox.showinfo("Derrota", f"Você perdeu! A palavra era {self.actual_word}")
            self.userSystem.update_score(self.logged_user.name, 'lose')
            self.userSystem.show_ranking()
            if messagebox.askyesno("Jogar Novamente", "Deseja jogar novamente?"):
                self.start_game()
            else:
                self.root.quit()

    def add_words(self):
        add_another_word = True
        while add_another_word:
            word = tk.simpledialog.askstring("Adicionar Palavra", "Insira a palavra que deseja adicionar:").lower()
            if word:
                confirmation = messagebox.askyesno("Confirmação", f"Você tem certeza que deseja inserir a palavra '{word}' no banco?")
                if confirmation:
                    self.game.add_word(word)
            add_another_word = messagebox.askyesno("Adicionar Mais", "Deseja adicionar uma nova palavra?")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
