# Nota e aprovação via dicionário
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'A Média do aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
    print(f'O Aluno {aluno["nome"]} está aprovado com média {aluno["media"]}')
    aluno['situação'] = 'Aprovado'
elif 7 > aluno['media'] > 5: # se 7 é maior que aluno que é maior q 5 então...
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é = {v}')
