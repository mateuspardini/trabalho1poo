from Hangman import Hangman
from UserSystem import UserSystem

import tkinter as tk
from tkinter import messagebox

def show_game_page():
    intro_frame.pack_forget()  # Esconde o frame de introdução
    game_frame.pack()  # Mostra o frame do jogo

# Número inicial de tentativas
attempts = 6

def guess_letter():
    global attempts
    attempts -= 1
    """Desenha o boneco da forca baseado no número de tentativas restantes."""
    canvas.delete("hangman")
    if attempts < 6:
        canvas.create_oval(275, 125, 325, 175, width=4,fill="white")  # Cabeça
    if attempts < 5:
        canvas.create_line(300, 175, 300, 225, width=4,fill="white")  # Corpo
    if attempts < 4:
        canvas.create_line(300, 200, 275, 175, width=4,fill="white")  # Braço esquerdo
    if attempts < 3:
        canvas.create_line(300, 200, 325, 175, width=4,fill="white")  # Braço direito
    if attempts < 2:
        canvas.create_line(300, 225, 275, 250, width=4,fill="white")  # Perna esquerda
    if attempts < 1:
        canvas.create_line(300, 225, 325, 250, width=4,fill="white")  # Perna direita

# Configuração da janela principal
window = tk.Tk()
window.geometry("600x400")
window.title("Jogo da Forca")
window.configure(bg="black")  # Define o fundo da janela principal como preto

# Frame de introdução
intro_frame = tk.Frame(window, bg="black")  # Fundo preto no frame de introdução
intro_label = tk.Label(intro_frame, text="Jogo da Forca", font=("Arial", 24), bg="black", fg="white")  # Texto branco
start_button = tk.Button(intro_frame, text="Iniciar Jogo", font=("Arial", 16), command=show_game_page, bg="black", fg="white")  # Botão com texto branco e fundo preto
intro_label.pack(pady=20)
start_button.pack(pady=10)
intro_frame.pack()

# Frame do jogo principal
game_frame = tk.Frame(window, bg="black")  # Fundo preto no frame do jogo

# Elementos do jogo
word_label = tk.Label(game_frame, text="", font=("Arial", 24), bg="black", fg="white")  # Texto branco
attempts_label = tk.Label(game_frame, text="", font=("Arial", 16), bg="black", fg="white")  # Texto branco
# Canvas para o desenho da forca
canvas = tk.Canvas(game_frame, width=600, height=250, bg="black",highlightthickness=0)  # Fundo preto no canvas
canvas.create_line(200, 250, 400, 250, width=4, fill="white")  # Base branca
canvas.create_line(350, 250, 350, 100, width=4, fill="white")  # Poste vertical branco
canvas.create_line(250, 102, 350, 102, width=4, fill="white")  # Poste horizontal branco
canvas.create_line(300, 100, 300, 120, width=4, fill="white")  # Corda branca
letter_entry = tk.Entry(game_frame, width=5, font=("Arial", 16), bg="black", fg="white")  # Texto e cursor branco no campo de entrada
guess_button = tk.Button(game_frame, text="Chutar letra", font=("Arial", 16), bg="black", fg="white" , command=guess_letter)  # Botão com texto branco e fundo preto  # Define a posição em (150, 300)

# Empacotando os elementos da página do jogo
canvas.pack()
word_label.pack()
attempts_label.pack()
letter_entry.pack()
guess_button.pack()

# Executa a janela principal
window.mainloop()