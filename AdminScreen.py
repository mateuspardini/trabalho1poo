import tkinter as tk
from Screen import Screen


class AdminScreen(Screen):
    def __init__(self, root, user):
        super().__init__(root)
        self.user = user
        self.screen_config()

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
        self.add_word_entry = tk.Entry(admin_frame, font=("Arial", 16), bg="black", fg="white", justify="center",insertbackground="white")
        self.add_word_entry.bind("<Return>", lambda event: self.add_word())
        self.add_word_entry.focus_set()
        self.add_word_entry.pack(pady=10)

        # Botão para confirmar a palavra
        add_word_button = tk.Button(admin_frame, text="Confirmar palavra", font=("Arial", 16), command=self.add_word, bg="black", fg="white")
        add_word_button.pack(pady=10)

        # Botão para voltar
        back_button = tk.Button(admin_frame, text="Voltar", font=("Arial", 10), command=self.back, bg="black", fg="white")
        back_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

    def display(self):
        self.root.mainloop()

    def add_word(self):
        self.user.add_word(self.wordSystem, self.add_word_entry.get().strip())
        self.add_word_entry.delete(0, tk.END)

    def back(self):
        from MainScreen import MainScreen
    # Limpa todos os widgets da janela atual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Carrega a tela principal na mesma janela
        main_screen = MainScreen(self.root)
        main_screen.display()