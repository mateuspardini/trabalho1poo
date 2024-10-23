import pandas as pd

class Usuario:
    def __init__(self, nome_arquivo="usuarios.json"):
        self.nome_arquivo = nome_arquivo
        try:
            self.df_usuarios = pd.read_json(self.nome_arquivo, orient='records', lines=True)
        except FileNotFoundError:
            self.df_usuarios = pd.DataFrame(columns=["nome", "cargo", "vitorias", "derrotas"])
            self.df_usuarios.to_json('usuarios.json', orient='records', lines=True)

    def adicionar_usuario(self, nome):
        if self.df_usuarios.empty:
            novo_usuario = {
                'nome': nome,
                'vitorias': 0,
                'derrotas': 0
            }
            self.df_usuarios = self.df_usuarios._append(novo_usuario, ignore_index=True)
            self.df_usuarios.to_json('usuarios.json', orient='records', lines=True)
        else:
            if nome in self.df_usuarios['nome'].values:
                print(f"O nome '{nome}' já está cadastrado.")
            else:
                novo_usuario = {
                'nome': nome,
                'vitorias': 0,
                'derrotas': 0
                }
                self.df_usuarios = self.df_usuarios._append(novo_usuario, ignore_index=True)
                self.df_usuarios.to_json('usuarios.json', orient='records', lines=True)

    def obter_ranking(self):
        # Ordena por vitórias (decrescente) e depois por derrotas (crescente)
        ranking = self.df_usuarios.sort_values(by=["vitorias", "derrotas"], ascending=[False, True])
        return ranking

class Jogador(Usuario):
    def __init__(self, nome_usuario):
        super().__init__()
        self.df_usuarios = self.df_usuarios.query('nome == {nome_usuario} and cargo == "jogador"')

    def atualizar_estatisticas(self, nome, ganhou):
        if nome in self.df_usuarios.index:
            if ganhou:
                self.df_usuarios.loc[nome, "vitorias"] += 1
            else:
                self.df_usuarios.loc[nome, "derrotas"] += 1

class Administrador(Usuario):
    def __init__(self, nome_usuario):
        super().__init__()
        self.df_usuarios = self.df_usuarios.query(f'nome == "{nome_usuario}" and cargo == "administrador"')

    def adicionar_palavra(self, palavra):
        print(palavra)