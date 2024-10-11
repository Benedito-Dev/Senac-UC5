from repository.repositories import ClienteRepository

class UsuarioController:
    def __init__(self):
        self.repository = ClienteRepository()  # Instancia o repositório de clientes

    # Controlador responsável por criar um produto
    def adicionar_produto(self, name, description, price):
        self.repository.cadastrar_cliente(name, description, price)

    def fazer_login(self, nome, senha):
        # Chama a função validar_login do repository
        if self.repository.validar_login(nome, senha):
            print("Login bem-sucedido!")
            return True
            # Aqui você pode adicionar outras lógicas, como redirecionar o usuário para a página principal.
        else:
            print("Nome ou senha incorretos!")
            # Aqui você pode mostrar uma mensagem de erro ao usuário ou redirecioná-lo de volta ao login
            

    # Controlador responsável por obter os produtos para exibir na interface
    def listar_usuarios(self):
        return self.repository.obter_usuarios()

    # Controlador responsável por atualizar um produto
    def atualizar_produto(self, product_id, name, description, price):
        self.repository.atualizar_cliente(product_id, name, description, price)

    # Controlador responsável por deletar um produto
    def deletar_produto(self, product_id):
        self.repository.deletar_cliente(product_id)
