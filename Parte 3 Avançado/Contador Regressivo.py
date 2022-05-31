#contador regressivo para fogos de artifícios for in range laços de repetições
from time import sleep
#import emoji
x = 'Você está preparado?'
print('-=' * 10)
print('{:=^10}'.format(x))
print('-=' * 10)
cont = 11
for c in range(cont, 0, -1):
    cont += -1
    sleep(1)
    print(cont)
print('BoOoooOoM! Feliz Ano Novo!')
