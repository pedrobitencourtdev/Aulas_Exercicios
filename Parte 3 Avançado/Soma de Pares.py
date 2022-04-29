#insira 6 números e some apenas os pares
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '.format(c)))
    if num % 2 == 0: # esse calculo eu tiro se é par ou não 
        soma += + num
        cont += + 1
print('Você informou {} números e a soma foi {}'.format(cont, soma))
