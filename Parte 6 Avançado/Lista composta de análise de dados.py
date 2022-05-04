# lista composta de análise de dados
temp = []
princ = []
mai = 0
men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Você quer continuar? [s/n] '))
    if resp in 'Nn':
        break
print(f'os dados foram os {princ}')
print(f'ao todo você cadastrou {len(princ)} pessoas. ')
print(f'o maior peso foi {mai}Kg. com peso de', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print(f'o menor peso foi {men}Kg')

