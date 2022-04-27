#programa para calcular quantidade de tinta por metros quadrados
#obs para calcular a quantidade de tinta eu precisei calcular a área e dividir por 2 para chegar na quantidade de tinta

larg = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(larg,alt,area))
print('Para pintar essa parede você precisará de {} L de tinta'.format(tinta))