import tkinter as tk
from sqlalchemy import *
from sqlalchemy.exc import SQLAlchemyError
from tkinter import ttk
from funções import Funções

class Application(tk.Tk, Funções):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.title(f"4 Fitness")
        self.geometry("800x600")
        self.Home()

# Janelas

    def menu_inicial(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        label_menu = tk.Label(self, text="Menu Principal", font=("Arial", 24))
        label_menu.pack(pady=20)

        btn_cadastro = tk.Button(self, text="Cadastro de Clientes", command=self.cadastrar_cliente, font=("Arial", 12))
        btn_cadastro.pack(pady=20)

        btn_gerenciador = tk.Button(self, text="Gerenciar Perfis", command=self.Exibir_perfis, font=("Arial", 12))
        btn_gerenciador.pack(pady=20)

        btn_Encerrar = tk.Button(self, text="Encerrar Programa", command=self.Encerrar_programa, font=("Arial", 12))
        btn_Encerrar.pack(pady=20)
        

    def cadastrar_cliente(self):
        for widget in self.winfo_children():
            widget.destroy()

        title = tk.Label(self, text="Cadastrar Cliente", font=('Arial', 20))
        title.pack(pady=20)

        tk.Label(self, text="Nome:", font=("Arial", 10)).pack()
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack(pady=5)

        tk.Label(self, text="Email:", font=("Arial", 10)).pack()
        self.entry_email = tk.Entry(self)
        self.entry_email.pack(pady=5)

        tk.Label(self, text="Senha:", font=("Arial", 10)).pack()
        self.entry_senha = tk.Entry(self)
        self.entry_senha.pack(pady=5)

        tk.Label(self, text="Telefone:", font=("Arial", 10)).pack()
        self.entry_telefone = tk.Entry(self)
        self.entry_telefone.pack(pady=5)

        tk.Label(self, text="Endereço:", font=("Arial", 10)).pack()
        self.entry_endereco = tk.Entry(self)
        self.entry_endereco.pack(pady=5)

        tk.Button(self, text="Cadastrar-se", command=self.validar_dados, font=("Arial", 12)).pack(pady=20)
        tk.Button(self, text="Voltar", command=self.menu_inicial, font=("Arial", 10)).pack(pady=10)

        
    def Exibir_perfis(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        title = tk.Label(self, text="Perfis dos Clientes", font=("Arial", 20))
        title.pack(pady=20)

        colunas = ("ID", "Nome", "Email", "Telefone", "Endereço") 
        self.tree = ttk.Treeview(self, columns=colunas, show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Endereço", text="Endereço")
        self.tree.pack(pady=0, fill=tk.BOTH, expand=True)
        self.carregar_perfis()

        btn_deletar = tk.Button(self, text="Deletar Perfil", command=self.deletar_perfil)
        btn_deletar.pack(pady=10)

        btn_voltar = tk.Button(self, text="Voltar", command=self.menu_inicial, font=("Arial", 10))
        btn_voltar.pack(pady=10)

    def Home(self):
        for widget in self.winfo_children():
            widget.destroy()

        nome_home = tk.Label(self, text="Home", font=("Arial",14))
        nome_home.grid(row=100, column=5, padx=350, pady=20)
        
        # Frame central para os botões
        central_frame = tk.Frame(self)
        central_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Centralizando o frame

        # Colocando os botões lado a lado usando grid
        btn_perfil = tk.Button(central_frame, text="Perfil", command=self.perfil, font=("Arial", 12), width=15)
        btn_perfil.grid(row=0, column=0, padx=10, pady=10)

        btn_treinos = tk.Button(central_frame, text="Treinos", command=self.treinos, font=("Arial", 12), width=15)
        btn_treinos.grid(row=0, column=1, padx=10, pady=10)

        btn_ajustes = tk.Button(central_frame, text="Ajustes", command=self.ajustes, font=("Arial", 12), width=15)
        btn_ajustes.grid(row=0, column=2, padx=10, pady=10)
    