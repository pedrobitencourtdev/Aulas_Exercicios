#validação de dados
sexo = str(input('qual seu sexo? ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. por favor, tente novamente! ')).strip().upper()[0]
print('Sexo {} Registrado com sucesso'.format(sexo))
