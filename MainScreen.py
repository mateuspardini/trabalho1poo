import tkinter as tk
from Screen import Screen
from AdminScreen import AdminScreen
from GameScreen import GameScreen
from tkinter import simpledialog, messagebox

class MainScreen(Screen):
    def __init__(self, root):
        super().__init__(root)
        self.screen_config()

    def screen_config(self):
        self.root.geometry("600x500")
        self.root.title("Jogo da Forca")
        self.root.configure(bg="black")

        # Frame de introdução
        intro_frame = tk.Frame(self.root, bg="black")
        intro_frame.pack(fill="both", expand=True)

        # Label do título do jogo
        intro_label = tk.Label(intro_frame, text="Jogo da Forca", font=("Arial", 24), bg="black", fg="white")
        intro_label.pack(pady=20)

        # Nome
        name_label = tk.Label(intro_frame, text="Digite seu nome:", font=("Arial", 16), bg="black", fg="white")
        name_label.pack(pady=5)
        self.name_entry = tk.Entry(intro_frame, font=("Arial", 16), bg="black", fg="white", justify="center", insertbackground="white")
        self.name_entry.bind("<Return>", lambda event: self.auth())
        self.name_entry.focus_set()
        self.name_entry.pack(pady=10)

        # Botão de iniciar o jogo
        start_button = tk.Button(intro_frame, text="Iniciar Jogo", font=("Arial", 16), command=self.auth, bg="black", fg="white")
        start_button.pack(pady=10)


        # Botão para sair do jogo jno canto inferior esquerdo
        exit_button = tk.Button(intro_frame, text="SAIR", font=("Arial", 10), command=self.exit_game, bg="red", fg="white")
        exit_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

        # Ranking
        ranking_label = tk.Label(intro_frame, text="Ranking", font=("Arial", 16), bg="black", fg="white")
        ranking_item1 = tk.Label(intro_frame, text=f"{self.userSystem.get_ranking().iloc[0]['name'].capitalize()} - {self.userSystem.get_ranking().iloc[0]['wins']}W / {self.userSystem.get_ranking().iloc[0]['loses']}L", font=("Arial", 12), bg="black", fg="white")
        ranking_item2 = tk.Label(intro_frame, text=f"{self.userSystem.get_ranking().iloc[1]['name'].capitalize()} - {self.userSystem.get_ranking().iloc[1]['wins']}W / {self.userSystem.get_ranking().iloc[1]['loses']}L", font=("Arial", 12), bg="black", fg="white")
        ranking_item3 = tk.Label(intro_frame, text=f"{self.userSystem.get_ranking().iloc[2]['name'].capitalize()} - {self.userSystem.get_ranking().iloc[2]['wins']}W / {self.userSystem.get_ranking().iloc[2]['loses']}L", font=("Arial", 12), bg="black", fg="white")

        ranking_label.pack(pady=10)
        ranking_item1.pack()
        ranking_item2.pack()
        ranking_item3.pack()

    def auth(self):
        # Verifica se o campo de nome foi preenchido
        if self.name_entry.get().strip() == "":
            messagebox.showwarning("Aviso", "Por favor, insira seu nome antes de continuar.")
        else:
            self.user = self.userSystem.auth(self.name_entry.get().strip())
            if self.user.role == "admin":
                self.open_admin_panel()   
            else:
                # Remove todos os widgets da janela atual (esconde o frame de introdução)
                for widget in self.root.winfo_children():
                    widget.destroy()

                # Carrega a GameScreen na mesma janela
                game_screen = GameScreen(self.root, self.user)
                game_screen.display()     

    def open_admin_panel(self):
        # Solicita a senha do administrador
        password = simpledialog.askstring("Senha de Admin", "Digite a senha de administrador:", show="*")
        
        # Valida a senha (substitua "admin" pela senha desejada)
        if password == "admin":
            for widget in self.root.winfo_children():
                widget.destroy()
            # Cria uma nova janela para o painel de administrador
            admin_screen = AdminScreen(self.root, self.user)
            admin_screen.display()
        else:
            messagebox.showerror("Erro", "Senha incorreta!")

    def exit_game(self):
        # Função placeholder para demonstrar funcionalidade
        self.root.destroy()

    def display(self):
        self.root.mainloop()