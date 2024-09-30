import tkinter as tk
from sqlalchemy import *
from sqlalchemy.exc import SQLAlchemyError
from tkinter import ttk
from funções import Funções
from tkcalendar import Calendar

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
        
        label_menu = tk.Label(self, text="4 Fitness", font=("Arial", 24))
        label_menu.pack(pady=50)

        btn_login = tk.Button(self,text="Login", command=self.realizar_login, font=("Arial", 12))
        btn_login.pack(pady=20)

        btn_gerenciador = tk.Button(self, text="Gerenciar Perfis", command=self.Exibir_perfis, font=("Arial", 12))
        btn_gerenciador.pack(pady=20)

        btn_Encerrar = tk.Button(self, text="Encerrar Programa", command=self.Encerrar_programa, font=("Arial", 12))
        btn_Encerrar.pack(pady=20, padx=5)

    def Home(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Estilização da Janela
        self.configure(bg="black")

        # Frame superior com o título e plano
        frame_superior = tk.Frame(self, bg="black")
        frame_superior.pack(side="top", fill="x", pady=10)

        title = tk.Label(frame_superior, text="4 FITNESS", fg="white", bg="black", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        plano_label = tk.Label(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", fg="white", bg="black", font=("Arial", 12))
        plano_label.pack(side="right", padx=20)

        # Frame central para os botões
        central_frame = tk.Frame(self, bg="black")
        central_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Centralizando o frame

        # Colocando os botões lado a lado usando grid
        btn_perfil = tk.Button(central_frame, text="Perfil", command=self.perfil, font=("Arial", 12, "bold"), width=15, height=5)
        btn_perfil.grid(row=0, column=0, padx=20, pady=20)

        btn_treinos = tk.Button(central_frame, text="Treinos", command=self.treinos, font=("Arial", 12, "bold"), width=15, height=5)
        btn_treinos.grid(row=0, column=1, padx=20, pady=20)

        btn_ajustes = tk.Button(central_frame, text="Ajustes", command=self.ajustes, font=("Arial", 12, "bold"), width=15, height=5)
        btn_ajustes.grid(row=0, column=2, padx=20, pady=20)


        # Configurar expansão de colunas
        central_frame.grid_columnconfigure(0, weight=1)
        central_frame.grid_columnconfigure(1, weight=1)
        central_frame.grid_columnconfigure(2, weight=1)

    def realizar_login(self):
        # Remove widgets existentes
        for widget in self.winfo_children():
            widget.destroy()

        # Configurações da janela para centralização
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        self.grid_rowconfigure(6, weight=1)  # Espaço na parte inferior

        # Frame para centralizar o conteúdo
        frame = tk.Frame(self)
        frame.grid(row=1, column=0, columnspan=2)

        # Título
        titulo = tk.Label(frame, text="Realizar login", font=("Arial", 20))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Nome do usuário
        tk.Label(frame, text="Nome:", font=("Arial", 10)).grid(row=1, column=0, sticky="e", padx=10)
        self.entry_nome = tk.Entry(frame)
        self.entry_nome.grid(row=1, column=1, pady=5)

        # Senha
        tk.Label(frame, text="Senha:", font=("Arial", 10)).grid(row=2, column=0, sticky="e", padx=10)
        self.entry_senha = tk.Entry(frame, show="*")
        self.entry_senha.grid(row=2, column=1, pady=5)

        # Checkbutton para mostrar senha
        self.check_senha = tk.IntVar()
        check = tk.Checkbutton(frame, text="Mostrar senha", variable=self.check_senha, command=self.Exibir_senha)
        check.grid(row=3, column=0, columnspan=2, pady=5)

        # Botão de validar
        tk.Button(frame, text="Validar dados", command=self.validar_login, font=("Arial", 10)).grid(row=4, column=0, columnspan=2, pady=10)

    # Botão de criar conta
        tk.Button(frame, text="Cadastrar-se", command=self.cadastrar_cliente, font=("Arial", 8)).grid(row=5, column=0, columnspan=2, pady=10)

        # Botão de voltar
        tk.Button(frame, text="Voltar", command=self.menu_inicial, font=("Arial", 10)).grid(row=6, column=0, columnspan=2, pady=10)

    def cadastrar_cliente(self):
        # Remove widgets existentes
        for widget in self.winfo_children():
            widget.destroy()

        # Configurações da janela para centralização
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        self.grid_rowconfigure(6, weight=1)  # Espaço na parte inferior

        # Frame para centralizar o conteúdo
        frame = tk.Frame(self)
        frame.grid(row=1, column=0, columnspan=2)

        # Título
        title = tk.Label(frame, text="Cadastrar Cliente", font=('Arial', 20))
        title.grid(row=0, column=0, columnspan=2, pady=10)

        # Nome
        tk.Label(frame, text="Nome:", font=("Arial", 10)).grid(row=1, column=0, sticky="e", padx=10)
        self.entry_nome = tk.Entry(frame)
        self.entry_nome.grid(row=1, column=1, pady=5)

        # Email
        tk.Label(frame, text="Email:", font=("Arial", 10)).grid(row=2, column=0, sticky="e", padx=10)
        self.entry_email = tk.Entry(frame)
        self.entry_email.grid(row=2, column=1, pady=5)

        # Senha
        tk.Label(frame, text="Senha:", font=("Arial", 10)).grid(row=3, column=0, sticky="e", padx=10)
        self.entry_senha = tk.Entry(frame, show="*")
        self.entry_senha.grid(row=3, column=1, pady=5)

        # Checkbutton para mostrar senha
        self.check_senha = tk.IntVar()
        check_button = tk.Checkbutton(frame, text="Exibir Senha", variable=self.check_senha, command=self.Exibir_senha)
        check_button.grid(row=4, column=1, sticky="w", padx=10)  # Posicionando à esquerda

        # Telefone
        tk.Label(frame, text="Telefone:", font=("Arial", 10)).grid(row=5, column=0, sticky="e", padx=10)
        self.entry_telefone = tk.Entry(frame)
        self.entry_telefone.grid(row=5, column=1, pady=5)

        # Endereço
        tk.Label(frame, text="Endereço:", font=("Arial", 10)).grid(row=6, column=0, sticky="e", padx=10)
        self.entry_endereco = tk.Entry(frame)
        self.entry_endereco.grid(row=6, column=1, pady=5)

        #CPF 
        tk.Label(frame, text="CPF", font=("Arial",10)).grid(row=7, column=0, sticky="e",padx=10)
        self.entry_cpf = tk.Entry(frame)
        self.entry_cpf.grid(row=7,column=1, pady=5)
        
        #Data de nascimento 
        tk.Label(frame, text="Data de nascimento", font=("Arial",10)).grid(row=8,column=0, sticky="e", padx=10)
        
        self.entry_dataDeNascimento = tk.Entry(frame)
        self.entry_dataDeNascimento.grid(row=8,column=1,pady=5)

        btn_abrir_calendario = ttk.Button(frame, text="Escolher data", command=self.abrir_calendario)
        btn_abrir_calendario.grid(row=8, column=2,padx=10)

        
        #
        btn_botao_escolher_plano = tk.Button(frame, text="Escolher plano", command=self.escolher_plano, font=("Arial",10))
        btn_botao_escolher_plano.grid(row=9, column=1, columnspan=2,pady=10)
    
        
        # Botão Cadastrar-se
        tk.Button(frame, text="Cadastrar-se", command=self.validar_dados, font=("Arial", 12)).grid(row=9, column=0, columnspan=2, pady=10)

        # Botão Voltar
        tk.Button(frame, text="Voltar", command=self.realizar_login, font=("Arial", 10)).grid(row=10, column=0, columnspan=2, pady=10)

    def abrir_calendario(self):
        janela_calendario = tk.Toplevel(self)
        janela_calendario.title("Selecione a data de nascimento")

        calendario = Calendar(janela_calendario,selectmode="day",year=2000,month=1,day=10)
        calendario.pack(pady=20)

        def pegar_data():
            data_selecionada = calendario.get_date()
            self.entry_dataDeNascimento.delete(0,tk.END)
            self.entry_dataDeNascimento.insert(0,data_selecionada)
            janela_calendario.destroy()
            
        btn_selecionar_data = ttk.Button(janela_calendario,text="Selecionar",command=pegar_data)
        btn_selecionar_data.pack(pady=10)


    def escolher_plano(self):
        for widget in self.winfo_children():
            widget.destroy()    
    
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