<<<<<<< HEAD
#Faça um programa que esolha um número
import random
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: ')) 
n4 = str(input('Quarto Aluno: '))   
lista = [n1, n2, n3, n4]
escolhido = random.choices(lista)
=======
#Faça um programa que esolha um número
import random
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: ')) 
n4 = str(input('Quarto Aluno: '))   
lista = [n1, n2, n3, n4]
escolhido = random.choices(lista)
>>>>>>> 7facdac90e7257f9c12751a2f47331e619c2c5e3
print('O aluno escolhido foi {}'.format(escolhido))