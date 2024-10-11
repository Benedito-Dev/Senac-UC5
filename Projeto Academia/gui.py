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


        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\Logo.png"
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
        ctk.CTkButton(frame, text="Login", font=("Arial", 18), width=160, fg_color="#808080", hover_color="#A9A9A9", command=self.realizar_login).grid(row=1, column=0, columnspan=2, pady=30, padx=60)

        ctk.CTkButton(frame, text="Gerenciar Perfis", font=("Arial", 18), width=160, fg_color="#808080", hover_color="#A9A9A9", command=self.Exibir_perfis).grid(row=2, column=0, columnspan=2, pady=30, padx=60)
        
        ctk.CTkButton(frame, text="Encerrar Programa", font=("Arial", 18), width=160, fg_color="#808080",  hover_color="#A9A9A9", command=self.Encerrar_programa).grid(row=3, column=0, columnspan=2, pady=30, padx=60)


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

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\Logo.png"

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
        ctk.CTkButton(frame, text="Acessar", font=("Arial", 18), width=160, fg_color="#808080", hover_color="#A9A9A9", command=self.validar_login).grid(row=4, column=0, columnspan=2, pady=10)

        # Botão de criar conta
        ctk.CTkButton(frame, text="Cadastrar", font=("Arial", 18), width=160, fg_color="#808080",  hover_color="#A9A9A9", command=self.cadastrar_cliente).grid(row=5, column=0, columnspan=2, pady=10)

        # Botão de voltar
        ctk.CTkButton(frame, text="Voltar", font=("Arial", 18), width=160, fg_color="#808080", hover_color="#A9A9A9", command=self.menu_inicial).grid(row=6, column=0, columnspan=2, pady=10)


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
        ctk.CTkButton(frame,text="Cadastrar-se",fg_color="#609746", hover_color="#A9A9A9", command=self.validar_dados).grid(row=9,column=1,pady=10)

        # Botão Voltar
        ctk.CTkButton(frame, text="Voltar",fg_color="#808080", hover_color="#A9A9A9", command=self.realizar_login).grid(row=10, column=1,pady=10)

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

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\Home\\Perfil.png"

        self.logo_image_perfil = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_perfil = ctk.CTkLabel(central_frame, image=self.logo_image_perfil, text="")
        self.label_image_perfil.grid(row=0, column=0, pady=0)

        # Colocando os botões lado a lado usando grid (CustomTkinter)
        btn_perfil = ctk.CTkButton(central_frame, text="Perfil", fg_color="#808080", hover_color="#A9A9A9", command=self.Perfil_usuario, font=("Arial", 18, "bold"), width=150, height=50)
        btn_perfil.grid(row=0, column=0, pady=(250, 00))


        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\Home\\Treinos.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=1, pady=0)

        btn_treinos = ctk.CTkButton(central_frame, text="Treinos", fg_color="#808080", hover_color="#A9A9A9", command=self.Treinos, font=("Arial", 18, "bold"), width=150, height=50)
        btn_treinos.grid(row=0, column=1, pady=(250, 00))

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\Home\\Ajustes.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=2, pady=0)

        btn_ajustes = ctk.CTkButton(central_frame, text="Ajustes", fg_color="#808080", hover_color="#A9A9A9", command=self.Ajustes, font=("Arial", 18, "bold"), width=150, height=50)
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


        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\Treinos\\Puxador.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_superiores = ctk.CTkButton(central_frame, text="Superiores", fg_color="#808080", hover_color="#A9A9A9", command=self.Superiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_superiores.grid(row=0, column=0, pady=(250, 00))

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\Treinos\\Leg-press.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_inferiores = ctk.CTkButton(central_frame, text="Inferiores", fg_color="#808080", hover_color="#A9A9A9", command=self.Inferiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_inferiores.grid(row=0, column=1, pady=(250, 00))

        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Home, font=("Arial", 18, "bold"), width=150, height=50)
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

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\Treinos\\Superiores\\Peito.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_Peito = ctk.CTkButton(central_frame, text="Peito", fg_color="#808080", hover_color="#A9A9A9", command=self.Peito, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Peito.grid(row=0, column=0, pady=(250, 00))

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\Treinos\\Superiores\\Costas.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_Costas = ctk.CTkButton(central_frame, text="Costas", fg_color="#808080", hover_color="#A9A9A9", command=self.Costas, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Costas.grid(row=0, column=1, pady=(250, 00))

        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Treinos, font=("Arial", 18, "bold"), width=150, height=50)
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


        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\Treinos\\Inferiores\\Perna.png"
        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_Perna = ctk.CTkButton(central_frame, text="Perna", fg_color="#808080", hover_color="#A9A9A9", command=self.Perna, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Perna.grid(row=0, column=0, pady=(250, 00))


        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_quadriceps = ctk.CTkButton(central_frame, text="Quadriceps", fg_color="#808080", hover_color="#A9A9A9", command=self.Quadriceps, font=("Arial", 18, "bold"), width=150, height=50)
        btn_quadriceps.grid(row=0, column=1, pady=(250, 00))


        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", command=self.Treinos, font=("Arial", 18, "bold"), width=150, height=50)

        btn_voltar.grid(row=1, column=0, columnspan=2, pady=(20, 0))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


    def Peito(self):
        # Limpar a janela
            for widget in self.winfo_children():
                widget.destroy()

            background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
            background_frame.pack(fill="both", expand=True)

            central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
            central_frame.pack(pady=20)
        
            label_peito = ctk.CTkLabel(central_frame, text="Treino de Peito", text_color="white", font=("Arial", 22, 'bold'))
            label_peito.grid(row=0, column=0, columnspan=3, pady=10)

            #Exercicio 1
            supino_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\supino reto.jpg" 
            self.supino_image = ctk.CTkImage(light_image=Image.open(supino_image_path), size=(150, 150))
            supino_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
            supino_frame.grid(row=1, column=0, padx=20, pady=20)

            label_supino_img = ctk.CTkLabel(supino_frame, image=self.supino_image, text="")
            label_supino_img.pack()

            label_supino_text = ctk.CTkLabel(supino_frame, text="Supino reto com barra\n3x15 reps", text_color="white", font=("Arial", 16))
            label_supino_text.pack()
            
            crucifixo_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\crucifixo inclinado.jpg" 
            self.crucifixo_image = ctk.CTkImage(light_image=Image.open(crucifixo_image_path), size=(150, 150))
            crucifixo_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30, width=200, height=200)
            crucifixo_frame.grid(row=1, column=1, padx=20, pady=20)

            label_crucifixo_img = ctk.CTkLabel(crucifixo_frame, image=self.crucifixo_image, text="")
            label_crucifixo_img.pack()

            label_crucifixo_text = ctk.CTkLabel(crucifixo_frame, text="Crucifixo inclinado\n3x15 reps", text_color="white", font=("Arial", 16))
            label_crucifixo_text.pack()

            # Exercício 3: Crucifixo no crossover polia alta
            crossover_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\crossover-musculos-.jpg" 
            self.crossover_image = ctk.CTkImage(light_image=Image.open(crossover_image_path), size=(150, 150))
            crossover_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
            crossover_frame.grid(row=1, column=2, padx=20, pady=20)

            label_crossover_img = ctk.CTkLabel(crossover_frame, image=self.crossover_image, text="")
            label_crossover_img.pack()

            label_crossover_text = ctk.CTkLabel(crossover_frame, text="Crucifixo no crossover\n3x15 reps", text_color="white", font=("Arial", 16))
            label_crossover_text.pack()


            # Adicionando Treino de Ombros
            label_ombros = ctk.CTkLabel(central_frame, text="Treino de Ombros", text_color="white", font=("Arial", 22, 'bold'))
            label_ombros.grid(row=2, column=0, columnspan=3, pady=10)

            # Exercício 1: Elevação lateral com halteres
            elevacao_lateral_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\elevacao_lateral.jpg" 
            self.elevacao_lateral_image = ctk.CTkImage(light_image=Image.open(elevacao_lateral_image_path), size=(150, 150))
            elevacao_lateral_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
            elevacao_lateral_frame.grid(row=3, column=0, padx=20, pady=20)

            label_elevacao_lateral_img = ctk.CTkLabel(elevacao_lateral_frame, image=self.elevacao_lateral_image, text="")
            label_elevacao_lateral_img.pack()

            label_elevacao_lateral_text = ctk.CTkLabel(elevacao_lateral_frame, text="Elevação lateral com halteres\n3x12 reps", text_color="white", font=("Arial", 16))
            label_elevacao_lateral_text.pack()

            # Exercício 2: Desenvolvimento com halteres
            desenvolvimento_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\desenvolvimento_halteres.jpg" 
            self.desenvolvimento_image = ctk.CTkImage(light_image=Image.open(desenvolvimento_image_path), size=(150, 150))
            desenvolvimento_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
            desenvolvimento_frame.grid(row=3, column=1, padx=20, pady=20)

            label_desenvolvimento_img = ctk.CTkLabel(desenvolvimento_frame, image=self.desenvolvimento_image, text="")
            label_desenvolvimento_img.pack()

            label_desenvolvimento_text = ctk.CTkLabel(desenvolvimento_frame, text="Desenvolvimento com halteres\n3x12 reps", text_color="white", font=("Arial", 16))
            label_desenvolvimento_text.pack()

            # Exercício 3: Remada alta com barra
            remada_alta_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\remada_alta_barra.jpg" 
            self.remada_alta_image = ctk.CTkImage(light_image=Image.open(remada_alta_image_path), size=(150, 150))
            remada_alta_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
            remada_alta_frame.grid(row=3, column=2, padx=20, pady=20)

            label_remada_alta_img = ctk.CTkLabel(remada_alta_frame, image=self.remada_alta_image, text="")
            label_remada_alta_img.pack()

            label_remada_alta_text = ctk.CTkLabel(remada_alta_frame, text="Remada alta com barra\n3x12 reps", text_color="white", font=("Arial", 16))
            label_remada_alta_text.pack()

            label_triceps = ctk.CTkLabel(central_frame, text="Treino de Tríceps", text_color="white", font=("Arial", 22, 'bold'))
            label_triceps.grid(row=4, column=0, columnspan=3, pady=10)

            # Exercício 1: Tríceps testa
            triceps_testa_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\triceps_testa.png" 
            self.triceps_testa_image = ctk.CTkImage(light_image=Image.open(triceps_testa_image_path), size=(150, 150))
            triceps_testa_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
            triceps_testa_frame.grid(row=5, column=0, padx=20, pady=20)

            label_triceps_testa_img = ctk.CTkLabel(triceps_testa_frame, image=self.triceps_testa_image, text="")
            label_triceps_testa_img.pack()

            label_triceps_testa_text = ctk.CTkLabel(triceps_testa_frame, text="Tríceps testa\n3x15 reps", text_color="white", font=("Arial", 16))
            label_triceps_testa_text.pack()

            # Exercício 2: Mergulho em bancos
            mergulho_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\mergulho_bancos.jpg" 
            self.mergulho_image = ctk.CTkImage(light_image=Image.open(mergulho_image_path), size=(150, 150))
            mergulho_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
            mergulho_frame.grid(row=5, column=1, padx=20, pady=20)

            label_mergulho_img = ctk.CTkLabel(mergulho_frame, image=self.mergulho_image, text="")
            label_mergulho_img.pack()

            label_mergulho_text = ctk.CTkLabel(mergulho_frame, text="Mergulho em bancos\n3x12 reps", text_color="white", font=("Arial", 16))
            label_mergulho_text.pack()

            # Exercício 3: Puxada de tríceps na polia
            puxada_polia_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\triceps_polia.jfif" 
            self.puxada_polia_image = ctk.CTkImage(light_image=Image.open(puxada_polia_image_path), size=(150, 150))
            puxada_polia_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
            puxada_polia_frame.grid(row=5, column=2, padx=20, pady=20)

            label_puxada_polia_img = ctk.CTkLabel(puxada_polia_frame, image=self.puxada_polia_image, text="")
            label_puxada_polia_img.pack()

            label_puxada_polia_text = ctk.CTkLabel(puxada_polia_frame, text="Puxada de tríceps na polia\n3x15 reps", text_color="white", font=("Arial", 16))
            label_puxada_polia_text.pack()


            # Frame inferior com botão Voltar
            frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=50)
            frame_inferior.pack(side="bottom", fill="x")

            btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Treinos, font=("Arial", 18, "bold"), width=150, height=50)
            btn_voltar.pack(pady=10)


    def Costas(self):

        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()

        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.pack(pady=20)

        # Título
        label_costas = ctk.CTkLabel(central_frame, text="Treino de Costas", text_color="white", font=("Arial", 22, 'bold'))
        label_costas.grid(row=2, column=0, columnspan=3, pady=10)

        # Exercício 1: Puxada alta
        puxada_alta_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\puxada.png" 
        self.puxada_alta_image = ctk.CTkImage(light_image=Image.open(puxada_alta_image_path), size=(150, 150))
        puxada_alta_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        puxada_alta_frame.grid(row=3, column=0, padx=20, pady=20)

        label_puxada_alta_img = ctk.CTkLabel(puxada_alta_frame, image=self.puxada_alta_image, text="")
        label_puxada_alta_img.pack()

        label_puxada_alta_text = ctk.CTkLabel(puxada_alta_frame, text="Puxada alta\n3x12 reps", text_color="white", font=("Arial", 16))
        label_puxada_alta_text.pack()

        # Exercício 2: Remada curvada
        remada_curvada_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\remada_curvada.jpg" 
        self.remada_curvada_image = ctk.CTkImage(light_image=Image.open(remada_curvada_image_path), size=(150, 150))
        remada_curvada_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        remada_curvada_frame.grid(row=3, column=1, padx=20, pady=20)

        label_remada_curvada_img = ctk.CTkLabel(remada_curvada_frame, image=self.remada_curvada_image, text="")
        label_remada_curvada_img.pack()

        label_remada_curvada_text = ctk.CTkLabel(remada_curvada_frame, text="Remada curvada\n3x12 reps", text_color="white", font=("Arial", 16))
        label_remada_curvada_text.pack()

        # Exercício 3: Levantamento terra
        levantamento_terra_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\levantamento_terra.jpg" 
        self.levantamento_terra_image = ctk.CTkImage(light_image=Image.open(levantamento_terra_image_path), size=(150, 150))
        levantamento_terra_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        levantamento_terra_frame.grid(row=3, column=2, padx=20, pady=20)

        label_levantamento_terra_img = ctk.CTkLabel(levantamento_terra_frame, image=self.levantamento_terra_image, text="")
        label_levantamento_terra_img.pack()

        label_levantamento_terra_text = ctk.CTkLabel(levantamento_terra_frame, text="Levantamento terra\n3x10 reps", text_color="white", font=("Arial", 16))
        label_levantamento_terra_text.pack()

        # Adicionando Treino de Bíceps
        label_biceps = ctk.CTkLabel(central_frame, text="Treino de Bíceps", text_color="white", font=("Arial", 22, 'bold'))
        label_biceps.grid(row=4, column=0, columnspan=3, pady=10)

        # Exercício 1: Rosca direta com barra
        rosca_direta_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\rosca_direta_barra.png"
        self.rosca_direta_image = ctk.CTkImage(light_image=Image.open(rosca_direta_image_path), size=(150, 150))
        rosca_direta_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        rosca_direta_frame.grid(row=5, column=0, padx=20, pady=20)

        label_rosca_direta_img = ctk.CTkLabel(rosca_direta_frame, image=self.rosca_direta_image, text="")
        label_rosca_direta_img.pack()

        label_rosca_direta_text = ctk.CTkLabel(rosca_direta_frame, text="Rosca direta com barra\n3x12 reps", text_color="white", font=("Arial", 16))
        label_rosca_direta_text.pack()

        # Exercício 2: Rosca martelo com halteres
        rosca_martelo_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\rosca_martelo.jfif"
        self.rosca_martelo_image = ctk.CTkImage(light_image=Image.open(rosca_martelo_image_path), size=(150, 150))
        rosca_martelo_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        rosca_martelo_frame.grid(row=5, column=1, padx=20, pady=20)

        label_rosca_martelo_img = ctk.CTkLabel(rosca_martelo_frame, image=self.rosca_martelo_image, text="")
        label_rosca_martelo_img.pack()

        label_rosca_martelo_text = ctk.CTkLabel(rosca_martelo_frame, text="Rosca martelo com halteres\n3x12 reps", text_color="white", font=("Arial", 16))
        label_rosca_martelo_text.pack()

        # Exercício 3: Rosca concentrada
        rosca_concentrada_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Senac-UC5\\Projeto Academia\\img\\rosca_concentrada.jfif"
        self.rosca_concentrada_image = ctk.CTkImage(light_image=Image.open(rosca_concentrada_image_path), size=(150, 150))
        rosca_concentrada_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        rosca_concentrada_frame.grid(row=5, column=2, padx=20, pady=20)

        label_rosca_concentrada_img = ctk.CTkLabel(rosca_concentrada_frame, image=self.rosca_concentrada_image, text="")
        label_rosca_concentrada_img.pack()

        label_rosca_concentrada_text = ctk.CTkLabel(rosca_concentrada_frame, text="Rosca concentrada\n3x12 reps", text_color="white", font=("Arial", 16))
        label_rosca_concentrada_text.pack()


        # Frame inferior com botão Voltar
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=50)
        frame_inferior.pack(side="bottom", fill="x")

        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Treinos, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.pack(pady=10)





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
        # Remove todos os widgets existentes
        for widget in self.winfo_children():
            widget.destroy()

        self.puxar_informações()
        
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Configurações da janela para centralização
        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_columnconfigure(1, weight=1)
        background_frame.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        background_frame.grid_rowconfigure(6, weight=1)  # Espaço na parte inferior

        # Ajusta o tamanho da tela
        self.geometry("800x600")  # Largura e altura maiores para acomodar mais espaço
        
        # Criando o frame verde
        frame_verde = ctk.CTkFrame(background_frame, fg_color="#313131", corner_radius=10, border_color="green", border_width=7)
        frame_verde.grid(row=1, column=0, columnspan=2, padx=40, pady=40)  # Aumentei o padding

        # Criando a fonte Nunito
        nunito_font = ("Nunito", 12)  # Fonte um pouco maior
        titulo_font = ("Nunito", 16, "bold")
        botao_font = ("Nunito", 12, "bold")

        # Label para o título
        titulo_label = ctk.CTkLabel(frame_verde, text="Editar Informações", text_color="White", font=titulo_font)
        titulo_label.grid(row=0, column=1, pady=15)  # Mais espaço vertical

        # Labels e entradas para nome
        self.entry_novo_nome = ctk.CTkEntry(frame_verde, fg_color="#ffffff", text_color="Black", font=nunito_font)
        label_nome = ctk.CTkLabel(frame_verde, text="Nome:", text_color="White", font=nunito_font)
        label_nome.grid(row=1, column=0, pady=10, sticky='e')  # Espaço vertical maior
        self.entry_novo_nome.grid(row=1, column=1, pady=10)
        self.entry_novo_nome.insert(0, f'{self.get_informacao(1).lower().capitalize()}')

        # Labels e entradas para data de nascimento
        self.entry_dataDeNascimento = ctk.CTkEntry(frame_verde, fg_color="#ffffff", text_color="Black", font=nunito_font)
        label_datanasc = ctk.CTkLabel(frame_verde, text="Data de nascimento:", text_color="White", font=nunito_font)
        label_datanasc.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.entry_dataDeNascimento.grid(row=2, column=1, pady=10)
        self.entry_dataDeNascimento.insert(0, f'{self.get_informacao(7)}')

        # Botão do calendário com cor preta
        self.btn_calendario = ctk.CTkButton(frame_verde, text="Escolher data", command=self.abrir_calendario, fg_color="#000000", text_color="#ffffff")
        self.btn_calendario.grid(row=2, column=2, padx=10)  # Espaço lateral maior

        # Labels e entradas para endereço
        self.entry_novo_endereco = ctk.CTkEntry(frame_verde, fg_color="#ffffff", text_color="Black", font=nunito_font)
        label_endereco = ctk.CTkLabel(frame_verde, text="Endereço:", text_color="White", font=nunito_font)
        label_endereco.grid(row=3, column=0, pady=10, sticky='e')
        self.entry_novo_endereco.grid(row=3, column=1, pady=10)
        self.entry_novo_endereco.insert(0, f'{self.get_informacao(5)}')

        # Labels e entradas para telefone
        self.entry_novo_telefone = ctk.CTkEntry(frame_verde, fg_color="#ffffff", text_color="Black", font=nunito_font)
        label_telefone = ctk.CTkLabel(frame_verde, text="Telefone:", text_color="White", font=nunito_font)
        label_telefone.grid(row=4, column=0, pady=10, sticky='e')
        self.entry_novo_telefone.grid(row=4, column=1, pady=10)
        self.entry_novo_telefone.insert(0, f'{self.get_informacao(4)}')

        # Labels e entradas para email
        self.entry_novo_email = ctk.CTkEntry(frame_verde, fg_color="#ffffff", text_color="Black", font=nunito_font)
        label_email = ctk.CTkLabel(frame_verde, text="E-mail:", text_color="White", font=nunito_font)
        label_email.grid(row=5, column=0, pady=10, sticky='e')
        self.entry_novo_email.grid(row=5, column=1, pady=10)
        self.entry_novo_email.insert(0, f'{self.get_informacao(2)}')

        # Labels e entradas para nova senha
        label_nova_senha = ctk.CTkLabel(frame_verde, text="Nova senha:", text_color="White", font=nunito_font)
        label_nova_senha.grid(row=6, column=0, pady=10, sticky='e')
        self.entry_nova_senha = ctk.CTkEntry(frame_verde, fg_color="#ffffff", text_color="Black", font=nunito_font, show='*')
        self.entry_nova_senha.grid(row=6, column=1, pady=10)

        # Botão de cancelar
        self.btn_voltar = ctk.CTkButton(frame_verde, text="Cancelar", command=self.Home, fg_color="#000000", text_color="#FF0000")
        self.btn_voltar.grid(row=7, column=1, pady=15)

        # Botão de salvar alterações
        botao_salvar = ctk.CTkButton(frame_verde, text="Salvar alterações", fg_color="#000000", text_color="#00ff00", font=botao_font, command=self.salvar_alterações)
        botao_salvar.grid(row=8, column=1, pady=15)