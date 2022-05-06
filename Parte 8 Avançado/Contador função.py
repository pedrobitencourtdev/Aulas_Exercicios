# função que conta pulando números
from time import sleep


def contador():
    print('-' * 30)
    print('Contágem de 1 até 10 de 1 em 1')
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.3)
    print('FIM!')
    print('-' * 30)
    sleep(1)
    print('-' * 30)
    print('Contágem de 10 até 0 de 2 em 2')
    for i in range(10, 0, -2):
        print(i, end=' ')
        sleep(0.3)
    print('FIM!')
    print('-' * 30)
    sleep(1)
    print('-' * 30)
    print('Agora é sua vez de personalizar a contagem.')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if inicio < fim:
        for i in range(inicio, fim, passo,):
            print(i, end=' ')
            sleep(0.3)
            print('FIM!')
            print('-' * 30)
    else:
        while inicio >= fim:
            print(inicio, end=' ')
            inicio -= passo
            sleep(0.5)
        print('FIM!')

contador()