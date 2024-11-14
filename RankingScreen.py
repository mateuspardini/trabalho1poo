import tkinter as tk
from tkinter import ttk
from Screen import Screen

class RankingScreen(Screen):
    def __init__(self, root, user):
        super().__init__(root)
        self.root = root
        self.user = user
        self.screen_config()

    def screen_config(self):
        # Limpa os widgets da tela, caso existam
        for widget in self.root.winfo_children():
            widget.destroy()

        # Configurações da tela
        self.root.configure(bg='black')

        # Título da tela "Ranking"
        title_label = tk.Label(self.root, text="Ranking", font=("Helvetica", 32), fg='white', bg='black')
        title_label.pack(pady=20)

        # Frame para mostrar o top 10 rankings
        ranking_frame = tk.Frame(self.root, bg='black')
        ranking_frame.pack(pady=10)
        self.ranking = self.userSystem.get_top_10()
        
        # Adiciona os rankings ao frame
        for idx, rank in enumerate(self.ranking[:10], start=1):
            rank_label = tk.Label(ranking_frame, text=f"{idx}. {rank}", font=("Helvetica", 16), fg='white', bg='black')
            rank_label.pack(anchor='w')

        # Frame para os botões na parte inferior da tela
        button_frame = tk.Frame(self.root, bg='black')
        button_frame.pack(pady=20)

        # Botão "Jogar de Novo"
        play_again_button = tk.Button(button_frame, text="Jogar de Novo", command=self.on_play_again, bg='black', fg='white')
        play_again_button.pack(side="left", padx=10)

        # Botão "Sair para o Menu Principal"
        exit_button = tk.Button(button_frame, text="Menu Principal", command=self.on_exit_to_menu, bg='black', fg='white')
        exit_button.pack(side="left", padx=10)

    def on_play_again(self):
        from GameScreen import GameScreen
    # Limpa todos os widgets da janela atual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Carrega a tela principal na mesma janela
        game_screen = GameScreen(self.root, self.user)
        game_screen.display()

    def on_exit_to_menu(self):
        from MainScreen import MainScreen
    # Limpa todos os widgets da janela atual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Carrega a tela principal na mesma janela
        main_screen = MainScreen(self.root)
        main_screen.display()
        
    def display(self):
        self.root.mainloop()
