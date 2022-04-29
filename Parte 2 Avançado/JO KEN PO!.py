# pedra papel tesoura
import random
from time import sleep

jogador = int(input('Escolha sua opção: \n[0] - Pedra \n[1] - Papel \n[2] - Tesoura \n>> '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2) #randomizar de tanto a tanto
print('-=' * 15)
 #se eu quiser colocar os itens por nome só seguir esse passo aqui!
print('\033[1;32mO você escolheu: {}\033[m'.format(itens[jogador]))
print('-=' * 15)
placarJ = 0
placarC = 0
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('JO!')
        sleep(1)
        print('KEN!')
        sleep(1)
        print('PO!')
        sleep(1)
        print('-=' * 10)
        print('Empate!')
        print('-=' * 10)
        sleep(2)
        print('\033[1;33mO computador escolheu: {}\033[m'.format(itens[computador]))
        print('-=' * 10)
        print('O placar é {} JOGADOR VS COMPUTADOR {}'.format(placarJ, placarC))
    elif jogador == 1:
        placarJ += 1
        print('JO!')
        sleep(1)
        print('KEN!')
        sleep(1)
        print('PO!')
        sleep(1)
        print('-=' * 10)
        print('O Jogador Ganhou!')
        print('-=' * 10)
        sleep(2)
        print('\033[1;33mO computador escolheu: {}\033[m'.format(itens[computador]))
        print('-=' * 10)
        print('O placar é {} JOGADOR VS COMPUTADOR {}'.format(placarJ, placarC))
    elif jogador == 2:
        placarC += 1
        print('JO!')
        sleep(1)
        print('KEN!')
        sleep(1)
        print('PO!')
        sleep(1)
        print('-=' * 10)
        print('O Computador Ganhou!')
        print('-=' * 10)
        sleep(2)
        print('\033[1;33mO computador escolheu: {}\033[m'.format(itens[computador]))
        print('-=' * 10)
        print('O placar é {} JOGADOR VS COMPUTADOR {}'.format(placarJ, placarC))
    else:
        print('Jogada Inválida.')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        placarC += 1
        print('JO!')
        sleep(1)
        print('KEN!')
        sleep(1)
        print('PO!')
        sleep(1)
        print('-=' * 10)
        print('O Computador Ganhou!')
        print('-=' * 10)
        sleep(2)
        print('\033[1;33mO computador escolheu: {}\033[m'.format(itens[computador]))
        print('-=' * 10)
        print('O placar é {} JOGADOR VS COMPUTADOR {}'.format(placarJ, placarC))
    elif jogador == 1:
        print('JO!')
        sleep(1)
        print('KEN!')
        sleep(1)
        print('PO!')
        sleep(1)
        print('-=' * 10)
        print('Empate!')
        print('-=' * 10)
        sleep(2)
        print('\033[1;33mO computador escolheu: {}\033[m'.format(itens[computador]))
        print('-=' * 10)
        print('O placar é {} JOGADOR VS COMPUTADOR {}'.format(placarJ, placarC))
    elif jogador == 2:
        placarJ += 1
        print('JO!')
        sleep(1)
        print('KEN!')
        sleep(1)
        print('PO!')
        sleep(1)
        print('-=' * 10)
        print('O Jogador Ganhou!')
        print('-=' * 10)
        sleep(2)
        print('\033[1;33mO computador escolheu: {}\033[m'.format(itens[computador]))
        print('-=' * 10)
        print('O placar é {} JOGADOR VS COMPUTADOR {}'.format(placarJ, placarC))
    else:
       print('Jogada Inválida.')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        placarJ += 1
        print('JO!')
        sleep(1)
        print('KEN!')
        sleep(1)
        print('PO!')
        sleep(1)
        print('-=' * 10)
        print('O Jogador Ganhou!')
        print('-=' * 10)
        sleep(2)
        print('\033[1;33mO computador escolheu: {}\033[m'.format(itens[computador]))
        print('-=' * 10)
        print('O placar é {} JOGADOR VS COMPUTADOR {}'.format(placarJ, placarC))
    elif jogador == 1:
        placarC += 1
        print('JO!')
        sleep(1)
        print('KEN!')
        sleep(1)
        print('PO!')
        sleep(1)
        print('-=' * 10)
        print('O Computador Ganhou!')
        print('-=' * 10)
        sleep(2)
        print('\033[1;33mO computador escolheu: {}\033[m'.format(itens[computador]))
        print('-=' * 10)
        print('O placar é {} JOGADOR VS COMPUTADOR {}'.format(placarJ, placarC))
    elif jogador == 2:
        print('JO!')
        sleep(1)
        print('KEN!')
        sleep(1)
        print('PO!')
        sleep(1)
        print('-=' * 10)
        print('Empate!')
        print('-=' * 10)
        sleep(2)
        print('\033[1;33mO computador escolheu: {}\033[m'.format(itens[computador]))
        print('-=' * 10)
        print('O placar é {} JOGADOR VS COMPUTADOR {}'.format(placarJ, placarC))
    else:
         print('Jogada Inválida.')
