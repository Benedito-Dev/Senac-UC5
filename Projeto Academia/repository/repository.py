import psycopg2
from psycopg2 import sql
from Model.usuario import Usuario

class UsuarioRepository():

    def __init__(self, db_config):
        self.connection = psycopg2.connect(**db_config)
        print("Conexão Bem sucecida")
    
    def close_connection(self):
        if self.connection:
            self.connection.close()