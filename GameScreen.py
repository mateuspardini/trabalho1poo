import tkinter as tk
from Screen import Screen
from tkinter import messagebox

class GameScreen(Screen):

    def __init__(self, root):
        super().__init__(root)
        self.attempts = 6


    def screen_config(self):
        self.root.geometry("600x500")
        self.root.configure(bg="black")

        self.word_to_guess = "computador"
        self.guessed_word = ["_"] * len(self.word_to_guess)  # Inicializa com underscores
        self.guessed_letters = set()  # Letras já chutadas
        self.wrong_letters = set() # Letras erradas chutadas

        # Frame do jogo
        game_frame = tk.Frame(self.root, bg="black")
        game_frame.pack(fill="both", expand=True)

        # Campo de entrada para o jogador inserir uma letra
        self.letter_entry = tk.Entry(game_frame, font=("Arial", 16), bg="black", fg="white", justify="center", insertbackground="white")
        self.letter_entry.bind("<Return>", lambda event: self.guess_letter())
        self.letter_entry.focus_set()

        # Campo que mostrará a palavra
        self.word_label = tk.Label(game_frame, text=" ".join(self.guessed_word), font=("Arial", 16), bg="black", fg="white")

        # Campo que mostrará as letras erradas
        self.wrong_letters_label = tk.Label(game_frame, text="LETRAS ERRADAS: ", font=("Arial", 12, "bold"), bg="black", fg="red")

        # Botão para confirmar o palpite
        self.guess_button = tk.Button(game_frame, text="Chutar Letra", font=("Arial", 16), command=self.guess_letter, bg="black", fg="white")

        # Canvas para desenhar a forca
        self.canvas = tk.Canvas(game_frame, width=600, height=250, bg="black", highlightthickness=0)
        self.canvas.create_line(200, 250, 400, 250, width=4, fill="white")  # Base branca
        self.canvas.create_line(350, 250, 350, 100, width=4, fill="white")  # Poste vertical branco
        self.canvas.create_line(250, 102, 350, 102, width=4, fill="white")  # Poste horizontal branco
        self.canvas.create_line(300, 100, 300, 120, width=4, fill="white")  # Corda branca
        self.canvas.pack()
        self.word_label.pack(pady=5)
        self.wrong_letters_label.pack(pady=5)
        self.letter_entry.pack(pady=10)
        self.guess_button.pack(pady=10)

    def display(self):
        self.root.mainloop()

    def guess_letter(self):
        # Função para processar o chute de uma letra
        letter = self.letter_entry.get().strip().lower()

        if not letter:
            messagebox.showwarning("Aviso", "Por favor, insira uma letra.")
            self.letter_entry.delete(0, tk.END)
            
            return

        if len(letter) > 1:
            messagebox.showwarning("Aviso", "Por favor, insira apenas uma letra.")
            self.letter_entry.delete(0, tk.END)
            return

        if letter in self.guessed_letters:
            messagebox.showwarning("Aviso", "Você já chutou essa letra.")
            self.letter_entry.delete(0, tk.END)
            return

        self.guessed_letters.add(letter)
        self.letter_entry.delete(0, tk.END)

        if letter in self.word_to_guess:
            # Atualiza a palavra adivinhada
            for index, char in enumerate(self.word_to_guess):
                if char == letter:
                    self.guessed_word[index] = letter

            # Atualiza o label com a palavra adivinhada
            self.word_label.config(text=" ".join([letter.upper() for letter in self.guessed_word]))

            # Verifica se o jogador adivinhou a palavra completa
            if "_" not in self.guessed_word:
                messagebox.showinfo("Parabéns!", "Você adivinhou a palavra!")
                self.reset_game()
        else:
            # Adiciona a letra errada à lista e atualiza o label
            self.wrong_letters.add(letter)
            self.wrong_letters_label.config(text="LETRAS ERRADAS:" + ", ".join([letter.upper() for letter in self.wrong_letters]))
        self.guessed_letters.add(letter)
        self.letter_entry.delete(0, tk.END)

        if letter in self.word_to_guess:
            # Atualiza a palavra adivinhada
            for index, char in enumerate(self.word_to_guess):
                if char == letter:
                    self.guessed_word[index] = letter

            # Atualiza o label com a palavra adivinhada
            self.word_label.config(text=" ".join([letter.upper() for letter in self.guessed_word]))

            # Verifica se o jogador adivinhou a palavra completa
            if "_" not in self.guessed_word:
                messagebox.showinfo("Parabéns!", "Você adivinhou a palavra!")
                self.reset_game()
        else:
            self.reduce_attempts()

    def reduce_attempts(self):
        """Reduz as tentativas em 1 e desenha parte do boneco."""
        self.attempts -= 1

        # Desenha o boneco da forca com base no número de tentativas restantes
        if self.attempts == 5:
            self.canvas.create_oval(275, 120, 325, 170, width=4, fill="white")  # Cabeça
        elif self.attempts == 4:
            self.canvas.create_line(300, 170, 300, 220, width=4, fill="white")  # Corpo
        elif self.attempts == 3:
            self.canvas.create_line(300, 195, 275, 170, width=4, fill="white")  # Braço esquerdo
        elif self.attempts == 2:
            self.canvas.create_line(300, 195, 325, 170, width=4, fill="white")  # Braço direito
        elif self.attempts == 1:
            self.canvas.create_line(300, 220, 275, 245, width=4, fill="white")  # Perna esquerda
        elif self.attempts == 0:
            self.canvas.create_line(300, 220, 325, 245, width=4, fill="white")  # Perna direita
            messagebox.showinfo("Fim de Jogo", f"Você perdeu! A palavra era '{self.word_to_guess}'.")
            self.reset_game()

    def reset_game(self):
        """Reseta o jogo para um novo início."""
        self.attempts = 6
        self.guessed_word = ["_"] * len(self.word_to_guess)
        self.wrong_letters.clear()
        self.guessed_letters.clear()
        self.wrong_letters_label.config(text="LETRAS ERRADAS:" + ", ".join([letter.upper() for letter in self.wrong_letters]))
        self.canvas.delete("all")
        # Redesenha a estrutura da forca
        self.canvas.create_line(200, 250, 400, 250, width=4, fill="white")
        self.canvas.create_line(350, 250, 350, 100, width=4, fill="white")
        self.canvas.create_line(250, 102, 350, 102, width=4, fill="white")
        self.canvas.create_line(300, 100, 300, 120, width=4, fill="white")
        # Atualiza o label com a palavra adivinhada
        self.word_label.config(text=" ".join(self.guessed_word))
