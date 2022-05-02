#tabuada usando laços
from time import sleep
nome = 'Tabuada do Biridin V2'
print('-=' * 15)
print('{:-^30}'.format(nome))
print('-=' * 15)
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        print('Encerrando Programa...')
        sleep(1)
        print('Programa Encerrado!')
        break
    for c in range(1, 11):
        sleep(0.2)
        print('|*','\033[1;32m{:^-5}x {:2} = {:^-5}\033[m''*|'.format(num, c, num*c))
