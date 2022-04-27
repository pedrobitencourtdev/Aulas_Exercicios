#programa que sorteia e embaralha os nomes dos alunos para apresentar trabalho!
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista) #o comando shuffle serve para embaralhar as coisas da lista
print('A ordem de apresentação é \n{}'.format(lista))
