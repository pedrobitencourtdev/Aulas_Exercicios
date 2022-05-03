numeros = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'Você Digitou os Valores {numeros}')
print(f'O Valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}')
else:
    print(f'O Valor 3 não foi digitado em nenhuma posição')
print(f'O valor 3 apareceu na {numeros.index(3)}ª Posição')
print(f'Os valores pares digitados foram:', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end='')