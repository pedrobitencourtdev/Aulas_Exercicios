resposta = 'S'
soma = quant = media = maior = menor = 0
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Acabou!')
print(('O maior valor foi {} e o menor foi {}'.format(maior, menor)))
