#programa de sortear nomes
import random, emoji
pergunta = 'Quem vai mamar o Biridin'
print('{:=^30}'.format(pergunta))
while True:
    n1 = str(input('Nome do Primeiro Aluno: '))
    n2 = str(input('Nome do Segundo Aluno: '))
    n3 = str(input('Nome do Terceiro Aluno: '))
    n4 = str(input('Nome do Quarto Aluno: '))
    lista = [n1, n2, n3, n4]
    escolhido = random.choice(lista) #o escolhido dentro da lista
    print('O aluno escolhido foi {}'.format(escolhido))
