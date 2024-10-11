from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Date, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from model.usuario import Usuario  # Supondo que o model 'Usuario' já esteja corretamente mapeado com SQLAlchemy

class RepositoryUsuario:
    def __init__(self, Config):
        self.engine = create_engine(Config)
        self.Session = sessionmaker(bind=self.engine)
        self.metadata = MetaData()
        self.connection = self.engine.connect()
        self.usuarios_table = Table('usuarios', self.metadata,
                                    Column('id', Integer, primary_key=True, autoincrement=True),
                                    Column('nome', String(100)),
                                    Column('email', String(100)),
                                    Column('senha', String(50)),
                                    Column('telefone', String(50)),
                                    Column('endereco', String(100)),
                                    Column('cpf', String(11), unique=True),
                                    Column('data_de_nascimento', Date))

    def create_table(self):
        try:
            self.metadata.create_all(self.engine)
            print("Tabela criada com sucesso!")
        except SQLAlchemyError as e:
            print(f"Erro ao criar a tabela: {e}")
            raise e

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def insert_user(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento):
        """Insere um novo usuário no banco de dados."""
        try:
            novo_usuario = Usuario(
                nome=nome, email=email, senha=senha, telefone=telefone,
                endereco=endereco, cpf=cpf, data_de_nascimento=data_de_nascimento
            )
            with self.Session() as session:
                session.add(novo_usuario)
                session.commit()
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            raise e

    def verificar_usuario(self, nome_login, senha_login):
        """Verifica se o usuário com nome e senha existe no banco (usado para login)."""
        try:
            with self.Session() as session:
                query = select(Usuario).where(Usuario.nome == nome_login, Usuario.senha == senha_login)
                resultado = session.execute(query).first()

                if resultado:
                    print(f"Usuário encontrado: {resultado.Usuario.nome}")
                    return True
                else:
                    print("Usuário não encontrado.")
                    return False
        except SQLAlchemyError as e:
            print(f"Erro ao verificar usuário: {e}")
            return False

    def delete_user(self, user_id):
        """Deleta um usuário do banco de dados pelo ID."""
        try:
            with self.Session() as session:
                user = session.query(Usuario).get(user_id)
                if user:
                    session.delete(user)
                    session.commit()
                else:
                    print(f"Usuário com ID {user_id} não encontrado.")
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            raise e

    def get_all_users(self):
        """Obtém todos os usuários do banco de dados."""
        try:
            with self.Session() as session:
                users = session.query(Usuario).all()
            return users
        except SQLAlchemyError as e:
            raise e

    def get_user_by_name(self, nome):
        """Busca um usuário pelo nome no banco de dados."""
        try:
            with self.Session() as session:
                user = session.query(Usuario).filter_by(nome=nome).first()
            return user
        except SQLAlchemyError as e:
            print(f"Erro ao buscar usuário: {e}")
            return None

    def update_user(self, user_id, nome=None, email=None, telefone=None, endereco=None, data_de_nascimento=None):
        """Atualiza informações de um usuário no banco de dados."""
        try:
            with self.Session() as session:
                user = session.query(Usuario).get(user_id)
                if user:
                    if nome:
                        user.nome = nome
                    if email:
                        user.email = email
                    if telefone:
                        user.telefone = telefone
                    if endereco:
                        user.endereco = endereco
                    if data_de_nascimento:
                        user.data_de_nascimento = data_de_nascimento

                    session.commit()
                else:
                    raise Exception(f"Usuário com ID {user_id} não encontrado.")
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            raise Exception(f"Erro ao atualizar usuário: {e}")

    def close(self):
        """Fecha a conexão com o banco de dados."""
        self.connection.close()
