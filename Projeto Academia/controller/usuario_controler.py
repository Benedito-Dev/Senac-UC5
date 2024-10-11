from repository.usuario_repository import RepositoryUsuario
from config.db_config import Config
from model.usuario import Usuario

class UsuarioController:
    def __init__(self):
        self.repository = RepositoryUsuario(Config.SQLALCHEMY_DATABASE_URI)

    def criar_tabela(self):
        """Chama o repositório para criar a tabela 'usuarios'."""
        self.repository.create_table()

    def criar_usuario(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento):
        """Cria um novo usuário e insere no banco de dados."""
        try:
            novo_usuario = Usuario(None, nome, email, senha, telefone, endereco, cpf, data_de_nascimento)
            self.repository.insert_user(novo_usuario.nome, novo_usuario.email, novo_usuario.senha, 
                                        novo_usuario.telefone, novo_usuario.endereco, novo_usuario.cpf, 
                                        novo_usuario.data_de_nascimento)
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")

    def atualizar_usuario(self, usuario_id, nome=None, email=None, telefone=None, endereco=None, data_de_nascimento=None):
        """Atualiza um usuário no banco de dados pelos campos fornecidos."""
        try:
            self.repository.update_user(usuario_id, nome=nome, email=email, telefone=telefone, 
                                        endereco=endereco, data_de_nascimento=data_de_nascimento)
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")

    def validar_login(self, nome_login, senha_login):
        """Valida se o login do usuário é correto com base no nome e senha."""
        try:
            return self.repository.verificar_usuario(nome_login=nome_login, senha_login=senha_login)
        except Exception as e:
            print(f"Erro ao validar login: {e}")
            return False

    def obter_usuario(self, nome):
        """Obtém um usuário pelo nome."""
        try:
            return self.repository.get_user_by_name(nome)
        except Exception as e:
            print(f"Erro ao obter usuário: {e}")
            return None

    def listar_usuarios(self):
        """Retorna uma lista de todos os usuários cadastrados no banco de dados."""
        try:
            return self.repository.get_all_users()
        except Exception as e:
            print(f"Erro ao listar usuários: {e}")
            return []

    def deletar_usuario(self, usuario_id):
        """Deleta um usuário do banco de dados pelo ID."""
        try:
            self.repository.delete_user(usuario_id)
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados."""
        self.repository.close_connection()
