#PA usando wihle
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ► '.format(termo), end=' ')
    cont += 1
    termo = termo + razão
    cont += 1
print('FIM')