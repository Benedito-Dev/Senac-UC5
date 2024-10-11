from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

# Base para a criação das tabelas
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True)  # ID como chave primária
    nome = Column(String, nullable=False)  # Nome do usuário, obrigatório
    cpf = Column(String(11), unique=True, nullable=False)  # CPF com 11 caracteres e único
    endereco = Column(String, nullable=False)  # Endereço obrigatório
    telefone = Column(String, nullable=False)  # Telefone obrigatório
    data_de_nascimento = Column(Date, nullable=False)  # Data de nascimento no formato de data
    email = Column(String, unique=True, nullable=False)  # Email único e obrigatório
    senha = Column(String, nullable=False)  # Senha obrigatória

    def __init__(self, nome, cpf, endereco, telefone, data_de_nascimento, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.data_de_nascimento = data_de_nascimento
        self.email = email
        self.senha = senha

    # Representação da classe para fins de debug
    def __repr__(self):
        return f"<Usuario(nome={self.nome}, cpf={self.cpf}, email={self.email})>"
