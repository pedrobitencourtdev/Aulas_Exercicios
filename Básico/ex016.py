#calculando salário com aumento
#da mesma forma do exercício anterior aqui só você calcular o valor de entrada * o desconto e divide por 100
x = float(input('Quanto você ganha? R$ '))
calc = (x * 15) / 100
nsal = x + calc
print('O Valor atual do seu salário é R$ {} e o novo salário com 15% de aumento é R${}'.format(x, nsal))

#Segunda forma de fazer
salario = float(input('Quanto você ganha? R$ '))
calc = salario + (x * 15 / 100)

print('O Valor atual do seu salário é R$ {} e o novo salário com 15% de aumento é R${}'.format(salario, calc))
