# validando expressões matemáticas
expr = str(input('Digite a Expressão: '))
pilha = []
for sim in expr:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        pilha.append(')')
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida! ')
else:
    print('Sua expressão está errada! ')