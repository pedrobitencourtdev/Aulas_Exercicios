#função Len e count
frase = 'Eu sou o Biridin o melhor do mundo!'
tam = len(frase) #serve para contar quantos caracteres tem na sua frase
print(tam)

frase = 'Eu sou o Biridin o melhor do mundo!'
tam = frase.lower().count('b') #serve para contar quantos caracteres tem na sua frase, o lower converte todas em minúsculas para contar.
print(tam)

frase = 'Eu sou o Biridin o melhor do mundo!'
tam = frase.lower().count('o', 0, 9) #aqui conto de as letras por distância, quantos o tenho de 0 a 12 caracteres
print(tam)

