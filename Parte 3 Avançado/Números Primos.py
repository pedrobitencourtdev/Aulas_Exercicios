#leia um número inteiro e diga se é um número primo
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m') #o que for divisível fica amarelo
        tot += 1
    else:
        print('\033[31m') #o que não for fica vermelho
    print('{}'.format(c) , end='')
print('\no número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é um numero PRIMO ')
else:
    print('Ele não é um número primo')