#impar ou par: pego o número inteiro e pego o resto% dele com  2 se for igual a 0 é par se não for é impar!
x = int(input('Digite um número inteiro: '))


if (x % 2 == 0):
    print('você escolheu {} o Número é par!'.format(x))

else:
    print('você escolheu {} o número é impar'.format(x))

