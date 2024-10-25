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

    def add_words(self, hangman):
        add_another_word = True
        while add_another_word == True:
            confirmation = False
            word = ''
            while confirmation == False:
                word = input("Insira a palavra que deseja adicionar: ")
                confirmation = self.confirm_action(f"Você tem certeza que deseja inserir a palavra {word} no banco? ")
            hangman.add_word(word)
            add_another_word = self.confirm_action("Deseja adicionar uma nova palavra? ")


    def confirm_action(self, message):
        while True:
            resposta = input(message).lower()
            if resposta in ['s', 'sim']:
                return True
            elif resposta in ['n', 'não', 'nao']:
                return False
            else:
                print("Por favor, responda com 's' para sim ou 'n' para não.")
