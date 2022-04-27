# estrutura condicional !
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if (m >= 6.0):
    print('Sua média está boa')
else:
    print('Sua média foi {:.1f} estude mais '.format(m))

#condição simplificada
print('Parabéns' if m >= 6.0 else 'Estude mais')