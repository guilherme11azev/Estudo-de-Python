# Métodos em instâncias de classes python.
# Classes gerão instâncias.
#Hard Code - Algo que foi escrito diretamente no código.
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')
        
fusca = Carro('Fusca')
print(fusca.nome)
print(fusca.acelerar())

celta = Carro(nome='Celta')
print(celta.nome)
print(celta.acelerar())