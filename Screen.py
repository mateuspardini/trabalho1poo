import tkinter as tk
from abc import ABC, abstractmethod
from Hangman import Hangman
from UserSystem import UserSystem

class Screen(ABC):
    def __init__(self, root):
        self.root = root
        self.root.title()
        self.game = Hangman('words.json')
        self.userSystem = UserSystem('users.json')

    @abstractmethod
    def screen_config(self):
        pass

    @abstractmethod
    def display(self):
        pass