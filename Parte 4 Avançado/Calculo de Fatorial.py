#calculo de fatorial
#sempre que for calcular uma multiplicação ele começa com 1
from math import factorial
#numero = int(input('Digite um número para calcular seu Fatorial: '))
#f = factorial(numero)
#print('O Fatorial de {} é {}'.format(numero, f))
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('O fatorial de {} é {}.'.format(n, f))
