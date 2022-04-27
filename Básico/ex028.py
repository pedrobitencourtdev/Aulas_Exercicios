#exercício de triangulo hipotenusa
#pego o cateto oposto elevo a 2 através do ** somo com o cateto adjacente elevo a dois tbm ** e elevo a meio (1/2) que seria (co ** 2 + ca ** 2) ** (1/2)
import math

co = float(input('O Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A Hipotenusa vai medir {:.2f}'.format(hi))

#maneira com importação de biblioteca
co = float(input('O Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co,ca)
print('O Hipotenusa vai medir {:.2f}'.format(hi))