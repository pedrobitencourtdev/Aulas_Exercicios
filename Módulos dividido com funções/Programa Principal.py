import moedas


p = float(input('Digite o Preço: '))
d = float(input('Digite o Desconto: '))
print(f'A metade do R${p} é {moedas.metade(p)}')
print(f'O dobro de R${p} é {moedas.dobro(p)}')
print(f'O Valor R${p} com 10% de desconto é {moedas.diminuir(p, d)}')
print(f'A metade do R${p} é {moedas.metade(p)}')
print(f'Se Acrescentar 10% de R${p} é {moedas.aumentar(p, d)}')
