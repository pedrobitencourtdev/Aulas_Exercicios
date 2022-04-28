#alistamento Militar
#para pegar a idade eu calculei 18 - a idade atual, e o resultado é a quantidade de ano que passou ou falta passar
from datetime import date
from time import sleep

atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Obtendo informações aguarde...')
sleep(4)
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Calculando...')
    sleep(2)
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Calculando...')
    sleep(2)
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será no ano de {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Calculando...')
    sleep(2)
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi no ano de {} '.format(ano))