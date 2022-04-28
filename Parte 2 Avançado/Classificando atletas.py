# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
from time import sleep
from datetime import datetime
nome = str(input('Nome do Atleta: '))
ano = int(input('Ano de nascimento do Atleta: '))
atual = datetime.today().year
calc = atual - ano
if calc > 0 and calc <= 9:
    print('O atleta {}, idade {} anos entra na categoria MIRIN'.format(nome, calc))
elif calc > 9 and calc <= 14:
    print('O atleta {}, idade {} anos entra na categoria INFANTIL'.format(nome, calc))
elif calc > 14 and calc <= 19:
    print('O atleta {}, idade {} anos entra na categoria JÚNIOR'.format(nome, calc))
elif calc > 19 and calc <= 25:
    print('O atleta {}, idade {} anos entra na categoria SÊNIOR'.format(nome, calc))
else:
    calc > 25
    print('O atleta {}, idade {} anos entra na categoria MASTER'.format(nome, calc))