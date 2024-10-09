import psycopg2
from psycopg2 import sql
from model.usuario import Usuario

class UsuarioRepository:
    def __init__(self, db_config):
        self.connection = psycopg2.connect(**db_config)

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def criar_tabela(self):
        """Cria a tabela de usuários no banco de dados, se ainda não existir."""
        with self.connection.cursor() as cursor:
            create_table_query = """
                CREATE TABLE IF NOT EXISTS clientes (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100),
                    email VARCHAR(100),
                    senha VARCHAR(50),
                    telefone VARCHAR(50),
                    endereco VARCHAR(100),
                    CPF VARCHAR(50),
                    Data_de_Nascimento DATE
                );
            """
            cursor.execute(create_table_query)
            self.connection.commit()

    def salvar_usuario(self, usuario):
        """Insere um novo usuário no banco de dados."""
        with self.connection.cursor() as cursor:
            insert_query = sql.SQL("""
                INSERT INTO clientes (nome, email, senha, telefone, endereco, CPF, Data_de_Nascimento)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """)
            cursor.execute(insert_query, (usuario.nome, usuario.email, usuario.senha, 
                                          usuario.telefone, usuario.endereco, usuario.cpf, 
                                          usuario.data_de_nascimento))
            self.connection.commit()

    def obter_usuario_por_nome(self, nome):
        """Busca um usuário pelo nome."""
        with self.connection.cursor() as cursor:
            select_query = sql.SQL("""
                SELECT id, nome, email, senha, telefone, endereco, CPF, Data_de_Nascimento
                FROM clientes
                WHERE nome = %s
            """)
            cursor.execute(select_query, (nome,))
            result = cursor.fetchone()
            if result:
                return Usuario(*result)
            return None

    def listar_usuarios(self):
        """Retorna uma lista de todos os usuários."""
        usuarios = []
        with self.connection.cursor() as cursor:
            select_query = sql.SQL("SELECT * FROM clientes")
            cursor.execute(select_query)
            for row in cursor.fetchall():
                usuarios.append(Usuario(*row))
        return usuarios

    def atualizar_usuario(self, user_id, nome=None, email=None, telefone=None, endereco=None, data_de_nascimento=None):
        """Atualiza os dados de um usuário com base nos campos fornecidos."""
        update_data = {}
        if nome:
            update_data['nome'] = nome
        if email:
            update_data['email'] = email
        if telefone:
            update_data['telefone'] = telefone
        if endereco:
            update_data['endereco'] = endereco
        if data_de_nascimento:
            update_data['Data_de_Nascimento'] = data_de_nascimento

        if update_data:
            columns = [sql.Identifier(k) for k in update_data.keys()]
            values = [sql.Literal(v) for v in update_data.values()]
            query = sql.SQL("UPDATE clientes SET ({}) = ({}) WHERE id = %s").format(
                sql.SQL(', ').join(columns),
                sql.SQL(', ').join(values)
            )

            with self.connection.cursor() as cursor:
                cursor.execute(query, (user_id,))
                self.connection.commit()

    def verificar_usuario(self, nome_login, senha_login):
        """Verifica se o usuário com o nome e senha fornecidos existe no banco de dados."""
        with self.connection.cursor() as cursor:
            select_query = sql.SQL("""
                SELECT id, nome
                FROM clientes
                WHERE nome = %s AND senha = %s
            """)
            cursor.execute(select_query, (nome_login, senha_login))
            result = cursor.fetchone()
            if result:
                return True
            return False

    def deletar_usuario(self, usuario_id):
        """Deleta um usuário pelo seu ID."""
        with self.connection.cursor() as cursor:
            delete_query = sql.SQL("DELETE FROM clientes WHERE id = %s")
            cursor.execute(delete_query, (usuario_id,))
            self.connection.commit()
