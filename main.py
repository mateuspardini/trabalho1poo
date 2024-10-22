from IPython.display import clear_output
from Forca import Forca
from Usuario import Usuario


def main():
    # Cria uma instância da classe Forca com uma lista de palavras
    jogo = Forca(["python", "programacao", "computador"])
    usuario = Usuario()
    usuario.adicionar_usuario("Gustavinho")
    
    # Inicia o jogo
    while jogo.verificar_fim_de_jogo() == False:
        jogo.exibir_estado()
        palpite = jogo.obter_palpite()
        jogo.verificar_palpite(palpite)

# main()
import pandas as pd

df_lido = pd.read_json('dados.json', orient='records', lines=True)
novo_registro = {
    'Nome': 'Daniel',
    'Idade': 28,
    'Cidade': 'Curitiba'
}
df_lido = df_lido._append(novo_registro, ignore_index=True)
df_lido.to_json('dados.json', orient='records', lines=True)
print(df_lido)