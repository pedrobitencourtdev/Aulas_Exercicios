#calculando unidade, dezenas, centenas, milhares

num = int(input('Informe um número: '))
u = num // 1 % 10 #calculo de unidade
d = num // 10 % 10 #Calculo de Dezena
c = num // 100 % 10 #Cálculo de Centena
m = num // 1000 % 10 #Cálculo de Milhar
print('Analizando o Número {}'.format(num))
print('Unidade:{}'.format(u))
print('Dezenas:{}'.format(d))
print('Centenas:{}'.format(c))
print('Milhar:{}'.format(m))
