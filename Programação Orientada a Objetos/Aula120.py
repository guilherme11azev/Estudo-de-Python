'''
class - Clases são moldes para criar novos objetos (instâncias) que podem ter seus próprios
atributos e métodos.
Os objetos gerados pela classe podem usar seus dados internos para validar ações.
Por conversão, utilizamos PascalCase para nomes de classes.
'''


class Pessoa:
    def __initi__(self, nome, sobrenome):
            self.nome =  nome
            self.sobrenome = sobrenome

p1 = Pessoa('Guilherme', 'Duarte')
p2 = Pessoa('Giovanna', 'Marson')

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)