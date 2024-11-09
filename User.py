from Utils import Utils

class User:
    def __init__(self, name, role, wins, loses):
        self.name = name
        self.role = role
        self.wins = wins
        self.loses = loses

class Player(User):
    def __init__(self, name, wins, loses):
        super().__init__(name, 'jogador', wins, loses)

    def play(self, hangman, userSystem):
        playing = True
        while playing == True:
            result = hangman.start_game()
            userSystem.update_score(self.name, result)
            playing = Utils.confirm_action("Deseja jogar novamente? ")

class Admin(User):
    def __init__(self, name, wins, loses):
        super().__init__(name, 'admin', wins, loses)

    def add_words(self, hangman):
        add_another_word = True
        while add_another_word == True:
            confirmation = False
            word = ''
            while confirmation == False:
                word = input("Insira a palavra que deseja adicionar: ").lower()
                confirmation = Utils.confirm_action(f"Você tem certeza que deseja inserir a palavra {word} no banco? ")
            hangman.add_word(word.lower())
            add_another_word = Utils.confirm_action("Deseja adicionar uma nova palavra? ")
