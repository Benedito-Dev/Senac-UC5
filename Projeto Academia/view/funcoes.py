import tkinter as tk
import re
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
from controller.controllers import UsuarioController


class Funções():
    def __init__(self):
        self.controler = UsuarioController()

    # Funções para acrescentar placeholder
    def on_entry_click(self, event):
        if len(entry.get()) > 0:  # type: ignore # Texto do placeholder
            entry.delete(0, tk.END)  # type: ignore # Limpa o placeholder
            entry.configure(fg_color='white')  # type: ignore # Muda a cor de fundo para branco
            entry.configure(fg='black')  # type: ignore # Muda a cor do texto

    def on_focusout(self, event):
        if entry.get() == '':  # type: ignore # Se o campo estiver vazio
            entry.insert(0, 'Digite aqui...')  # type: ignore # Reinsere o placeholder
            entry.configure(fg_color='grey')  # type: ignore # Muda a cor de fundo para cinza
            entry.configure(fg='grey')  # type: ignore # Muda a cor do texto

    def carregar_perfis(self):
        try:
            # Obtendo os dados da tabela através do controlador
            users = self.controler.listar_usuarios()

            # Inserindo os dados na ordem correta no TreeView
            for user in users:
                id = user.id  # Acessando o atributo 'id'
                nome = user.nome  # Acessando o atributo 'nome'
                email = user.email  # Acessando o atributo 'email'
                telefone = user.telefone  # Acessando o atributo 'telefone' # Acessando o atributo 'endereco'
                self.tree.insert('', tk.END, values=(id, nome, email, telefone))

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar perfis: {e}")


    def Exibir_senha(self):
        if self.check_senha.get() == 1:
            self.entry_senha.configure(show="")
        else:
            self.entry_senha.configure(show="*")

    def validar_dados(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()
        telefone = self.entry_telefone.get().strip()
        endereco = self.entry_endereco.get().strip()
        cpf = self.entry_cpf.get().strip()
        data_de_nascimento = self.entry_dataDeNascimento.get().strip()

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

        if len(cpf) != 11:  # Corrigido para verificar se o CPF tem exatamente 11 dígitos
            messagebox.showerror("Erro", "O CPF deve ter exatamente 11 dígitos.")
            return

        if not self.validar_data(data_de_nascimento):
            messagebox.showerror("Erro", "Você deve ter mais de 12 anos")
            return

        # Se todos os dados estiverem válidos, prosseguir com a lógica de envio
        self.enviar_dados(nome=nome, email=email, senha=senha, telefone=telefone, endereco=endereco, cpf=cpf, data_de_nascimento=data_de_nascimento)

    # Função para validar a idade do novo usuário
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
            return idade >= 12

        except ValueError:
            # Retorna False se o formato da data for inválido
            return False

    def enviar_dados(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento):
        if self.controler.adicionar_usuario(nome.upper(), email, senha, telefone, endereco, cpf, data_de_nascimento):
            self.after(500, self.menu_inicial)

    def abrir_calendario(self):
        janela_calendario = tk.Toplevel(self)
        janela_calendario.title("Selecione a data de nascimento")

        calendario = Calendar(janela_calendario, selectmode="day", year=2000, month=1, day=10)
        calendario.pack(pady=20)

        def pegar_data():
            data_selecionada = calendario.get_date()
            self.entry_dataDeNascimento.delete(0, tk.END)
            self.entry_dataDeNascimento.insert(0, data_selecionada)
            janela_calendario.destroy()

        btn_selecionar_data = ttk.Button(janela_calendario, text="Selecionar", command=pegar_data)
        btn_selecionar_data.pack(pady=10)

    def validando_login(self):
        nome = self.entry_nome.get().strip()
        senha = self.entry_senha.get().strip()
        
        # Chama o método do controlador para validar o login
        if self.controler.fazer_login(nome.upper(), senha) :
            self.nome_usuario = nome.capitalize()
            self.senha_usuario = senha
            self.after(500, self.Home)
        else:
            pass

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
                # Mudado de self.db para self.controler
                self.controler.deletar_usuario(user_id)  # Deleta o perfil do banco de dados
                self.tree.delete(selected_item[0])  # Remove o perfil do Treeview
                messagebox.showinfo("Sucesso", "Perfil deletado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao deletar perfil: {e}")

    def limpar_formulario(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_endereco.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_dataDeNascimento.delete(0, tk.END)
        messagebox.showinfo("Limpeza", "Os campos foram limpos com sucesso.")

    def atualizar_perfil(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Nenhum perfil selecionado.")
            return

        perfil_selecionado = self.tree.item(selected_item[0])['values']
        user_id = perfil_selecionado[0]  # Supondo que o ID é o primeiro valor

        # Pega os dados do formulário
        novo_nome = self.entry_nome.get().upper()
        novo_email = self.entry_email.get()
        nova_senha = self.entry_senha.get()
        novo_telefone = self.entry_telefone.get()
        novo_endereco = self.entry_endereco.get()
        novo_cpf = self.entry_cpf.get()
        nova_data_de_nascimento = self.entry_dataDeNascimento.get()

        # Confirmar com o usuário antes de atualizar
        confirm = messagebox.askyesno("Confirmar", "Tem certeza que deseja atualizar este perfil?")
        if confirm:
            try:
                # Mudado de self.db para self.controler
                self.controler.atualizar_usuario(user_id, novo_nome, novo_email, nova_senha, novo_telefone, novo_endereco, novo_cpf, nova_data_de_nascimento)
                messagebox.showinfo("Sucesso", "Perfil atualizado com sucesso!")
                self.carregar_perfis()  # Atualiza a lista de perfis
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao atualizar perfil: {e}")

    def Encerrar_programa(self):
        self.destroy()