import moedas
import cores

p = float(input('Digite o Preço: '))
print(f'A metade do {cores.verde(moedas.moeda(p))} é {cores.vermelho(moedas.metade(p, True))}')
print(f'O dobro de {cores.verde(moedas.moeda(p))} é {cores.vermelho(moedas.dobro(p, True))}')
print(f'O Valor {cores.verde(moedas.moeda(p))} com 10% de desconto é {cores.vermelho(moedas.diminuir(p, 10, True))}')
print(f'A metade do {cores.verde(moedas.moeda(p))} é {cores.vermelho(moedas.metade(p, True))}')
print(f'Se Acrescentar 10% de {cores.verde(moedas.moeda(p))} é {cores.vermelho(moedas.aumentar(p, 10, True))}')
print(cores.verde(moedas.aumentar(p)))