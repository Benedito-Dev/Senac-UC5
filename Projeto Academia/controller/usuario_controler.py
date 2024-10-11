from repository.repository import UsuarioRepository
from config.db_config import db_config
from Model.usuario import Usuario

class UsuarioControler:
    def __init__(self):
        self.repository = UsuarioRepository(db_config)
        print("Controler Funcionando")