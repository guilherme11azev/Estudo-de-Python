# Metodo estados dentro da classe

class Camera:

    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando


    def filmar(self):
        print(f'{self.nome} está filmando')
        self.filmando = True

        