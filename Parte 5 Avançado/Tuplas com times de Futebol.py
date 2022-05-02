# Times de Futebol
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO',)
print('-' * 15)
print(f'Lista de times do Brasileirão {times}')
print('-' * 15)
print(f'Os 5 Primeiros são {times[:5]}')
print('-' * 15)
print(f'Os 4 últimos colocados {times[-4:]}')
print('-' * 15)
print(f'Times em ordem alfabética {sorted(times)}')# sorted coloca em ordem alfabética
print('-' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ªposição')# o index busca em qual posição está a string
