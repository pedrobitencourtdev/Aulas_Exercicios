#calcular usando dólar e real
#aqui você calcula quantos reais entra e divide ele pela cotação atual do dólar.
real = float(input('Quanto em reais você tem?: R$ '))
dolar = float(input('Qual a cotação atual do dólar?: $ '))

calc = real / dolar

print('Com o valor de {} você poderá comprar {:.2f} dólares'.format(real, calc))