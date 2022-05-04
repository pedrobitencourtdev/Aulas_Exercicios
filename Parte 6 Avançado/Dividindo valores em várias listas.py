# dividindo valores em várias listas
comp = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        comp.append(n)
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
        comp.append(n)
    per = str(input('Deseja continuar? [s/n] ')).strip().upper()
    while per != 'S' and per != 'N':
        print('você só pode digitar S ou N')
        per = str(input('Deseja continuar? [s/n] ')).strip().upper()
    if per == 'S':
        continue
    else:
         if per == 'N':
            print(f'A lista completa é {comp}')
            print(f'A lista de pares é {pares}')
            print(f'A lista de ímpares é {impares}')
            break
