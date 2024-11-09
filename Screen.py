import tkinter as tk
from abc import ABC, abstractmethod

class Screen(ABC):
    def __init__(self, root):
        self.root = root
        self.root.title()
        self.screen_config()

    @abstractmethod
    def screen_config(self):
        pass

    @abstractmethod
    def display(self):
        pass