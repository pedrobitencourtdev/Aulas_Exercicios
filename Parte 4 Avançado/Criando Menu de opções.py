#criando menu de opções
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor. '))
opcao = 0
while opcao != 5:
    print('''    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR
    [4] - REINICIAR
    [5] - SAIR DO PROGRAMA''')
    opcao = int(input('>> Qual é sua opção: '))
    if opcao == 1: #soma
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2: #multiplicação
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))
    elif opcao == 3:#maior valor
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:#reuniciar o programa
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor. '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
print('=' * 30)
print('Fim do programa! Volte sempre!')