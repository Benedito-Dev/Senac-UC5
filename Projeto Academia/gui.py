import tkinter as tk
from sqlalchemy import *
from sqlalchemy.exc import SQLAlchemyError
from tkinter import ttk
from funções import Funções

class Application(tk.Tk, Funções):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.title("Primeira Janela")
        self.geometry("800x600")
        self.menu_inicial()

# Janelas

    def menu_inicial(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        label_menu = tk.Label(self, text="Bem vindo de volta", font=("Arial", 24))
        label_menu.pack(pady=50)

        btn_cadastro = tk.Button(self, text="Cadastrar clientes", command=self.cadastrar_cliente, font=("Arial", 12))
        btn_cadastro.pack(pady=20)

        btn_gerenciador = tk.Button(self, text="Gerenciar Perfis", command=self.Exibir_perfis, font=("Arial", 12))
        btn_gerenciador.pack(pady=20)

        btn_login = tk.Button(self,text="Login", command=self.realizar_login, font=("Arial", 12))
        btn_login.pack(pady=20)

        btn_Encerrar = tk.Button(self, text="Encerrar Programa", command=self.Encerrar_programa, font=("Arial", 12))
        btn_Encerrar.pack(pady=20, padx=5)

        
    def realizar_login(self):
        for widget in self.winfo_children():
            widget.destroy()

        titulo = tk.Label(self,text="Realizar login", font=("Arial",20))
        titulo.pack(pady=20)

        tk.Label(self, text="Nome:", font=("Arial",10)).pack()
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack(pady=5)

        tk.Label(self, text="Senha:", font=("Arial",10)).pack()
        self.entry_senha = tk.Entry(self,show="*")
        self.entry_senha.pack(pady=5)

        self.check_senha = tk.IntVar()
        check = tk.Checkbutton(self, text="Mostrar senha", variable=self.check_senha, command=self.Exibir_senha)
        check.pack()

        button = tk.Button(self, text="Validar dados", command=self.verificando_usuario, font=("Arial", 10)).pack(10)



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

        self.check_senha = tk.IntVar()

        tk.Label(self, text="Senha:", font=("Arial", 10)).pack()
        self.entry_senha = tk.Entry(self, show="*")
        self.entry_senha.pack(pady=5)

        check_button = tk.Checkbutton(self, text="Exibir Senha", variable=self.check_senha, command=self.Exibir_senha)
        check_button.pack()

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