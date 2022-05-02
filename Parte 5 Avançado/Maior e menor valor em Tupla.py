# sortear vários valores usando tuplas
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10) )
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO Maior valor sorteado foi {max(numeros)}')
print(f'O Menor valor sorteado foi {min(numeros)}')