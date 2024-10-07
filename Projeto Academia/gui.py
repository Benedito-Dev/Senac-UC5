import tkinter as tk
from sqlalchemy import *
from sqlalchemy.exc import SQLAlchemyError
from tkinter import ttk
from funcoes import Funções
from tkinter import messagebox
from tkinter import font

class Application(tk.Tk, Funções):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.title("4 FITNESS")
        self.geometry("800x600")
        self.current_page = 0
        self.menu_inicial()

# Janelas

    def menu_inicial(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.configure(bg="#313131")
        
        label_menu = tk.Label(self, text="4 Fitness", fg="white", bg="#313131", font=("Arial", 24))
        label_menu.pack(pady=50)

        btn_login = tk.Button(self,text="Login", fg="white", bg="#7fd350", command=self.realizar_login, font=("Arial", 12))
        btn_login.pack(pady=20)

        btn_gerenciador = tk.Button(self, text="Gerenciar Perfis", fg="white", bg="#7fd350", command=self.Exibir_perfis, font=("Arial", 12))
        btn_gerenciador.pack(pady=20)

        btn_Encerrar = tk.Button(self, text="Encerrar Programa", fg="white", bg="#7fd350", command=self.Encerrar_programa, font=("Arial", 12))
        btn_Encerrar.pack(pady=20, padx=5)


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
        frame = tk.Frame(self, bg="#313131", highlightthickness=4, highlightbackground="#7fd350", highlightcolor="#7fd350")
        frame.grid(row=1, column=0, columnspan=2)

        # Título
        titulo = tk.Label(frame, text="Realizar login", fg="white", bg="#313131", font=("Arial", 20))
        titulo.grid(row=0, column=0, columnspan=2, pady=10, padx=20)

        # Nome do usuário
        tk.Label(frame, text="Nome:", fg="white", bg="#313131", font=("Arial", 10)).grid(row=1, column=0, sticky="e", padx=10)
        self.entry_nome = tk.Entry(frame)
        self.entry_nome.grid(row=1, column=1, pady=5, padx=20)

        # Senha
        tk.Label(frame, text="Senha:", fg="white", bg="#313131", font=("Arial", 10)).grid(row=2, column=0, sticky="e", padx=10)
        self.entry_senha = tk.Entry(frame, show="*")
        self.entry_senha.grid(row=2, column=1, pady=5, padx=20)

        # Checkbutton para mostrar senha
        self.check_senha = tk.IntVar()
        check = tk.Checkbutton(frame, text="Mostrar senha", fg="white", bg="#313131", variable=self.check_senha, command=self.Exibir_senha)
        check.grid(row=3, column=0, columnspan=2, pady=5)

        # Botão de validar
        tk.Button(frame, text="Login", fg="white", bg="#7fd350", command=self.validar_login, font=("Arial", 12)).grid(row=4, column=0, columnspan=2, pady=10)

    # Botão de criar conta
        tk.Button(frame, text="Cadastrar-se", fg="white", bg="#7fd350", command=self.cadastrar_cliente, font=("Arial", 12)).grid(row=5, column=0, columnspan=2, pady=10)

        # Botão de voltar
        tk.Button(frame, text="Voltar", fg="white", bg="#7fd350", command=self.menu_inicial, font=("Arial", 12)).grid(row=6, column=0, columnspan=2, pady=10)


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
        frame = tk.Frame(self,bg='#313131',highlightthickness=4,highlightbackground='#7fd350',highlightcolor='#7fd350')
        frame.grid(row=1, column=0, columnspan=2)

        # Título
        title = tk.Label(frame, text="Cadastrar Cliente", fg="white", bg="#313131", font=('Arial', 20))
        title.grid(row=0, column=0, columnspan=5, pady=10)

        # Nome
        tk.Label(frame, text="Nome:", fg="white", bg="#313131", font=("Arial", 10)).grid(row=1, column=0, sticky="e", padx=10)
        self.entry_nome = tk.Entry(frame)
        self.entry_nome.grid(row=1, column=1, pady=5)

        # Email
        tk.Label(frame, text="Email:", fg="white", bg="#313131", font=("Arial", 10)).grid(row=2, column=0, sticky="e", padx=10)
        self.entry_email = tk.Entry(frame)
        self.entry_email.grid(row=2, column=1, pady=5)

        # Senha
        tk.Label(frame, text="Senha:", fg="white", bg="#313131", font=("Arial", 10)).grid(row=3, column=0, sticky="e", padx=10)
        self.entry_senha = tk.Entry(frame, show="*")
        self.entry_senha.grid(row=3, column=1, pady=5)

        # Checkbutton para mostrar senha
        self.check_senha = tk.IntVar()
        check_button = tk.Checkbutton(frame, text="Exibir Senha", fg="white", bg="#313131", variable=self.check_senha, command=self.Exibir_senha)
        check_button.grid(row=4, column=1, sticky="w", padx=10)  # Posicionando à esquerda

        # Telefone
        tk.Label(frame, text="Telefone:", fg="white", bg="#313131", font=("Arial", 10)).grid(row=5, column=0, sticky="e", padx=10)
        self.entry_telefone = tk.Entry(frame)
        self.entry_telefone.grid(row=5, column=1, pady=5)

        # Endereço
        tk.Label(frame, text="Endereço:", fg="white", bg="#313131", font=("Arial", 10)).grid(row=6, column=0, sticky="e", padx=10)
        self.entry_endereco = tk.Entry(frame)
        self.entry_endereco.grid(row=6, column=1, pady=5)

        #CPF 
        tk.Label(frame, text="CPF", fg="white", bg="#313131", font=("Arial",10)).grid(row=7, column=0, sticky="e",padx=10)
        self.entry_cpf = tk.Entry(frame)
        self.entry_cpf.grid(row=7,column=1, pady=5)
        
        #Data de nascimento 
        tk.Label(frame, text="Data de nascimento", fg="white", bg="#313131", font=("Arial",10)).grid(row=8,column=0, sticky="e", padx=10)
        
        self.entry_dataDeNascimento = tk.Entry(frame)
        self.entry_dataDeNascimento.grid(row=8,column=1,pady=5)

        btn_abrir_calendario = ttk.Button(frame, text="Escolher data", command=self.abrir_calendario)
        btn_abrir_calendario.grid(row=8, column=2,padx=10)

        # Botão Cadastrar-se
        tk.Button(frame, text="Cadastrar-se",fg='white',bg='#7fd350',command=self.validar_dados, font=("Arial", 12)).grid(row=9, column=1, pady=10)
        

        # Botão Voltar
        tk.Button(frame, text="Voltar",fg='white',bg='#7fd350', command=self.realizar_login, font=("Arial", 10)).grid(row=10, column=1,pady=10)


    def escolher_plano(self):
        for widget in self.winfo_children():
            widget.destroy()    
   
  
    def Home(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Estilização da Janela
        self.configure(bg="#313131")

        # Frame superior com o título e plano
        frame_superior = tk.Frame(self, bg="#7fd350")
        frame_superior.pack(side="top", fill="x", pady=10)

        title = tk.Label(frame_superior, text="4 FITNESS", fg="white", bg="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        log_out = tk.Button(frame_superior, text="Log Out", fg="white", bg="black", command=self.realizar_login)
        log_out.pack(side="right", padx=10)

        plano_label = tk.Label(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", fg="white", bg="#7fd350", font=("Arial", 12, ))
        plano_label.pack(side="right", padx=20)

        # Frame central para os botões
        central_frame = tk.Frame(self, bg="#313131")
        central_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Centralizando o frame

        # Colocando os botões lado a lado usando grid
        btn_perfil = tk.Button(central_frame, text="Perfil", command=self.Perfil_usuario, font=("Arial", 12, "bold"), width=15, height=5)
        btn_perfil.grid(row=0, column=0, padx=20, pady=20)

        btn_treinos = tk.Button(central_frame, text="Treinos", command=self.Treinos, font=("Arial", 12, "bold"), width=15, height=5)
        btn_treinos.grid(row=0, column=1, padx=20, pady=20)

        btn_ajustes = tk.Button(central_frame, text="Ajustes", command=self.Ajustes, font=("Arial", 12, "bold"), width=15, height=5)
        btn_ajustes.grid(row=0, column=2, padx=20, pady=20)


        # Configurar expansão de colunas
        central_frame.grid_columnconfigure(0, weight=1)
        central_frame.grid_columnconfigure(1, weight=1)
        central_frame.grid_columnconfigure(2, weight=1)


    def Treinos(self):
        for widget in self.winfo_children():
            widget.destroy()

            
        self.configure(bg="#313131")

        # Frame superior com o título e plano
        frame_superior = tk.Frame(self, bg="#7fd350")
        frame_superior.pack(side="top", fill="x", pady=10)

        title = tk.Label(frame_superior, text="4 FITNESS", fg="white", bg="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        plano_label = tk.Label(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", fg="white", bg="#7fd350", font=("Arial", 12, ))
        plano_label.pack(side="right", padx=20)

        home_button = tk.Button(frame_superior, text="🏠", fg="white", bg="black", command=self.Home)
        home_button.pack(side="right", padx=10)

        # Frame central para os botões
        central_frame = tk.Frame(self, bg="#313131")
        central_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)# Centralizando o frame

        # Colocando os botões lado a lado usando grid

        btn_treinos = tk.Button(central_frame, text="Superiores", command=self.Superiores, font=("Arial", 12, "bold"), width=15, height=5)
        btn_treinos.grid(row=0, column=0, padx=20, pady=20)

        btn_ajustes = tk.Button(central_frame, text="Inferiores", command=self.Inferiores, font=("Arial", 12, "bold"), width=15, height=5)
        btn_ajustes.grid(row=0, column=1, padx=20, pady=20)

        btn_voltar = tk.Button(central_frame, text="Voltar", command=self.Home, font=("Arial", 12, "bold"))
        btn_voltar.grid(row=1, column=0, columnspan=2, padx=60, pady=20)


        # Configurar expansão de colunas
        central_frame.grid_columnconfigure(0, weight=1)
        central_frame.grid_columnconfigure(1, weight=1)
        central_frame.grid_columnconfigure(2, weight=1)

        tk.Button(self, text="Voltar", font=("Arial", 10), command=self.Home).grid(row=2, column=0, columnspan=2, pady=10, sticky="s")


    def Superiores(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.configure(bg="#313131")

        # Frame superior com o título e plano
        frame_superior = tk.Frame(self, bg="#7fd350")
        frame_superior.pack(side="top", fill="x", pady=10)

        title = tk.Label(frame_superior, text="4 FITNESS", fg="white", bg="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        plano_label = tk.Label(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", fg="white", bg="#7fd350", font=("Arial", 12))
        plano_label.pack(side="right", padx=20)

        home_button = tk.Button(frame_superior, text="🏠", fg="white", bg="black", command=self.Home)
        home_button.pack(side="right", padx=10)

        # Frame central para os botões
        central_frame = tk.Frame(self, bg="#313131")
        central_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Centralizando o frame

        # Colocando os botões lado a lado usando grid com borda colorida
        
        # Frame para o botão Perna com borda colorida
        peito_frame = tk.Frame(central_frame, highlightbackground="#7fd350", highlightthickness=4)
        peito_frame.grid(row=0, column=0, padx=20, pady=20)
        
        btn_Peito = tk.Button(peito_frame, text="Peito", command=self.Peito, bd=0, font=("Arial", 12, "bold"), width=15, height=5)
        btn_Peito.pack()

        # Frame para o botão Quadriceps com borda colorida
        Costas_frame = tk.Frame(central_frame, highlightbackground="#7fd350", highlightthickness=4)
        Costas_frame.grid(row=0, column=1, padx=20, pady=20)
        
        btn_Costas = tk.Button(Costas_frame, text="Costas", command=self.Costas, bd=0, font=("Arial", 12, "bold"), width=15, height=5)
        btn_Costas.pack()

        # Botão Voltar
        btn_voltar = tk.Button(central_frame, text="Voltar", command=self.Treinos, font=("Arial", 12, "bold"))
        btn_voltar.grid(row=1, column=0, columnspan=2, padx=60, pady=20)


    def Inferiores(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.configure(bg="#313131")

        # Frame superior com o título e plano
        frame_superior = tk.Frame(self, bg="#7fd350")
        frame_superior.pack(side="top", fill="x", pady=10)

        title = tk.Label(frame_superior, text="4 FITNESS", fg="white", bg="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        plano_label = tk.Label(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", fg="white", bg="#7fd350", font=("Arial", 12))
        plano_label.pack(side="right", padx=20)

        home_button = tk.Button(frame_superior, text="🏠", fg="white", bg="black", command=self.Home)
        home_button.pack(side="right", padx=10)

        # Frame central para os botões
        central_frame = tk.Frame(self, bg="#313131")
        central_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Centralizando o frame

        # Colocando os botões lado a lado usando grid com borda colorida
        
        # Frame para o botão Perna com borda colorida
        perna_frame = tk.Frame(central_frame, highlightbackground="#7fd350", highlightthickness=4)
        perna_frame.grid(row=0, column=0, padx=20, pady=20)
        
        btn_Perna = tk.Button(perna_frame, text="Perna", command=self.Perna, bd=0, font=("Arial", 12, "bold"), width=15, height=5)
        btn_Perna.pack()

        # Frame para o botão Quadriceps com borda colorida
        quadriceps_frame = tk.Frame(central_frame, highlightbackground="#7fd350", highlightthickness=4)
        quadriceps_frame.grid(row=0, column=1, padx=20, pady=20)
        
        btn_Quadriceps = tk.Button(quadriceps_frame, text="Quadriceps", command=self.Quadriceps, bd=0, font=("Arial", 12, "bold"), width=15, height=5)
        btn_Quadriceps.pack()

        # Botão Voltar
        btn_voltar = tk.Button(central_frame, text="Voltar", command=self.Treinos, font=("Arial", 12, "bold"))
        btn_voltar.grid(row=1, column=0, columnspan=2, padx=60, pady=20)


    def Peito(self):
        # Dicionário de músculos e exercícios
        treinos = {
            "Peito": [
                {"nome": "Supino reto com barra", "reps": "3x15reps"},
                {"nome": "Crucifixo inclinado com halteres", "reps": "3x15reps"},
                {"nome": "Crucifixo no crossover polia alta", "reps": "3x15reps"},
            ],
            "Ombros": [
                {"nome": "Elevação lateral com halteres", "reps": "3x12reps"},
                {"nome": "Desenvolvimento com halteres", "reps": "3x12reps"},
                {"nome": "Remada alta com barra", "reps": "3x12reps"},
            ],
            "Tríceps": [
                {"nome": "Tríceps testa", "reps": "3x15reps"},
                {"nome": "Mergulho em bancos", "reps": "3x12reps"},
                {"nome": "Puxada de tríceps na polia", "reps": "3x15reps"},
            ]
        }

        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()

        # Título
        tk.Label(self, text="Treinos", font=("Arial", 24), bg="#313131", fg="white").pack(pady=10)

        # Frame principal para treinos em pirâmide
        main_frame = tk.Frame(self, bg="#282828")
        main_frame.pack(pady=20, padx=20)

        # Exibindo os três grupos musculares lado a lado
        for i, grupo in enumerate(treinos.keys()):
            col_frame = tk.Frame(main_frame, bg="#282828")
            col_frame.grid(row=0, column=i, padx=20)  # Colocando cada grupo em uma coluna separada

            # Título do grupo muscular
            tk.Label(col_frame, text=grupo, font=("Arial", 14, "bold"), bg="#282828", fg="white").pack(pady=10)

            # Exibindo os exercícios de cada grupo muscular
            for exercicio in treinos[grupo]:
                tk.Label(col_frame, text=exercicio["nome"], font=("Arial", 12), bg="#282828", fg="white").pack(pady=5)
                tk.Label(col_frame, text=exercicio["reps"], font=("Arial", 12, "bold"), bg="#282828", fg="white").pack(pady=5)

        # Botão Voltar
        tk.Button(self, text="Voltar", font=("Arial", 10), command=self.Superiores).pack(pady=20)


    def Costas(self):
        # Dicionário de músculos e exercícios
        treinos = {
            "Costas": [
                {"nome": "Puxada alta", "reps": "3x12reps"},
                {"nome": "Remada curvada", "reps": "3x12reps"},
                {"nome": "Levantamento terra", "reps": "3x10reps"},
            ],
            "Bíceps": [
                {"nome": "Rosca direta com barra", "reps": "3x12reps"},
                {"nome": "Rosca martelo com halteres", "reps": "3x12reps"},
                {"nome": "Rosca concentrada", "reps": "3x15reps"},
            ]
        }

        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()

        # Título
        tk.Label(self, text="Treinos", font=("Arial", 24), bg="#313131", fg="white").pack(pady=10)

        # Frame principal para treinos em pirâmide
        main_frame = tk.Frame(self, bg="#282828")
        main_frame.pack(pady=20, padx=20)

        # Exibindo os dois grupos musculares lado a lado
        for i, grupo in enumerate(treinos.keys()):
            col_frame = tk.Frame(main_frame, bg="#282828")
            col_frame.grid(row=0, column=i, padx=20)  # Colocando cada grupo em uma coluna separada

            # Título do grupo muscular
            tk.Label(col_frame, text=grupo, font=("Arial", 14, "bold"), bg="#282828", fg="white").pack(pady=10)

            # Exibindo os exercícios de cada grupo muscular
            for exercicio in treinos[grupo]:
                tk.Label(col_frame, text=exercicio["nome"], font=("Arial", 12), bg="#282828", fg="white").pack(pady=5)
                tk.Label(col_frame, text=exercicio["reps"], font=("Arial", 12, "bold"), bg="#282828", fg="white").pack(pady=5)

            # Adicionar separador entre as colunas, exceto após o último treino
            if i < len(treinos) - 1:
                sep = ttk.Separator(main_frame, orient="vertical")
                sep.grid(row=0, column=i+1, sticky="ns", padx=10)  # Separador vertical

        # Botão Voltar
        tk.Button(self, text="Voltar", font=("Arial", 10), command=self.Superiores).pack(pady=20)


    def Quadriceps(self):
        # Dicionário de exercícios para Quadríceps
        treinos = {
            "Quadríceps": [
                {"nome": "Agachamento livre", "reps": "3x12reps"},
                {"nome": "Leg press 45°", "reps": "3x12reps"},
                {"nome": "Extensão de pernas", "reps": "3x15reps"},
            ]
        }

        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()

        # Título
        tk.Label(self, text="Treinos de Quadríceps", font=("Arial", 24), bg="#313131", fg="white").pack(pady=10)

        # Frame principal para treinos em pirâmide
        main_frame = tk.Frame(self, bg="#282828")
        main_frame.pack(pady=20, padx=20)

        # Exibindo o grupo muscular
        col_frame = tk.Frame(main_frame, bg="#282828")
        col_frame.pack(pady=20)

        # Título do grupo muscular
        tk.Label(col_frame, text="Quadríceps", font=("Arial", 14, "bold"), bg="#282828", fg="white").pack(pady=10)

        # Exibindo os exercícios de Quadríceps
        for exercicio in treinos["Quadríceps"]:
            tk.Label(col_frame, text=exercicio["nome"], font=("Arial", 12), bg="#282828", fg="white").pack(pady=5)
            tk.Label(col_frame, text=exercicio["reps"], font=("Arial", 12, "bold"), bg="#282828", fg="white").pack(pady=5)

        # Botão Voltar
        tk.Button(self, text="Voltar", font=("Arial", 10), command=self.Inferiores).pack(pady=20)


    def Perna(self):
        # Dicionário de exercícios para Perna
        treinos = {
            "Perna": [
                {"nome": "Stiff", "reps": "3x12reps"},
                {"nome": "Afundo com halteres", "reps": "3x12reps"},
                {"nome": "Flexão de pernas na máquina", "reps": "3x15reps"},
            ]
        }

        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()

        # Título
        tk.Label(self, text="Treinos de Perna", font=("Arial", 24), bg="#313131", fg="white").pack(pady=10)

        # Frame principal para treinos em pirâmide
        main_frame = tk.Frame(self, bg="#282828")
        main_frame.pack(pady=20, padx=20)

        # Exibindo o grupo muscular
        col_frame = tk.Frame(main_frame, bg="#282828")
        col_frame.pack(pady=20)

        # Título do grupo muscular
        tk.Label(col_frame, text="Perna", font=("Arial", 14, "bold"), bg="#282828", fg="white").pack(pady=10)

        # Exibindo os exercícios de Perna
        for exercicio in treinos["Perna"]:
            tk.Label(col_frame, text=exercicio["nome"], font=("Arial", 12), bg="#282828", fg="white").pack(pady=5)
            tk.Label(col_frame, text=exercicio["reps"], font=("Arial", 12, "bold"), bg="#282828", fg="white").pack(pady=5)

        # Botão Voltar
        tk.Button(self, text="Voltar", font=("Arial", 10), command=self.Inferiores).pack(pady=20)


    def Exibir_perfis(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        title = tk.Label(self, text="Perfis dos Clientes", fg="white", bg="#313131", font=("Arial", 20))
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

        btn_deletar = tk.Button(self, text="Deletar Perfil", fg="white", bg="#7fd350", command=self.deletar_perfil)
        btn_deletar.pack(pady=10)

        btn_voltar = tk.Button(self, text="Voltar", fg="white", bg="#7fd350", command=self.menu_inicial, font=("Arial", 10))
        btn_voltar.pack(pady=10)

    def Ajustes(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        self.grid_rowconfigure(6, weight=1)  # Espaço na parte inferior

        # Frame para centralizar o conteúdo
        frame = tk.Frame(self,bg='#313131',highlightthickness=4,highlightbackground='#7fd350',highlightcolor='#7fd350')
        frame.grid(row=1, column=0, columnspan=2)

        # Título
        title = tk.Label(frame, text="Ajustes", fg="white", bg="#313131", font=('Arial', 20))
        title.grid(row=0, column=0, columnspan=5, pady=10)


        #Label Notificações - 01
        notificacoes = tk.Label(frame, text="Notificações : ", fg="white", bg="#313131", font=('Arial', 14))
        notificacoes.grid(row=1, column=0, pady=10, padx=10)

        Notificacoes = ["Exibir", "Não Exibir"]

        notificacoes_var = tk.StringVar()
        notificacoes_var.set(Notificacoes[0])  

        optionmenu_notificacoes = tk.OptionMenu(frame, notificacoes_var, * Notificacoes)
        optionmenu_notificacoes.grid(row=1, column=1, padx=10)


        # Label Idioma - 02
        Idioma = tk.Label(frame, text="Idioma : ", fg="white", bg="#313131", font=('Arial', 14))
        Idioma.grid(row=2, column=0, pady=10, padx=10)

        Idiomas = ["Português Brasil"]

        idiomas_var = tk.StringVar()
        idiomas_var.set(Idiomas[0])  

        optionmenu_idiomas = tk.OptionMenu(frame, idiomas_var, * Idiomas)
        optionmenu_idiomas.grid(row=2, column=1, padx=10)


        # Label Unidade de Medida - 03
        und_medida = tk.Label(frame, text="Unidade de Medida : ", fg="white", bg="#313131", font=('Arial', 14))
        und_medida.grid(row=3, column=0, pady=10, padx=10)


        Unidades_med = ["Kg", "LB"]

        Unidades_med_var = tk.StringVar()
        Unidades_med_var.set(Unidades_med[0])  

        optionmenu_cidades = tk.OptionMenu(frame, Unidades_med_var, * Unidades_med)
        optionmenu_cidades.grid(row=3, column=1, padx=10)


        # Label Frequencia - 04
        Frequencia = tk.Label(frame, text="Frquencia de Treinos :", fg="white", bg="#313131", font=('Arial', 14))
        Frequencia.grid(row=4, column=0, pady=10, padx=10)


        Frequencia = ["5 Dias na semana", "3 Dias na semana", "4 Dias na semana"]

        Frequencia_var = tk.StringVar()
        Frequencia_var.set(Frequencia[0])  

        optionmenu_frequencia = tk.OptionMenu(frame, Frequencia_var, * Frequencia)
        optionmenu_frequencia.grid(row=4, column=1, padx=10)

        # Label Meta - 5
        Meta = tk.Label(frame, text="Meta :", fg="white", bg="#313131", font=('Arial', 14))
        Meta.grid(row=5, column=0, pady=10, padx=10)


        Meta = ["Ganho de Massa", "Hipertrofia", "Perca de Peso"]

        Meta_var = tk.StringVar()
        Meta_var.set(Meta[0])  

        optionmenu_meta = tk.OptionMenu(frame, Meta_var, * Meta)
        optionmenu_meta.grid(row=5, column=1, padx=10)

        # Botão Cadastrar-se
        tk.Button(frame, text="Salvar Alterações",fg='white', bg='#7fd350',command=self.Home, font=("Arial", 12)).grid(row=6, column=0, columnspan=5, pady=10, padx=20)
        
        # Botão Voltar
        tk.Button(frame, text="Voltar",fg='white',bg='#7fd350', command=self.Home, font=("Arial", 10)).grid(row=7, column=0, columnspan=5, pady=10)


    def Perfil_usuario(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.puxar_informações()
        
        # Configurações da janela para centralização
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        self.grid_rowconfigure(6, weight=1)  # Espaço na parte inferior

        # Criando o frame verde
        frame_verde = tk.Frame(self, bg="#313131", padx=20, pady=20, highlightthickness=4, highlightcolor="green", highlightbackground="green")
        frame_verde.grid(row=1, column=0, columnspan=2)

        # Criando a fonte Nunito
        nunito_font = font.Font(family="Nunito", size=10)
        titulo_font = font.Font(family="Nunito", size=14, weight="bold")
        botao_font = font.Font(family="Nunito", size=10, weight="bold")

        # Label para o título
        titulo_label = tk.Label(frame_verde, text="Editar Informações", bg="#313131", fg="White", font=titulo_font)
        titulo_label.grid(row=0, column=1, pady=10)

        # Labels e entradas
        self.entry_novo_nome = tk.Entry(frame_verde, bg="#ffffff", fg="Black", font=nunito_font)
        label_nome = tk.Label(frame_verde, text="Nome:", bg="#313131", fg="White", font=nunito_font)
        label_nome.grid(row=1, column=0, pady=2, sticky='e')
        self.entry_novo_nome.grid(row=1, column=1, pady=2)

        self.entry_novo_nome.insert(0, f'{self.get_informacao(1).lower().capitalize()}')  # Adiciona o placeholder

        self.entry_nova_dataDeNascimento = tk.Entry(frame_verde, bg="#ffffff", fg="Black", font=nunito_font)
        label_datanasc = tk.Label(frame_verde, text="Data de nascimento:", bg="#313131", fg="White", font=nunito_font)
        label_datanasc.grid(row=2, column=0, pady=2, sticky='e')
        self.entry_nova_dataDeNascimento.grid(row=2, column=1, pady=2)

        self.entry_nova_dataDeNascimento.insert(0, f'{self.get_informacao(7)}')  # Adiciona o placeholder

        self.btn_calendario = tk.Button(frame_verde, text="Escolher data", command=self.abrir_calendario)
        self.btn_calendario.grid(row=2, column=2, padx=4)


        self.entry_novo_endereco = tk.Entry(frame_verde, bg="#ffffff", fg="Black", font=nunito_font)
        label_endereco = tk.Label(frame_verde, text="Endereço:", bg="#313131", fg="White", font=nunito_font)
        label_endereco.grid(row=3, column=0, pady=2, sticky='e')
        self.entry_novo_endereco.grid(row=3, column=1, pady=2)

        self.entry_novo_endereco.insert(0, f'{self.get_informacao(5)}')  # Adiciona o placeholder

        self.entry_novo_telefone = tk.Entry(frame_verde, bg="#ffffff", fg="Black", font=nunito_font)
        label_telefone = tk.Label(frame_verde, text="Telefone:", bg="#313131", fg="White", font=nunito_font)
        label_telefone.grid(row=4, column=0, pady=2, sticky='e')
        self.entry_novo_telefone.grid(row=4, column=1, pady=2)

        self.entry_novo_telefone.insert(0, f'{self.get_informacao(4)}')  # Adiciona o placeholder

        self.entry_novo_email = tk.Entry(frame_verde, bg="#ffffff", fg="Black", font=nunito_font)
        label_email = tk.Label(frame_verde, text="E-mail:", bg="#313131", fg="White", font=nunito_font)
        label_email.grid(row=5, column=0, pady=2, sticky='e')
        self.entry_novo_email.grid(row=5, column=1, pady=2)

        self.entry_novo_email.insert(0, f'{self.get_informacao(2)}')  # Adiciona o placeholder

        self.btn_voltar = tk.Button(frame_verde, text="Cancelar", command=self.Home, bg="#000000", fg="#FF0000")
        self.btn_voltar.grid(row=6, column=1, pady=10)

        botao_salvar = tk.Button(frame_verde, text="Salvar alterações", bg="#000000", fg="#00ff00", font=botao_font, command=self.salvar_alterações)
        botao_salvar.grid(row=7, column=1, pady=10)