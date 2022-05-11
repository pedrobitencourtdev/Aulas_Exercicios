def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print(f'{entrada} é um preço inválido')
        else:
            valido = True
            return valido


entrada = leiaDinheiro('Digite o Preço: R$ ')
