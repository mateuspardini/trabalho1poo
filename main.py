from Hangman import Hangman
from UserSystem import UserSystem
from Utils import Utils
import tkinter as tk
from MainScreen import MainScreen

def main():
    # Cria uma instância da classe Forca com uma lista de palavras
    game = Hangman('words.json')
    userSystem = UserSystem('users.json')
    logged_user = userSystem.auth()
    
    if logged_user.role == 'admin':
        logged_user.add_words(game)
    elif logged_user.role == 'jogador':
        # Inicia o jogo
        logged_user.play(game, userSystem)

main()


# if __name__ == "__main__":
#     root = tk.Tk()
#     tela_principal = MainScreen(root)
#     tela_principal.display()