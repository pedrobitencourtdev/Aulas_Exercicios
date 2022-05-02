# contador de números por extenso.
from time import sleep
cont = ('zero', 'um', 'dois', 'Tres', 'Quatro', 'Cinco',
        'seis', 'sete', 'oito', 'nove', 'Dez', 'onze',
        'doze', 'treze', 'Quatorze', 'Quinzee', 'Dezesseis',
        'dezessete', 'dezoitto', 'deszenove', 'vinte')
while True:
    try:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            print(f'você digitou o número {cont[num]}')
            pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
            while pergunta not in 'SN':
                pergunta = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()
            if pergunta == 'N':
                print('Encerrando programa...')
                sleep(2)
                print('Programa encerrado!')
                break
            else:
                continue
    except ValueError:
        print('você só pode digitar números!')