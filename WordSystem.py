import pandas as pd
import random

class WordSystem:
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

    def get_random_word(self):
        return random.choice(self.df_words['word'].tolist())