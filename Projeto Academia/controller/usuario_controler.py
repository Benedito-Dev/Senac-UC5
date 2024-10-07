# Usuario Controler
from repository.usuario_repository import RepositoryUsuario
from config.db_config import db_config
from model.usuario import Usuario

class UsuarioController:
    def __init__(self):
        self.repository = RepositoryUsuario(db_config)

    def criar_tabela(self):
        self.repository.create_table()

    def criar_usuario(self, nome, idade, profissao, cidade, genero, email, senha):
        novo_usuario = Usuario(None, nome, idade, profissao, cidade, genero, email, senha)
        self.repository.insert_user(novo_usuario)
    
    #def atualizar_usuario()

    def validar_login(self, nome_login, senha_login):
        self.repository.verificando_usuario(nome_login=nome_login, senha_login=senha_login)

    def obter_usuario(self, nome):
        return self.repository.get_user_by_name(nome)

    def listar_usuarios(self):
        return self.repository.get_all_users()

    def deletar_usuario(self, usuario_id):
        self.repository.delete_user(usuario_id)

    def fechar_conexao(self):
        self.repository.close_connection()