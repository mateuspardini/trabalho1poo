import tkinter as tk
from Screen import Screen


class RankingScreen(Screen):
    def screen_config(self):
        self.root.geometry("600x500")
        self.root.configure(bg="black")

        # Frame de administração
        admin_frame = tk.Frame(self.root, bg="black")
        admin_frame.pack(fill="both", expand=True)

        # Label para inserir palavras
        add_word_label = tk.Label(admin_frame, text="Insira a palavra a ser adicionada:", font=("Arial", 16), bg="black", fg="white")
        add_word_label.pack(pady=5)

        # Entrada de texto para a palavra
        add_word_entry = tk.Entry(admin_frame, font=("Arial", 16), bg="black", fg="white", justify="center")
        add_word_entry.pack(pady=10)

        # Botão para confirmar a palavra
        add_word_button = tk.Button(admin_frame, text="Confirmar palavra", font=("Arial", 16), command=self.add_word, bg="black", fg="white")
        add_word_button.pack(pady=10)

        # Botão para voltar
        back_button = tk.Button(admin_frame, text="Voltar", font=("Arial", 10), command=self.back, bg="black", fg="white")
        back_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

    def display(self):
        self.root.mainloop()

    def add_word(self):
        # Função placeholder para adicionar lógica de adicionar palavra
        print("Palavra adicionada (a lógica pode ser implementada aqui)")

    def back(self):
        from MainScreen import MainScreen
        # Limpa todos os widgets da janela atual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Carrega a tela principal na mesma janela
        main_screen = MainScreen(self.root)
        main_screen.display()