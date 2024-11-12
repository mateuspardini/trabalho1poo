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
            self.df_users.to_json(self.file_name, orient='records', lines=True)
        else:
            if name in self.df_users['name'].values:
                print(f"O nome '{name}' já está cadastrado.")
            else:
                self.df_users = self.df_users._append(new_user, ignore_index=True)
                self.df_users.to_json(self.file_name, orient='records', lines=True)
        user = self.get_user_class(new_user)
        return user

    def auth(self, name):
        user_data = self.df_users[self.df_users['name'] == name]
        
        if user_data.empty:
            new_user = self.add_user(name, 'jogador')
            return new_user
        else:
            user = self.get_user_class(user_data.iloc[0])
            return user

    def get_user_class(self, user):
        if user['role'] == 'jogador':
            return Player(user['name'], user['wins'], user['loses'])
        elif user['role'] == 'admin':
            return Admin(user['name'], user['wins'], user['loses'])

    def update_score(self, name, result):
        if name in self.df_users['name'].values:
            index = self.df_users.index[self.df_users['name'] == name].tolist()[0]
            if result == 'win':
                self.df_users.loc[index, "wins"] += 1
            elif result == 'lose':
                self.df_users.loc[index, "loses"] += 1
        else:
            print("Usuário não encontrado")
        self.df_users.to_json(self.file_name, orient='records', lines=True)

    def get_ranking(self):
        sorted_players = self.df_users[self.df_users['role'] == 'jogador'].sort_values(by=['wins', 'loses'], ascending=[False, True])
        return sorted_players