#calculo bissexto, usando time do computador
#para pegar a data de um computador em tempo real uso a biblioteca datetime
from datetime import date
from time import sleep
ano = int(input('Que ano quer analizar? Coloque 0 Para analisar o ano atual. '))

if ano == 0:
    ano = date.today().year #aqui ele vai pegar só o ano atual.

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Calculando ano...')
    sleep(2)
    print('O ano {} é Bissexto'.format(ano))
else:
    print('Calculando ano...')
    sleep(3)
    print('O ano {} não é Bissexto'.format(ano))