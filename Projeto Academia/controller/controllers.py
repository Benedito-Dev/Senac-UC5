from repository.repositories import ClienteRepository
from tkinter import messagebox

class UsuarioController:
    def __init__(self):
        self.repository = ClienteRepository()  # Instancia o repositório de clientes

    # Controlador responsável por criar um produto
    def adicionar_produto(self, name, description, price):
        self.repository.cadastrar_cliente(name, description, price)

    def fazer_login(self, nome, senha):
        # Chama a função validar_login do repository
            try:
                if self.repository.validar_login(nome, senha):
                    messagebox.showinfo("Sucesso", "Login Efetuado")
                    return True
                else :
                    messagebox.showerror("Erro", "Login Não encontrado")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro em nosso sistema, aguarde... {e}")
            

    # Controlador responsável por obter os produtos para exibir na interface
    def listar_usuarios(self):
        return self.repository.obter_usuarios()

    # Controlador responsável por atualizar um produto
    def atualizar_produto(self, product_id, name, description, price):
        self.repository.atualizar_cliente(product_id, name, description, price)

    # Controlador responsável por deletar um produto
    def deletar_produto(self, product_id):
        self.repository.deletar_cliente(product_id)
