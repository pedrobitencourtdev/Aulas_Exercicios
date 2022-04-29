#sistema de pagamentos
from time import sleep
x = 'Lojas Bitencourt'
print('-' * 30)
print('{:=^30}'.format(x))
print('-' * 30)
preco = float(input('Qual valor do Produto? R$ '))
pag = int(input("""FORMAS DE PAGAMENTO \n[1] - À VISTA DINHEIRO/CHEQUE \n[2] - 2X NO CARTÃO \n[3] - À VISTA CARTÃO \n[4] - 3X OU MAIS NO CARTÃO \n>> """))

if pag == 1: # à vista dinheiro/cheque 10% Desconto
    desc = preco - (preco * 10)/100
    print('O valor do produto final é: {:.2f} '.format(desc))
elif pag == 2: # preço normal em 2x cartão
    print('O valor do produto final é: {:.2f}'.format(preco))
elif pag == 3:# à vista no cartão 5% desconto
    desc = preco - (preco * 5)/100
    print('O valor total do produto é {:.2f}'.format(desc))
elif pag == 4: # 3x ou mais no cartão juros de 20%
    juros = preco + (preco * 20)/100
    parc = int(input('QUANTAS PARCELAS (1-12):  '))
    totalp = juros / parc
    if parc >= 3:
        print('O Produto foi dividido em {} parcelas de R$ {:.2f}, com o valor total de R$ {:.2f} COM 20% DE JUROS'.format(parc, totalp, juros))
    else:
        print('O Valor máximo de parcelas é 3')
else:
    print('Opção Inválida. Tente novamente')

