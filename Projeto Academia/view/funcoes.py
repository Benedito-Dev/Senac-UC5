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

    def Exibir_senha(self):
        if self.check_senha.get() == 1:
            self.entry_senha.configure(show="")
        else:
            self.entry_senha.configure(show="*")


    def carregar_perfis(self):
        try:
            # Obtendo os dados da tabela através do controlador
            users = self.controler.listar_usuarios()

            users = sorted(users, key=lambda user : user.nome)

            # Inserindo os dados na ordem correta no TreeView
            for user in users:
                id = user.id  # Acessando o atributo 'id'
                nome = user.nome  # Acessando o atributo 'nome'
                data_de_nascimento = user.data_de_nascimento
                self.tree.insert('', tk.END, values=(id, nome, data_de_nascimento))

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar perfis: {e}")


    def validar_dados(self):
        nome = self.entry_nome.get().strip()
        data_de_nascimento = self.entry_dataDeNascimento.get().strip()

        # Validação do nome (mínimo de 3 letras, apenas caracteres alfabéticos)
        if len(nome) < 3 or not nome.isalpha():
            messagebox.showerror("Erro", "O nome deve ter pelo menos 3 letras e conter apenas caracteres alfabéticos.")
            return

        # Se todos os dados estiverem válidos, prosseguir com a lógica de envio
        self.enviar_dados(nome=nome, data_de_nascimento=data_de_nascimento)

    # Função para validar a idade do novo usuário

    def enviar_dados(self, nome, data_de_nascimento):
        if self.controler.adicionar_usuario(nome.upper(), data_de_nascimento):
            self.after(500, self.menu_inicial)


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
        data_de_nascimento = self.entry_dataDeNascimento.get().strip()

        # Verificando atributos
        if len(nome) < 3 or not nome.isalpha():
            messagebox.showerror("Erro", "O nome deve ter pelo menos 3 letras e conter apenas caracteres alfabéticos.")
            return
        
        if not data_de_nascimento:
            messagebox.showerror("Erro", "A data de nascimento não pode estar vazia.")
            return
        
        #Convertendo data antes de enviar
        data_de_nascimento =  datetime.strptime(data_de_nascimento, "%d/%m/%Y")
        data_de_nascimento = data_de_nascimento.date()
        
        # Chama o método do controlador para validar o login
        if self.controler.fazer_login(nome.upper(), data_de_nascimento) :
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


        # Validação do nome
        if len(novo_nome) < 3 or not novo_nome.isalpha():
            messagebox.showerror("Erro", "O nome deve ter pelo menos 3 letras e conter apenas caracteres alfabéticos.")
            return

        # Chamada para salvar alterações
        self.salvar_alterações(id_cliente, novo_nome, nova_data_de_nascimento)


    def salvar_alterações(self, id, nome, data_de_nascimento):
        if not data_de_nascimento:
            messagebox.showerror("Erro", "Data de nascimento inválida")
            return

        try:
            self.nome_usuario = nome
            self.controler.atualizar_usuario(id=id, nome=nome, data_de_nascimento=data_de_nascimento)
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