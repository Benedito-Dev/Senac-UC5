from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    
    # Campos da tabela 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    telefone = Column(String)
    endereco = Column(String)
    cpf = Column(String)
    data_de_nascimento = Column(Date)

    def __repr__(self):
        return f'<Cliente {self.nome}>'
