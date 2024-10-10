import tkinter as tk
from sqlalchemy import *
from sqlalchemy.exc import SQLAlchemyError
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
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
        
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill='both', expand=True)

        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_rowconfigure(0, weight=0) 

        image_path = "Projeto Academia\\img\\Logo.png"
        self.logo_image = ctk.CTkImage(light_image=Image.open(image_path), size=(150, 150))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image = ctk.CTkLabel(background_frame, image=self.logo_image, text="")
        self.label_image.grid(row=1, column=0, pady=(60, 0))

        border_frame = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=10)
        border_frame.grid(row=2, column=0, padx=20, pady=20)

        # Frame para centralizar o conteúdo
        frame = ctk.CTkFrame(border_frame, fg_color="#313131", corner_radius=10)
        frame.grid(row=0, column=0, padx=10, pady=10)
        
        #Titulo
        titulo = ctk.CTkLabel(frame, text="4 FITNESS", text_color="white", font=("Arial", 40))
        titulo.grid(row=0, column=0, columnspan=2, pady=20)

        #Botoes
        ctk.CTkButton(frame, text="Login", font=("Arial", 18), width=160, command=self.realizar_login).grid(row=1, column=0, columnspan=2, pady=30, padx=60)

        ctk.CTkButton(frame, text="Gerenciar Perfis", font=("Arial", 18), width=160, command=self.Exibir_perfis).grid(row=2, column=0, columnspan=2, pady=30, padx=60)
        
        ctk.CTkButton(frame, text="Encerrar Programa", font=("Arial", 18), width=160, command=self.Encerrar_programa).grid(row=3, column=0, columnspan=2, pady=30, padx=60)


    def realizar_login(self):
        # Remove widgets existentes
        for widget in self.winfo_children():
            widget.destroy()

        # Criação do frame de fundo
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill='both', expand=True)
        
        # Configuração de colunas e linhas para centralizar
        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_rowconfigure(0, weight=0)  # Para centralizar verticalmente
        # Imagem
        image_path = "Projeto Academia\\img\\Logo.png"
        self.logo_image = ctk.CTkImage(light_image=Image.open(image_path), size=(150, 150))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image = ctk.CTkLabel(background_frame, image=self.logo_image, text="")
        self.label_image.grid(row=0, column=0, pady=0)

        # Frame para a borda
        border_frame = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=10)
        border_frame.grid(row=1, column=0, padx=20, pady=20)

        # Frame para centralizar o conteúdo
        frame = ctk.CTkFrame(border_frame, fg_color="#313131", corner_radius=10)
        frame.grid(row=0, column=0, padx=10, pady=10)

        # Título
        titulo = ctk.CTkLabel(frame, text="Realizar login", text_color="white", font=("Arial", 20))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Nome do usuário
        ctk.CTkLabel(frame, text="Nome:", text_color="white", font=("Arial", 14)).grid(row=1, column=0, sticky="e", padx=10)
        self.entry_nome = ctk.CTkEntry(frame, placeholder_text="Nome")
        self.entry_nome.grid(row=1, column=1, pady=5, padx=20)

        # Senha
        ctk.CTkLabel(frame, text="Senha:", text_color="white", font=("Arial", 14)).grid(row=2, column=0, sticky="e", padx=10)
        self.entry_senha = ctk.CTkEntry(frame, show="*", placeholder_text="Senha")
        self.entry_senha.grid(row=2, column=1, pady=5, padx=20)

        # Checkbutton para mostrar senha
        self.check_senha = ctk.IntVar()
        check = ctk.CTkCheckBox(frame, text="Mostrar senha", text_color="white", variable=self.check_senha, command=self.Exibir_senha)
        check.grid(row=3, column=0, columnspan=2, pady=5)

        # Botão de validar
        ctk.CTkButton(frame, text="Login", font=("Arial", 18), width=160, command=self.validar_login).grid(row=4, column=0, columnspan=2, pady=10)

        # Botão de criar conta
        ctk.CTkButton(frame, text="Cadastrar-se", font=("Arial", 18), width=160, command=self.cadastrar_cliente).grid(row=5, column=0, columnspan=2, pady=10)

        # Botão de voltar
        ctk.CTkButton(frame, text="Voltar", font=("Arial", 18), width=160, command=self.menu_inicial).grid(row=6, column=0, columnspan=2, pady=10)


    def cadastrar_cliente(self):
        # Remove widgets existentes
        for widget in self.winfo_children():
            widget.destroy()

        backgorund_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        backgorund_frame.pack(fill="both", expand=True)

        # Configurações da janela para centralização
        backgorund_frame.grid_columnconfigure(0, weight=1)
        backgorund_frame.grid_columnconfigure(1, weight=1)
        backgorund_frame.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        backgorund_frame.grid_rowconfigure(6, weight=1)  # Espaço na parte inferior
        
        border_frame = ctk.CTkFrame(backgorund_frame,fg_color="#7fd350",corner_radius=10)
        border_frame.grid(row=0,column=0,columnspan=2,padx=20,pady=20)
        
        
        # Frame para centralizar o conteúdo
        frame = ctk.CTkFrame(border_frame, fg_color="#313131",corner_radius=10)
        frame.grid(padx=10,pady=10)

        # Título
        title = ctk.CTkLabel(frame,text="Realizar cadastro", text_color="white",font=("Arial", 20))
        title.grid(row=0,column=1,pady=10)

        # Nome
        ctk.CTkLabel(frame, text="Nome:",text_color="white", font=("Arial", 14)).grid(row=1, column=0, sticky="e", padx=10)
        self.entry_nome = ctk.CTkEntry(frame)
        self.entry_nome.grid(row=1, column=1, pady=5)

        # Email
        ctk.CTkLabel(frame, text="Email:", text_color="white", font=("Arial", 14)).grid(row=2, column=0, sticky="e", padx=10)
        self.entry_email = ctk.CTkEntry(frame)
        self.entry_email.grid(row=2, column=1, pady=5)

        # Senha
        ctk.CTkLabel(frame, text="Senha:", text_color="white", font=("Arial", 14)).grid(row=3, column=0, sticky="e", padx=10)
        self.entry_senha = ctk.CTkEntry(frame, show="*")
        self.entry_senha.grid(row=3, column=1, pady=5)

        # Checkbutton para mostrar senha
        self.check_senha = ctk.IntVar()
        check_button = ctk.CTkCheckBox(frame, text="Mostrar senha", text_color="white", variable=self.check_senha, command=self.Exibir_senha)
        check_button.grid(row=4, column=1, sticky="w", padx=10)  # Posicionando à esquerda

        # Telefone
        ctk.CTkLabel(frame, text="Telefone:", text_color="white", font=("Arial", 14)).grid(row=5, column=0, sticky="e", padx=10)
        self.entry_telefone = ctk.CTkEntry(frame)
        self.entry_telefone.grid(row=5, column=1, pady=5)

        # Endereço
        ctk.CTkLabel(frame, text="Endereço:", text_color="white", font=("Arial", 14)).grid(row=6, column=0, sticky="e", padx=10)
        self.entry_endereco = ctk.CTkEntry(frame)
        self.entry_endereco.grid(row=6, column=1, pady=5)

        #CPF 
        ctk.CTkLabel(frame, text="CPF", text_color="white", font=("Arial", 14)).grid(row=7, column=0, sticky="e",padx=10)
        self.entry_cpf = ctk.CTkEntry(frame)
        self.entry_cpf.grid(row=7,column=1, pady=5)
        
        #Data de nascimento 
        ctk.CTkLabel(frame, text="Data de nascimento", text_color="white", font=("Arial", 14)).grid(row=8,column=0, sticky="e", padx=10)
        
        self.entry_dataDeNascimento = ctk.CTkEntry(frame)
        self.entry_dataDeNascimento.grid(row=8,column=1,pady=5)

        btn_abrir_calendario = ttk.Button(frame, text="Escolher data", command=self.abrir_calendario)
        btn_abrir_calendario.grid(row=8, column=2,padx=10)

        # Botão Cadastrar-se
        ctk.CTkButton(frame,text="Cadastrar-se",command=self.validar_dados).grid(row=9,column=1,pady=10)

        # Botão Voltar
        ctk.CTkButton(frame, text="Voltar",command=self.realizar_login).grid(row=10, column=1,pady=10)

    def Home(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="4 FITNESS", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        log_out = ctk.CTkButton(frame_superior, text=" ⬅ Log Out", text_color="white", fg_color='#ED1B24', hover_color='#242424', font=("Arial", 14, 'bold'), height=20, command=self.realizar_login)
        log_out.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame

        #Imagem Perfil
        image_path = "Projeto Academia\\img\\Home\\Perfil.png"
        self.logo_image_perfil = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_perfil = ctk.CTkLabel(central_frame, image=self.logo_image_perfil, text="")
        self.label_image_perfil.grid(row=0, column=0, pady=0)

        # Colocando os botões lado a lado usando grid (CustomTkinter)
        btn_perfil = ctk.CTkButton(central_frame, text="Perfil", command=self.Perfil_usuario, font=("Arial", 18, "bold"), width=150, height=50)
        btn_perfil.grid(row=0, column=0, pady=(250, 00))

        image_path = "Projeto Academia\\img\\Home\\Treinos.png"
        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=1, pady=0)

        btn_treinos = ctk.CTkButton(central_frame, text="Treinos", command=self.Treinos, font=("Arial", 18, "bold"), width=150, height=50)
        btn_treinos.grid(row=0, column=1, pady=(250, 00))

        image_path = "Projeto Academia\\img\\Home\\Ajustes.png"
        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=2, pady=0)

        btn_ajustes = ctk.CTkButton(central_frame, text="Ajustes", command=self.Ajustes, font=("Arial", 18, "bold"), width=150, height=50)
        btn_ajustes.grid(row=0, column=2, pady=(250, 00))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


    def Treinos(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="4 FITNESS", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        home_button = ctk.CTkButton(frame_superior, text="🏠 Home", font=("Arial", 14, 'bold'), text_color="white", height=20 ,command=self.Home)
        home_button.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame

        image_path = "Projeto Academia\\img\\Treinos\\Puxador.png"
        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_superiores = ctk.CTkButton(central_frame, text="Superiores", command=self.Superiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_superiores.grid(row=0, column=0, pady=(250, 00))

        image_path = "Projeto Academia\\img\\Treinos\\Leg-press.png"
        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_inferiores = ctk.CTkButton(central_frame, text="Inferiores", command=self.Inferiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_inferiores.grid(row=0, column=1, pady=(250, 00))

        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", command=self.Home, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=(20, 0))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


    def Superiores(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="4 FITNESS", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        home_button = ctk.CTkButton(frame_superior, text="🏠 Home", font=("Arial", 14, 'bold'), text_color="white", height=20 ,command=self.Home)
        home_button.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame

        image_path = "Projeto Academia\\img\\Treinos\\Superiores\\Peito.png"
        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_Peito = ctk.CTkButton(central_frame, text="Peito", command=self.Peito, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Peito.grid(row=0, column=0, pady=(250, 00))

        image_path = "Projeto Academia\\img\\Treinos\\Superiores\\Costas.png"
        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_Costas = ctk.CTkButton(central_frame, text="Costas", command=self.Costas, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Costas.grid(row=0, column=1, pady=(250, 00))

        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", command=self.Treinos, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=(20, 0))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


    def Inferiores(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="4 FITNESS", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        home_button = ctk.CTkButton(frame_superior, text="🏠 Home", font=("Arial", 14, 'bold'), text_color="white", height=20 ,command=self.Home)
        home_button.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame

        image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Perna.png"
        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_Perna = ctk.CTkButton(central_frame, text="Perna", command=self.Perna, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Perna.grid(row=0, column=0, pady=(250, 00))

        image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps.png"
        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_quadriceps = ctk.CTkButton(central_frame, text="Quadriceps", command=self.Quadriceps, font=("Arial", 18, "bold"), width=150, height=50)
        btn_quadriceps.grid(row=0, column=1, pady=(250, 00))

        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", command=self.Home, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=(20, 0))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


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

        # Criação do frame de fundo
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill='both', expand=True)
        
        # Configuração de colunas e linhas para centralizar
        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_rowconfigure(0, weight=0)  # Para centralizar verticalmente
        
        title = tk.Label(background_frame, text="Perfis dos Clientes", fg="white", bg="#313131", font=("Arial", 20))
        title.pack(pady=20)

        colunas = ("ID", "Nome", "Email", "Telefone", "Endereço") 
        self.tree = ttk.Treeview(background_frame, columns=colunas, show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Endereço", text="Endereço")
        self.tree.pack(pady=0, fill=tk.BOTH, expand=True)
        self.carregar_perfis()

        ctk.CTkButton(background_frame, text="Deletar Perfil", command=self.deletar_perfil).pack(pady=10)
        ctk.CTkButton(background_frame, text="Voltar", command=self.menu_inicial).pack(pady=10)

    def Ajustes(self):
        for widget in self.winfo_children():
            widget.destroy()

        backgorund_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        backgorund_frame.pack(fill="both", expand=True)
   
        backgorund_frame.grid_columnconfigure(0, weight=1)
        backgorund_frame.grid_columnconfigure(1, weight=1)
        backgorund_frame.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        backgorund_frame.grid_rowconfigure(6, weight=1) 
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        self.grid_rowconfigure(6, weight=1)  # Espaço na parte inferior

        # Frame para centralizar o conteúdo
        frame = tk.Frame(backgorund_frame, bg='#313131', highlightthickness=4, highlightbackground='#7fd350', highlightcolor='#7fd350')
        frame.grid(row=1, column=0, columnspan=2)

        # Título
        title = tk.Label(frame, text="Ajustes", fg="white", bg="#313131", font=('Arial', 20))
        title.grid(row=0, column=0, columnspan=5, pady=10)

        # Label Notificações
        notificacoes = ctk.CTkLabel(frame, text="Notificações :", text_color="white", font=('Arial', 14))
        notificacoes.grid(row=1, column=0, pady=10, padx=10)

        notificacoes = ["Exibir", "Não exibir"]

        notificaoes_selecionada = ctk.StringVar(value=notificacoes[0])

        optionmenu_notificacoes = ctk.CTkOptionMenu(frame, variable=notificaoes_selecionada, values=notificacoes)
        optionmenu_notificacoes.grid(row=1, column=1, padx=10)

        # Label Idioma
        Idioma = ctk.CTkLabel(frame, text="Idioma : ", text_color="white", font=('Arial', 14))
        Idioma.grid(row=2, column=0, pady=10, padx=10)

        idiomas = ["Português-BR"]

        idioma_selecionado = ctk.StringVar(value=idiomas[0])

        optionmenu_idioma = ctk.CTkOptionMenu(frame,variable=idioma_selecionado,values=idiomas)
        optionmenu_idioma.grid(row=2, column=1, padx=10)   

        # Label Unidade de Medida
        und_medida = ctk.CTkLabel(frame, text="Unidade de Medida : ", text_color="white", font=('Arial', 14))
        und_medida.grid(row=3, column=0, pady=10, padx=10)

        unidades = ["KG", "LB"]

        unidade_selecionada = ctk.StringVar(value=unidades[0])
        
        optionmenu_unidade = ctk.CTkOptionMenu(frame,variable=unidade_selecionada,values=unidades)
        optionmenu_unidade.grid(row=3, column=1, padx=10)

        # Label Frequência
        frequencia = ctk.CTkLabel(frame, text="Frequência de Treinos :", text_color="white", font=('Arial', 14))
        frequencia.grid(row=4, column=0, pady=10, padx=10)

        Frequencias = ["5 Dias na semana", "3 Dias na semana", "4 Dias na semana"]

        Frequencia_var = ctk.StringVar(value=Frequencias[0])  
        optionmenu_frequencia = ctk.CTkOptionMenu(frame,variable=Frequencia_var, values=Frequencias)
        optionmenu_frequencia.grid(row=4, column=1, padx=10)

        # Label Meta
        meta = ctk.CTkLabel(frame, text="Meta :", text_color="white", font=('Arial', 14))
        meta.grid(row=5, column=0, pady=10, padx=10)

        Metas = ["Ganho de Massa", "Hipertrofia", "Perda de Peso"]

        Meta_var = ctk.StringVar(value=Metas[0])  
        optionmenu_meta = ctk.CTkOptionMenu(frame, variable=Meta_var, values=Metas)
        optionmenu_meta.grid(row=5, column=1, padx=10)

        # Botão Cadastrar-se
        ctk.CTkButton(frame, text="Salvar Alterações",fg_color="#696767", command=self.Home).grid(row=6, column=0, columnspan=5, pady=10, padx=20)
        
        # Botão Voltar
        ctk.CTkButton(frame, text="Voltar", fg_color="#696767",command=self.Home).grid(row=7, column=0, columnspan=5, pady=10)


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