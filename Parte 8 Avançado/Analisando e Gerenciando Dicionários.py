def notas(*n, sit=False):
    """
    Função para analisar notas e situalões de vários alunos.
    Param n: uma ou mais notas dos alunos (aceita várias)
    Param sit: valor opcional, indicando se deve ou não adicionar a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7: # tenho que adicionar a situação aqui
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['média'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# programa principal
resp = notas(2.5, 9, 3.5, sit=True)
print(resp)
help(notas)
