# valores únicos em lista, importante! para validar
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros: # aqui fiz se o número não tiver na variavel números então adiciona
        numeros.append((n))
        print('valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar')
    r = str(input(('Quer continuar? [S/N] ')))
    if r in 'Nn':
        break
print('-' * 30)
numeros.sort()
print(f'você digitou os valores {numeros}')