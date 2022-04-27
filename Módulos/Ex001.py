#fazer o pc pensar em um número inteiro de 1 a 5 e se o usuário acertar escreva um msg na tela se ele errar escreva outro
#usarei o randomint para número inteiros
import random
while True:
    num = int(input('Digite um número inteiro: '))
    r1 = random.randint(1, 5)
    print('O computador escolheu o número {}'.format(r1))
    if (num == r1):
        print('Parabéns, Você venceu!')
    else:
        print('Que pena, você perdeu!')
