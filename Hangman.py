import pandas as pd
import random

class Hangman:
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            self.df_words = pd.read_json(self.file_name, orient='records', lines=True)
        except FileNotFoundError:
            self.df_words = pd.DataFrame(columns=["word"])
            self.df_words.to_json(self.file_name, orient='records', lines=True)

    def add_word(self, word):
            self.df_words = self.df_words._append({'word': word}, ignore_index=True)
            self.df_words.to_json(self.file_name, orient='records', lines=True)

    def show_state(self):
      from IPython.display import clear_output
      clear_output(wait=True)
      displayed_word = ""
      for letter in self.actual_word:
          if letter in self.guessed_letters:
              displayed_word += letter
          else:
              displayed_word += "_"
      print(displayed_word)
      print("Tentativas restantes:", self.remaining_tries)
      if self.guessed_letters:
          print("Letras adivinhadas:", ", ".join(self.guessed_letters))
      return displayed_word

    def get_guess(self):
        while True:
            guess = input("Digite uma letra: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Palpite inválido. Digite uma única letra.")
            elif guess in self.guessed_letters:
                print("Você já adivinhou essa letra. Tente outra.")
            else:
                return guess

    def verify_guess(self, guess):
        if guess in self.actual_word:
            self.guessed_letters.add(guess)
            return True
        else:
            self.remaining_tries -= 1
            self.guessed_letters.add(guess)
            return False

    def check_game_end(self):
        if "_" not in self.show_state():
            print("Parabéns! Você ganhou!")
            self.result = 'win'
            return True
        elif self.remaining_tries == 0:
            print("Você perdeu! A palavra era", self.actual_word)
            self.result = 'lose'
            return True
        else:
            return False

    def start_game(self):
        self.actual_word = self.df_words.sample(n=1)['word'].iloc[0]
        self.remaining_tries = 6
        self.guessed_letters = set()
        while self.check_game_end() == False:
            self.show_state()
            guess = self.get_guess()
            self.verify_guess(guess)
        return self.result