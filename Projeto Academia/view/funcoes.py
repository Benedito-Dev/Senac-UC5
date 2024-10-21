import tkinter as tk
import re
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime, date
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

    def Exibir_senha(self):
        if self.check_senha.get() == 1:
            self.entry_senha.configure(show="")
        else:
            self.entry_senha.configure(show="*")


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
        
        if not self.controler.validar_email(email):
            messagebox.showerror("Erro", "Email já cadastrado no sistema. ")
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
        
        # Verifica se o CPF já está cadastrado
        if not self.controler.validar_cpf(cpf):
            messagebox.showerror("Erro", "O CPF já está cadastrado no sistema.")
            return
        
        if self.validar_data(data_de_nascimento):
            messagebox.showerror("Erro", "Insira uma data valida por favor")
            return

        # Se todos os dados estiverem válidos, prosseguir com a lógica de envio
        self.enviar_dados(nome=nome, email=email, senha=senha, telefone=telefone, endereco=endereco, cpf=cpf, data_de_nascimento=data_de_nascimento)

    # Função para validar a idade do novo usuário

    def enviar_dados(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento):
        if self.controler.adicionar_usuario(nome.upper(), email, senha, telefone, endereco, cpf, data_de_nascimento):
            self.after(500, self.menu_inicial)

            
    from datetime import datetime, date

    def validar_data(self, data_nascimento_str):
        try:
            if isinstance(data_nascimento_str, date):
                data_nascimento = data_nascimento_str
            
            else:
                data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()

            # Obtém a data atual
            data_atual = datetime.now().date()

            # Verifica se a data de nascimento é no futuro
            if data_nascimento > data_atual:
                return True

            # Calcula a diferença de anos
            idade = data_atual.year - data_nascimento.year

            # Ajusta a idade caso o aniversário ainda não tenha ocorrido este ano
            if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1

            # Verifica se a idade é menor que 12
            if idade >= 12:
                return False
            
            else :
                return True

        except ValueError as e:
                # Retorna False se o formato da data for inválido
                print(f"O erro é {e}")
                return False


    def abrir_calendario(self):
        janela_calendario = tk.Toplevel(self)
        janela_calendario.title("Selecione a data de nascimento")

        calendario = Calendar(janela_calendario, selectmode="day", year=2000, month=1, day=10)
        calendario.pack(pady=20)

        def pegar_data():
            data_selecionada = calendario.get_date()
            # Convertendo a data para o formato "YYYY-MM-DD"
            self.entry_dataDeNascimento.delete(0, tk.END)
            self.entry_dataDeNascimento.insert(0, data_selecionada)
            janela_calendario.destroy()

        btn_selecionar_data = ttk.Button(janela_calendario, text="Selecionar", command=pegar_data)
        btn_selecionar_data.pack(pady=10)

    def validando_login(self):
        nome = self.entry_nome.get().strip()
        
        # Chama o método do controlador para validar o login
        if self.controler.fazer_login(nome.upper()) :
            self.nome_usuario = nome.capitalize()
            self.after(500, self.Home)
        else:
            pass
    
    def puxar_informacoes(self):
        user_name = self.nome_usuario.strip().upper()

        try:
            user = self.controler.obter_usuario_por_nome(user_name)


            if user:
                self.informacoes = user


            else:
                messagebox.showinfo("Info", "Usuario não encontrado")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Ao buscar informações : {e}")

    def get_informacao(self, informacao):
        return getattr(self.informacoes, informacao, None)
    
    def validar_alteracoes(self):
        id_cliente = self.get_informacao("id")  # Renomeado para id_cliente para maior clareza

        novo_nome = self.entry_novo_nome.get().strip().upper() or self.get_informacao("nome").upper()
        nova_data_de_nascimento = self.entry_dataDeNascimento.get().strip() or self.get_informacao("data_de_nascimento")
        novo_endereco = self.entry_novo_endereco.get() or self.get_informacao("endereco")
        novo_telefone = self.entry_novo_telefone.get().strip() or self.get_informacao("telefone")
        novo_email = self.entry_novo_email.get().strip() or self.get_informacao("email")
        nova_senha = self.entry_nova_senha.get().strip() or self.get_informacao("senha")

        # Validação do nome
        if len(novo_nome) < 3 or not novo_nome.isalpha():
            messagebox.showerror("Erro", "O nome deve ter pelo menos 3 letras e conter apenas caracteres alfabéticos.")
            return

        # Validação de e-mail
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_pattern, novo_email):
            messagebox.showerror("Erro", "Por favor, insira um e-mail válido.")
            return

        # Validação de senha
        if len(nova_senha) < 8 or not any(char.isdigit() for char in nova_senha) or not any(char.isalpha() for char in nova_senha):
            messagebox.showerror("Erro", "A senha deve ter pelo menos 8 caracteres e conter letras e números.")
            return

        # Validação de telefone
        if not novo_telefone.isdigit() or not (10 <= len(novo_telefone) <= 11):
            messagebox.showerror("Erro", "O telefone deve conter apenas números e ter 10 ou 11 dígitos.")
            return

        # Validação de endereço
        if len(novo_endereco) < 5:
            messagebox.showerror("Erro", "O endereço deve ter pelo menos 5 caracteres.")
            return

         # Validação de data de nascimento
        if self.validar_data(nova_data_de_nascimento):
             messagebox.showerror("Erro", "Data de nascimento inválida ou você deve ter mais de 12 anos.")
             return

        # Chamada para salvar alterações
        self.salvar_alterações(id_cliente, novo_nome, novo_email, nova_senha, novo_telefone, novo_endereco, nova_data_de_nascimento)

    def salvar_alterações(self, id, nome, email, senha, telefone, endereco, data_de_nascimento):
        if not data_de_nascimento:
            messagebox.showerror("Erro", "Data de nascimento inválida")
            return

        try:
            self.nome_usuario = nome
            self.controler.atualizar_usuario(id=id, nome=nome, data_de_nascimento=data_de_nascimento, endereco=endereco, telefone=telefone, email=email, senha=senha)
            self.after(500, self.Home)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar alterações: {e}")


    def deletar_perfil(self):
        # Verifica se há algum item selecionado
        if not (selected_item := self.tree.selection()):
            return messagebox.showwarning("Aviso", "Nenhum perfil selecionado.")

        user_id = self.tree.item(selected_item[0])['values'][0]  # Pega o ID do perfil selecionado

        # Confirmação
        if messagebox.askyesno("Confirmar", f"Você tem certeza que deseja deletar o perfil ID '{user_id}'?"):
            try:
                # Controlador lida com a exclusão no banco de dados e na visualização
                self.controler.deletar_usuario(user_id)
                self.tree.delete(selected_item[0])  # Remove o item da visualização
                messagebox.showinfo("Sucesso", "Perfil deletado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao deletar perfil: {e}")


    def Encerrar_programa(self):
        self.destroy()