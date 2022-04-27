#aumento de salário com condicional

salario = float(input('Qual o Salário do funcionário? '))

if (salario < 1250):
   nsal = (salario * 15) / 100 + salario
   print('Você Ganhou um aumento de 15% seu novo salário é {:.2f}'.format(nsal))
else:
   (salario > 1250)
   nsal = (salario * 15) / 100 + salario
   print('Você recebeu um aumento de 10% seu novo salário é: {:.2f}'.format(nsal))