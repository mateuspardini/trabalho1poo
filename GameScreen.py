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

        # Frame do jogo
        game_frame = tk.Frame(self.root, bg="black")
        game_frame.pack(fill="both", expand=True)

        # Campo de entrada para o jogador inserir uma letra
        self.letter_entry = tk.Entry(game_frame, font=("Arial", 16), bg="black", fg="white", justify="center")
        

        # Botão para confirmar o palpite
        self.guess_button = tk.Button(game_frame, text="Chutar Letra", font=("Arial", 16), command=self.guess_letter, bg="black", fg="white")
        

        # Botão para voltar à tela principal
        back_button = tk.Button(game_frame, text="Voltar", font=("Arial", 10), command=self.back, bg="black", fg="white")
        back_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

        self.canvas = tk.Canvas(game_frame, width=600, height=250, bg="black",highlightthickness=0)  # Fundo preto no canvas
        self.canvas.create_line(200, 250, 400, 250, width=4, fill="white")  # Base branca
        self.canvas.create_line(350, 250, 350, 100, width=4, fill="white")  # Poste vertical branco
        self.canvas.create_line(250, 102, 350, 102, width=4, fill="white")  # Poste horizontal branco
        self.canvas.create_line(300, 100, 300, 120, width=4, fill="white")  # Corda branca
        self.canvas.pack()
        self.letter_entry.pack(pady=10)
        self.guess_button.pack(pady=10)

    def display(self):
        self.root.mainloop()

    def guess_letter(self):
        # Função para processar o chute de uma letra
        letter = self.letter_entry.get().strip()
        if not letter:
            messagebox.showwarning("Aviso", "Por favor, insira uma letra.")
            return

        self.letter_entry.delete(0, tk.END)
        self.reduce_attempts()  

    def reduce_attempts(self):
        """Reduz as tentativas em 1 e desenha parte do boneco."""
        self.attempts -= 1

        # Desenha o boneco da forca com base no número de tentativas restantes
        if self.attempts < 6:
            self.canvas.create_oval(275, 120, 325, 170, width=4, fill="white")  # Cabeça
        if self.attempts < 5:
            self.canvas.create_line(300, 170, 300, 220, width=4, fill="white")  # Corpo
        if self.attempts < 4:
            self.canvas.create_line(300, 195, 275, 170, width=4, fill="white")  # Braço esquerdo
        if self.attempts < 3:
            self.canvas.create_line(300, 195, 325, 170, width=4, fill="white")  # Braço direito
        if self.attempts < 2:
            self.canvas.create_line(300, 220, 275, 245, width=4, fill="white")  # Perna esquerda
        if self.attempts < 1:
            self.canvas.create_line(300, 220, 325, 245, width=4, fill="white")  # Perna direita



    def back(self):
        from MainScreen import MainScreen  # Certifique-se de que o caminho está correto
        # Limpa todos os widgets da janela atual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Carrega a tela principal na mesma janela
        main_screen = MainScreen(self.root)
        main_screen.display()
