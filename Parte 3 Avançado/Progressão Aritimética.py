#termos de Progressão Aritmética
# PA é contar de tanto a até tanto pulando de 2 em 2
print('=' * 17)
print(' 10 TERMOS DE PA')
print('=' * 17)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 -1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' ♠')
print('Acabou!')