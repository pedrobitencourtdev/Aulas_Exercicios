# Estatísticas em produtos
total = 0
totmil = 0
menor = 0
cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do programa')) #centralizar texto em print fácil
print(f'O Valor total da compra foi {total:.2f}')
print(f'Temos {totmil} produtoss custando mais de R$ 1000')
print(f'O produto mais barato {barato} que custa {menor:.2f}')