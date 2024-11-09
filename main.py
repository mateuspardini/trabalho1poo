
import tkinter as tk
from MainScreen import MainScreen

if __name__ == "__main__":
    root = tk.Tk()
    tela_principal = MainScreen(root)
    tela_principal.display()