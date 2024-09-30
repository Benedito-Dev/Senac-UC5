# Funções 
import tkinter as tk
import re
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime


class Funções():
        
    # Funções da Home
    def perfil(self):
        super().perfil()

    def treinos(self):
        super().treinos()

    def ajustes(self):
        super().ajustes()


    def carregar_perfis(self):
        try:
            # Obtendo os dados da tabela
            users = self.db.get_all_users()

            # Inserindo os dados na ordem correta no TreeView
            for user in users:
                id = user[0]  # Supondo que o id é a primeira coluna
                nome = user[1]  # Supondo que o nome é a segunda coluna
                email = user[2]  # Supondo que o email é a terceira coluna
                telefone = user[4]  # Supondo que o telefone é a quarta coluna
                endereco = user[5]  # Supondo que o endereço é a quarta coluna
                self.tree.insert('', tk.END, values=(id, nome, email, telefone, endereco))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar perfis: {e}")


    def Exibir_senha(self):
        if self.check_senha.get() == 1:
            self.entry_senha.config(show="")
        else:
            self.entry_senha.config(show="*")

    def validar_dados(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()
        telefone = self.entry_telefone.get().strip()
        endereco = self.entry_endereco.get().strip()
        data_de_nascimento = self.entry_dataDeNascimento.get().strip()
        cpf = self.entry_cpf.get().strip()        
       
        # Validação do nome (mínimo de 3 letras, apenas caracteres alfabéticos)
        if len(nome) < 3 or not nome.isalpha():
            messagebox.showerror("Erro", "O nome deve ter pelo menos 3 letras e conter apenas caracteres alfabéticos.")
            return

        # Validação de e-mail (usando expressão regular)
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_pattern, email):
            messagebox.showerror("Erro", "Por favor, insira um e-mail válido.")
            return

        # Validação de senha (mínimo de 8 caracteres, deve conter letras e números)
        if len(senha) < 8 or not any(char.isdigit() for char in senha) or not any(char.isalpha() for char in senha):
            messagebox.showerror("Erro", "A senha deve ter pelo menos 8 caracteres e conter letras e números.")
            return

        # Validação de telefone (deve conter apenas dígitos e ter 10 ou 11 números)
        if not telefone.isdigit() or not (10 <= len(telefone) <= 11):
            messagebox.showerror("Erro", "O telefone deve conter apenas números e ter 10 ou 11 dígitos.")
            return

        # Validação de endereço (mínimo de 5 caracteres, qualquer valor é permitido)
        if len(endereco) < 5:
            messagebox.showerror("Erro", "O endereço deve ter pelo menos 5 caracteres.")
            return
        
        if len(cpf) > 11 or len(cpf) < 11:
            messagebox.showerror("Erro", "cpf deve ter exatos 11 digitos")
            return
        
        if self.validar_data(data_de_nascimento) == False:
            messagebox.showerror("Erro", "Você deve ter mais de 12 anos")
            return


        # Se todos os dados estiverem válidos, prosseguir com a lógica de envio
        self.enviar_dados()

    def validar_data(self, data_nascimento_str):
        try:
            # Converte a string em um objeto datetime
            data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
            
            # Obtém a data atual
            data_atual = datetime.now()
            
            # Calcula a diferença de anos
            idade = data_atual.year - data_nascimento.year
            
            # Ajusta a idade caso o aniversário ainda não tenha ocorrido este ano
            if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1

            # Verifica se a idade é menor que 12
            if idade < 12:
                return False
            return True

        except ValueError:
            # Retorna False se o formato da data for inválido
            return False
    
    def enviar_dados(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        telefone = self.entry_telefone.get()
        endereco = self.entry_endereco.get()

        if not nome or not email:
            messagebox.showerror("Erro", "Por favor preencha todos os campos")
            return

        try:
            self.db.insert_user(nome, email, senha, telefone, endereco)
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.after(500, self.menu_inicial)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")


    def validar_login(self):
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()

        try:
            if self.db.verificando_usuario(nome, senha):
                messagebox.showinfo("Sucesso", "Login Efetuado")
                self.nome_usuario = nome
                self.after(500, self.Home)
            else:
                messagebox.showerror("Erro", "Nome ou senha inválidos")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro em nosso sistema, aguarde... {e}")


    def deletar_perfil(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Nenhum perfil selecionado.")
            return
        
        perfil_selecionado = self.tree.item(selected_item[0])['values']
        user_id = perfil_selecionado[0]  # Supondo que o ID é o primeiro valor

        confirm = messagebox.askyesno("Confirmar", f"Você tem certeza que deseja deletar o perfil ID '{user_id}'?")
        if confirm:
            try:
                self.db.delete_user(user_id)  # Deleta o perfil do banco de dados
                self.tree.delete(selected_item[0])  # Remove o perfil do Treeview
                messagebox.showinfo("Sucesso", "Perfil deletado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao deletar perfil: {e}")


    def Encerrar_programa(self):
            self.destroy()