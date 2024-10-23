from Forca import Forca
from UserSystem import UserSystem


def main():
    # Cria uma instância da classe Forca com uma lista de palavras
    jogo = Forca(["python", "programacao", "computador"])
    userSystem = UserSystem('users.json')
    user = userSystem.auth()
    print(f"Nome: {user.name}\nCargo: {user.role}\nVitorias: {user.wins}\nDerrotas: {user.loses}")
    
    # Inicia o jogo
    while jogo.verificar_fim_de_jogo() == False:
        jogo.exibir_estado()
        palpite = jogo.obter_palpite()
        jogo.verificar_palpite(palpite)

main()