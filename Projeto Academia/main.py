from controller.controllers import UsuarioController
from view.app import Application

def main():
    # Inicializar o banco de dados
    controlador = UsuarioController()
    controlador.inicar_banco()

    # Inicializar a interface gráfica
    app = Application()
    app.mainloop()

# Executar a função main
if __name__ == "__main__":
    main()

# MVCR