#fazer o pc pensar em um número inteiro de 1 a 5 e se o usuário acertar escreva um msg na tela se ele errar escreva outro
#usarei o randomint para número inteiros
from random import randint
from time import sleep #função que faz o computador dormir por alguns segundos
while True:
    num = int(input('Em que número de 1-5 estou pensando? : '))
    r1 = randint(1, 5)


    if (num == r1):
        print('Processando...')
        sleep(2)
        print('Eu pensei em {}'.format(r1))
        print('Parabéns, Você me venceu!')
    else:
        print('Processando...')
        sleep(2)
        print('Eu pensei em {}'.format(r1))
        print('Que pena, você perdeu!')
