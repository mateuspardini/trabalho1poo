import pandas as pd

class Usuario:
    def __init__(self, nome_arquivo="usuarios.csv"):
        self.nome_arquivo = nome_arquivo
        try:
            self.df_usuarios = pd.read_csv(self.nome_arquivo, index_col="nome")
        except FileNotFoundError:
            self.df_usuarios = pd.DataFrame(columns=["nome", "vitorias", "derrotas"])
            self.df_usuarios.set_index("nome", inplace=True)

    def adicionar_usuario(self, nome):
        self.df_usuarios['nome'] = nome
        if nome not in self.df_usuarios.index:
            self.df_usuarios.loc[0, 'nome'] = nome  # Inicializa com 0 vitórias e 0 derrotas
            print(f"{nome}")

    def atualizar_estatisticas(self, nome, ganhou):
        if nome in self.df_usuarios.index:
            if ganhou:
                self.df_usuarios.loc[nome, "vitorias"] += 1
            else:
                self.df_usuarios.loc[nome, "derrotas"] += 1

    def salvar_dados(self):
        self.df_usuarios.to_csv(self.nome_arquivo)

    def obter_ranking(self):
        # Ordena por vitórias (decrescente) e depois por derrotas (crescente)
        ranking = self.df_usuarios.sort_values(by=["vitorias", "derrotas"], ascending=[False, True])
        return ranking