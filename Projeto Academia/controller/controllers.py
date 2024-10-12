from repository.repositories import ClienteRepository
from tkinter import messagebox
from datetime import datetime

class UsuarioController:
    def __init__(self):
        self.repository = ClienteRepository()  # Instancia o repositório de clientes

    # Controlador responsável por criar um produto
    def adicionar_usuario(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento):
        # Convertendo data de nascimento para formato Correto
        data_de_nascimento = datetime.strptime(data_de_nascimento, '%d/%m/%Y').date()
        try:
            # Mudado de self.db para self.controler
            if self.repository.cadastrar_cliente(nome, email, senha, telefone, endereco, cpf, data_de_nascimento):
                messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
                return True
            else:
                messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")

    def fazer_login(self, nome, senha):
        # Chama a função validar_login do repository
            try:
                if self.repository.validar_login(nome, senha):
                    messagebox.showinfo("Sucesso", "Login Efetuado")
                    return True
                else :
                    messagebox.showerror("Erro", "Login Não encontrado")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro em nosso sistema, aguarde... {e}")
            
    # Controlador responsável por obter os produtos para exibir na interface
    def listar_usuarios(self):
        return self.repository.obter_usuarios()

    def obter_usuario_por_nome(self, nome):
        return self.repository.obter_usuario(nome)

    # Controlador responsável por atualizar um produto
    def atualizar_usuario(self, id, nome, data_de_nascimento, endereco, telefone, email, senha):
        try:

            nome = nome
            data_de_nascimento = data_de_nascimento
            endereco = endereco
            telefone = telefone
            email = email
            senha = senha
            self.repository.atualizar_cliente(id, nome, data_de_nascimento, endereco, telefone, email, senha)

        except Exception as e:
            raise Exception(f"Erro ao atualizar usuário: {e}")

    # Controlador responsável por deletar um produto
    def deletar_usuario(self, usuario_id):
        self.repository.deletar_cliente(usuario_id)
