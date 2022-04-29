#o maior ou menor peso lido
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Digite da {} Pessoa: Kg '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso
print('O Maior peso lido foi de {}kg'.format(maior))
print(('O Menor peso lido foi {}'.format(menor)))