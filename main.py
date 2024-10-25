from Hangman import Hangman
from UserSystem import UserSystem


def main():
    # Cria uma instância da classe Forca com uma lista de palavras
    game = Hangman('words.json')
    userSystem = UserSystem('users.json')
    logged_user = userSystem.auth()
    
    if logged_user.role == 'admin':
        logged_user.add_words(game)
    elif logged_user.role == 'jogador':
        # Inicia o jogo
        while jogo.verificar_fim_de_jogo() == False:
            jogo.exibir_estado()
            palpite = jogo.obter_palpite()
            jogo.verificar_palpite(palpite)

main()