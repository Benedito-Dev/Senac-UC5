from view.gui import Application  # Importa a interface gráfica
from controller.usuario_controler import UsuarioController  # Importa o controlador

def main():
    # Cria uma instância do controlador, que gerenciará a lógica dos usuários
    usuario_controller = UsuarioController()

    # Cria a tabela de usuários no banco de dados
    usuario_controller.criar_tabela()

    # Inicializa a interface gráfica
    app = Application(usuario_controller)  # Passa o controlador para a aplicação

    # Inicia o loop da interface gráfica
    app.mainloop()

    # Fecha a conexão com o banco de dados ao finalizar a aplicação
    usuario_controller.fechar_conexao()

if __name__ == "__main__":
    main()
