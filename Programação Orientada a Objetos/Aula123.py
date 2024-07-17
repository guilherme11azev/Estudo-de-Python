# Escopo a classe e de métodos da classe
class Animal:

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
        
    def executar(self, *args, **kwargs):
        return self.comando(*args, **kwargs)



leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã')) 