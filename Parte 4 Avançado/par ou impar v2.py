#pegar os números pares que estão entre 1 e 50 e printar na tela while not in
print('Aqui está todos os números pares entre 1 e 50')
from random import randint
from time import sleep
vitoria = 0
while True:
    jogador = int(input('Diga um Valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi': #enquanto o tipo não tiver P ou I o programa vai continuar repetindo.
       tipo = str(input('Par ou Ímpar [P/I]')).strip().upper()[0] #tiro os espaços e coloco em maiúsculo
    print(f' Você jogou {jogador} e o computador {computador}. Total de {total} ')
    if tipo == 'P':
        if total %2 == 0:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você Perdeu :(')
            break
    elif tipo == 'I':
        if total %2 == 1:
            print('Você venceu!')
            vitoria += 1
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} Vezes')