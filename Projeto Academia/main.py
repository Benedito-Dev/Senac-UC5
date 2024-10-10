from view.view import Aplication
from Controller.usuario_controler import UsuarioControler

def main():

    controler = UsuarioControler

    app = Aplication(controler)
    app.mainloop()
    
if __name__ == '__main__':
    main()