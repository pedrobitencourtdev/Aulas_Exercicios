#programa de empréstimo bancário para financiamento de casa
#calculo
import time
#================VARIAVEIS==================#

nome = str(input('Nome completo: ')).strip().split()
print('Olá {} aguarde um momento estamos processando as informações...'.format(nome[0]))
time.sleep(1)
salario = float(input('Qual valor do seu salário? R$ '))
casa = float(input('Qual o valor da Casa? R$ '))
anos = int(input('Em quantos anos você quer kitar a casa? '))
min = (salario * 30) / 100
prestacao = casa / (anos * 12)

#================PRINTS==================#
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}'.format(prestacao))

#================CONDIÇÕES==================#
if prestacao <= min:
    print('Seu Empréstimo pode foi', '\033[1;32mAPROVADO')

else:
    print('Não Conseguimos aprovar seu Empréstimo', 'Status', '\033[1;31mNEGADO')
#================FIM==================#



