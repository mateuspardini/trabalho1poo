from Hangman import Hangman
from UserSystem import UserSystem

import random
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Lista de palavras possíveis
palavras = ["programacao", "computador", "python", "jogos", "algoritmo"]

# Seleciona uma palavra aleatória no início do jogo
palavra = random.choice(palavras)
revealed_word = ["_" for _ in palavra] # Gera um vetor de sublinhados para cada letra da palavra


    

def show_game_page():
    # Verifica se o campo de nome foi preenchido
    if name_entry.get().strip() == "":
        messagebox.showwarning("Aviso", "Por favor, insira seu nome antes de continuar.")
    else:
        intro_frame.pack_forget()  # Esconde o frame de introdução
        game_frame.pack(fill="both", expand=True)

def open_admin_panel():
    # Solicita a senha do administrador
    password = simpledialog.askstring("Senha de Admin", "Digite a senha de administrador:", show="*")
    
    # Valida a senha (substitua "admin123" pela senha desejada)
    if password == "admin":
        intro_frame.pack_forget()  # Esconde o frame de introdução
        admin_frame.pack(fill="both", expand=True)
    else:
        messagebox.showerror("Erro", "Senha incorreta!")

def add_word():
    if add_word_entry.get().strip() == "":
         messagebox.showwarning("Aviso", "Insira uma palavra válida.")
    else:
        messagebox.showinfo("","Palavra Adicionada")
def back():
    admin_frame.pack_forget()
    intro_frame.pack(fill="both", expand=True)

# Número inicial de tentativas
attempts = 6

def guess_letter():
    global attempts
    attempts -= 1
    revealed_word_label.config(text=" ".join(revealed_word))
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
window.geometry("600x500")
window.title("Jogo da Forca")
window.configure(bg="black")  # Define o fundo da janela principal como preto
# Frame de introdução
# Configurações do frame de introdução
intro_frame = tk.Frame(window, bg="black")
intro_frame.pack(fill="both", expand=True)

# Label do título do jogo
intro_label = tk.Label(intro_frame, text="Jogo da Forca", font=("Arial", 24), bg="black", fg="white")
intro_label.pack(pady=20)

#name
name_label = tk.Label(intro_frame, text="Digite seu nome:", font=("Arial", 16), bg="black", fg="white")
name_label.pack(pady=5)
name_entry = tk.Entry(intro_frame, font=("Arial", 16), bg="black", fg="white", justify="center")
name_entry.pack(pady=10)

# Botão de iniciar o jogo
start_button = tk.Button(intro_frame, text="Iniciar Jogo", font=("Arial", 16), command=show_game_page, bg="black", fg="white")
start_button.pack(pady=10)

# Botão de administrador no canto inferior direito
admin_button = tk.Button(intro_frame, text="Admin", font=("Arial", 10), command=open_admin_panel, bg="black", fg="white")
admin_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)  # Posição no canto inferior direito com margens

#Ranking
ranking_label = tk.Label(intro_frame, text="Ranking", font=("Arial", 16), bg="black", fg="White")
ranking_item1 =  tk.Label (intro_frame, text="Mateus - 3 W", font=("Arial", 12), bg="black", fg="White")
ranking_item2 =  tk.Label (intro_frame, text="Gustavo - 2 W", font=("Arial", 12), bg="black", fg="White")
ranking_item3 =  tk.Label (intro_frame, text="Gabriela - 1 W", font=("Arial", 12), bg="black", fg="White")

ranking_label.pack(pady=10)
ranking_item1.pack()
ranking_item2.pack()
ranking_item3.pack()


admin_frame = tk.Frame(window, bg="black")

add_word_label = tk.Label(admin_frame, text="Insira a palavra a ser adicionada:", font=("Arial", 16), bg="black", fg="white")
add_word_label .pack(pady=5)
add_word_entry = tk.Entry(admin_frame, font=("Arial", 16), bg="black", fg="white", justify="center")
add_word_entry.pack(pady=10)
add_word_button = tk.Button(admin_frame, text="Confirmar palavra", font=("Arial", 16), command=add_word, bg="black", fg="white")
add_word_button.pack(pady=10)

back_button = tk.Button(admin_frame, text="Voltar", font=("Arial", 10), command=back, bg="black", fg="white")
back_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

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

# Label para exibir a palavra parcialmente revelada com tracejados
revealed_word_label = tk.Label(game_frame, font=("Arial", 24), bg="black", fg="white")

# Inicializa o texto do label com os tracejados equivalentes ao número de letras

letter_entry = tk.Entry(game_frame, width=5, font=("Arial", 16), bg="black", fg="white")  # Texto e cursor branco no campo de entrada
guess_button = tk.Button(game_frame, text="Chutar letra", font=("Arial", 16), bg="black", fg="white" , command=guess_letter)  # Botão com texto branco e fundo preto  # Define a posição em (150, 300)

# Empacotando os elementos da página do jogo
canvas.pack()
word_label.pack()
attempts_label.pack()
revealed_word_label.pack()
letter_entry.pack(pady=10)
guess_button.pack()


# Executa a janela principal
window.mainloop()