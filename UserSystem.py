import pandas as pd
from User import Player, Admin

class UserSystem:
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            self.df_users = pd.read_json(self.file_name, orient='records', lines=True)
        except FileNotFoundError:
            self.df_users = pd.DataFrame(columns=["name", "role", "wins", "loses"])
            self.df_users.to_json(self.file_name, orient='records', lines=True)

    def add_user(self, name, role):
        new_user = {
            'name': name,
            'role': role,
            'wins': 0,
            'loses': 0
        }
        if self.df_users.empty:
            self.df_users = self.df_users._append(new_user, ignore_index=True)
            self.df_users.to_json('users.json', orient='records', lines=True)
        else:
            if name in self.df_users['name'].values:
                print(f"O nome '{name}' já está cadastrado.")
            else:
                self.df_users = self.df_users._append(new_user, ignore_index=True)
                self.df_users.to_json('users.json', orient='records', lines=True)
        user = self.get_user_class(new_user)
        return user

    def auth(self):
        name = input("Por favor, insira seu nome: ")
        user_data = self.df_users[self.df_users['name'] == name]
        
        if user_data.empty:
            print(f"Usuário {name} não encontrado. Adicionando ao banco.")
            new_user = self.add_user(name, 'jogador')
            return new_user
        else:
            user = self.get_user_class(user_data.iloc[0])
            return user

    def get_user_class(self, user):
        if user['role'] == 'jogador':
            return Player(user['name'], user['wins'], user['loses'])
        elif user['role'] == 'admin':
            password = ''
            while password != 'admin':
                password = input("Insira a senha: ")
                if password == 'admin':
                    print(f"Seja bem vindo {user['name']}")
                else:
                    print("Senha errada!!")
            return Admin(user['name'], user['wins'], user['loses'])