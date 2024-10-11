from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'usuarios'
    
    # Campos da tabela 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    data_de_nascimento = Column(Date, nullable=False)

    def __repr__(self):
        return f'<Cliente {self.nome}>'
