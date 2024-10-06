class Usuario:
    def __init__(self, id, nome, cpf, endereco, telefone, data_de_nascimento , email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento