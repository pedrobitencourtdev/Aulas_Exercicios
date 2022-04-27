#calcular passagem de ônibus
x = float(input('Digite a distância que você irá percorrer KM: '))

if (x < 200):
    calc = x * 0.50
    print('De acordo com o valor percorrido o valor total a pagar é: {:.2f}'.format(calc))
else:
    (x > 200)
    calc = x * 0.45
    print('De acordo com a sua distância o valor a pagar é {:.2f} '.format(calc))