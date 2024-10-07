# Usuario Controler
from repository.usuario_repository import RepositoryUsuario
from config.db_config import db_config
from model.usuario import Usuario

class UsuarioController:
    def __init__(self):
        self.repository = RepositoryUsuario(db_config)

    def criar_tabela(self):
        self.repository.create_table()

    def criar_usuario(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento):
        novo_usuario = Usuario(None, nome, email, senha, telefone, endereco, cpf, data_de_nascimento)
        self.repository.insert_user(novo_usuario)

    def atualizar_usuario(self, usuario_id, nome=None, email=None, telefone=None, endereco=None, data_de_nascimento=None):
        # Atualiza o usuário, passando apenas os campos que não são `None`
        self.repository.update_user(usuario_id, nome=nome, email=email, telefone=telefone, endereco=endereco, data_de_nascimento=data_de_nascimento)

    def validar_login(self, nome_login, senha_login):
        # Retorna o resultado da verificação do login
        return self.repository.verificando_usuario(nome_login=nome_login, senha_login=senha_login)

    def obter_usuario(self, nome):
        return self.repository.get_user_by_name(nome)

    def listar_usuarios(self):
        return self.repository.get_all_users()

    def deletar_usuario(self, usuario_id):
        self.repository.delete_user(usuario_id)

    def fechar_conexao(self):
        self.repository.close_connection()
