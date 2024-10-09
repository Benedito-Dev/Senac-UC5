# controller/usuario_controller.py
from repository.usuario_repository import UsuarioRepository
from config.db_config import db_config
from model.usuario import Usuario

class UsuarioController:
    def __init__(self):
        self.repository = UsuarioRepository(db_config)

    def criar_tabela(self):
        self.repository.criar_tabela()

    def criar_usuario(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento):
        # Mantendo o comportamento original de criação de usuário
        novo_usuario = Usuario(None, nome, email, senha, telefone, endereco, cpf, data_de_nascimento)
        self.repository.salvar_usuario(novo_usuario)

    def atualizar_usuario(self, usuario_id, nome=None, email=None, telefone=None, endereco=None, data_de_nascimento=None):
        # Mantendo o comportamento original da atualização parcial de usuário
        self.repository.atualizar_usuario(usuario_id, nome=nome, email=email, telefone=telefone, endereco=endereco, data_de_nascimento=data_de_nascimento)

    def validar_login(self, nome_login, senha_login):
        # Mantendo a função de validação de login
        return self.repository.verificar_usuario(nome_login=nome_login, senha_login=senha_login)

    def obter_usuario(self, nome):
        return self.repository.obter_usuario_por_nome(nome)

    def listando_usuarios(self):
        return self.repository.listar_usuarios()

    def deletar_usuario(self, usuario_id):
        self.repository.deletar_usuario(usuario_id)

    def fechar_conexao(self):
        self.repository.fechar_conexao()
