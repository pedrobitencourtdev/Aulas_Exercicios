#tabuada usando laços
from time import sleep
nome = 'Tabuada do Biridin V2'
print('-=' * 15)
print('{:-^30}'.format(nome))
print('-=' * 15)
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    sleep(0.4)
    print('|*','\033[1;32m{:^-5}x {:2} = {:^-5}\033[m''*|'.format(num, c, num*c))