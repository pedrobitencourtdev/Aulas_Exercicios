#calcular velocidade radar eletrônico
vel = float(input('Qual a velocidade do carro? '))
from time import sleep
if (vel > 80):
    print('Calculando Velocidade...')
    sleep(3)
    print('Você foi multado')
    multa = (vel - 80) * 7
    print('Valor total da multa é {}'.format(multa))
else:
    print('Calculando velocidade...')
    sleep(3)
    print('Tenha um bom dia dirija com segurança.')