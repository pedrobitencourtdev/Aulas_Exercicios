#calcular aluguel de carro
#o valor do aluguel do carro é R$60 reais por dia, e o km é R$ 0.15 centávos
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km você percorreu? '))
pago = dias * 60 + (km * 0.15)
print('Você usou o veículo por {} dias \npercorreu {:.2f} Km.'.format(dias,km))
print('O Total a pagar é de R$: {:.2f}'.format(pago))