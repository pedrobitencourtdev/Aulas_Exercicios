# tratando um erro exemplo 1
try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a / b
except Exception as erro:
    print(f'O Problema encontrado doi {erro.__class__}')
else:
    print(f'O Resultado foi  {r}')
finally:
    print('Volte Sempre meu amigo...')