#operadores aritméticos
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
so = n1 + n2
su = n1 - n2
m = n1 * n2
di = n1 / n2
po = n1 ** n2
#esse end='' no final é para os dois prints ficarem todos na mesma linha.
print('\nA soma vale {}, \na subtração é {}, \na Multiplicação {}, \na Divisão é {:.3f} '.format(so, su, m, di), end='')
print('\nA potência é {:.2f}'.format(po))
