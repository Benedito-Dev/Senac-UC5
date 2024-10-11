from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.models import Base, Cliente
from config.config import Config

class ClienteRepository():
    def __init__(self):
        # Conectar ao banco de dados PostgreSQL
        self.engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    # Função para inicializar o banco de dados
    def init_db(self):
        Base.metadata.create_all(self.engine)

    # Função para cadastrar um novo cliente
    def cadastrar_cliente(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento):
        novo_cliente = Cliente(
            nome=nome,
            email=email,
            senha=senha,
            telefone=telefone,
            endereco=endereco,
            cpf=cpf,
            data_de_nascimento=data_de_nascimento
        )
        self.session.add(novo_cliente)
        self.session.commit()

    # Função para obter todos os clientes
    def obter_usuarios(self):
        return self.session.query(Cliente).all()

    # Função para atualizar um cliente
    def atualizar_cliente(self, cliente_id, nome, email, senha, telefone, endereco, cpf, data_de_nascimento):
        cliente = self.session.query(Cliente).get(cliente_id)
        if cliente:
            cliente.nome = nome
            cliente.email = email
            cliente.senha = senha
            cliente.telefone = telefone
            cliente.endereco = endereco
            cliente.cpf = cpf
            cliente.data_de_nascimento = data_de_nascimento
            self.session.commit()

    # Função para deletar um cliente
    def deletar_cliente(self, cliente_id):
        cliente = self.session.query(Cliente).get(cliente_id)
        if cliente:
            self.session.delete(cliente)
            self.session.commit()