# função com calculo de terreno
from time import sleep


def calcular_terreno():
    cumprimento = float(input('cumprimento do Terreno: '))
    largura = float(input('Largura do Terreno: '))
    area = largura * cumprimento
    tamanho = area / 2
    print(f'A área de um terreno com {cumprimento:.2f}m de cumprimento e {largura:.2f}m de largura é {tamanho:.2f}m²')


# Função para Printar linhas com mensagem no meio
def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


# Função que escreve na tela com linhas adaptáveis
def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt:}')
    print('~' * tam)


# função que conta de trás pra frente e visse versa obs: Requer função sleep
# função que conta pulando números
from time import sleep


def contador():
    print('-' * 30)
    print('Contágem de 1 até 10 de 1 em 1')
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.3)
    print('FIM!')
    print('-' * 30)
    sleep(1)
    print('-' * 30)
    print('Contágem de 10 até 0 de 2 em 2')
    for i in range(10, 0, -2):
        print(i, end=' ')
        sleep(0.3)
    print('FIM!')
    print('-' * 30)
    sleep(1)
    print('-' * 30)
    print('Agora é sua vez de personalizar a contagem.')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if inicio < fim:
        for i in range(inicio, fim, passo,):
            print(i, end=' ')
            sleep(0.3)
        print('FIM!')
        print('-' * 30)
    else:
        while inicio >= fim:
            print(inicio, end=' ')
            inicio -= passo
            sleep(0.5)
        print('FIM!')
        print('-' * 30)


def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da {lista}, temos {soma}')


def voto(ent=0):
    from datetime import datetime
    atual = datetime.now().year
    nasc = int(input('Digite o ano de nascimento: '))
    ano = atual - nasc
    print(f'Sua idade atual é {ano} anos')
    if 18 <= ano < 68:
        print('Voto Obrigatório!')
    elif 16 <= ano <= 18 or ano >= 68:
        print('Voto Opcional!')
    else:
        if ano < 16:
            print('Você não tem direito a voto!')
    return


def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        f += c
    return f



def leiaInt(msg): # validando dados de entrada
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um valor inteiro válido\033[m')
        if ok:
            break
    return valor