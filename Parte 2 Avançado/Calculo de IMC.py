#calculando o IMC índice de massa corporal
#calculando o IMC tem que pegar o peso dividido pela altura elevado ao quadrado

peso = float(input('Qual seu peso? (KG) '))
alt = float(input('Qual sua altura? (m) '))

imc = peso/ (alt ** 2)
print('o IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Peso Ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')