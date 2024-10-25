import pandas as pd

class Hangman:
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            self.df_words = pd.read_json(self.file_name, orient='records', lines=True)
        except FileNotFoundError:
            self.df_words = pd.DataFrame(columns=["word"])
            self.df_words.to_json(self.file_name, orient='records', lines=True)

    def add_word(self, word):
        if len(word) < 3:
            print(f"A palavra deve ter 3 ou mais caracteres.")
        elif word.lower() in self.df_words['word'].str.lower().values:
            print(f"A palavra '{word}' já está na lista.")
        else:
            self.df_words = self.df_words._append({'word': word}, ignore_index=True)
            self.df_words.to_json(self.file_name, orient='records', lines=True)
            print(f"Palavra '{word}' adicionada com sucesso!")