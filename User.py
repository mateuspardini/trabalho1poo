class User:
    def __init__(self, name, role, wins, loses):
        self.name = name
        self.role = role
        self.wins = wins
        self.loses = loses

class Player(User):
    def __init__(self, name, wins, loses):
        super().__init__(name, 'jogador', wins, loses)

class Admin(User):
    def __init__(self, name, wins, loses):
        super().__init__(name, 'admin', wins, loses)