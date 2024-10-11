from repository.repositories import ClienteRepository
from view.app import Application

def main():
    # Inicializar o banco de dados
    repository = ClienteRepository()
    repository.init_db()

    # Inicializar a interface gráfica
    app = Application()
    app.mainloop()

# Executar a função main
if __name__ == "__main__":
    main()

    # Teste