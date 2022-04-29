#palíndromo é um nome ou frase que de trás pra frente tem o mesmo resultado de leitura

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('Você digitou a frase {},  de trás pra frente seria {}'.format(junto, inverso))
if inverso == junto:
    print('a Frases acima é PALÍNDROMO')
else:
    print('A frase não é um palíndromo')