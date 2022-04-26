#calcular metragem
# só pegar o valor de entrada da metragem multiplicar por 100, e os milímetros multiplica por 1000
s1 = int(input('Digite quantos metros você quer converter: '))
cm = s1 * 100
mm = s1 * 1000

print('O valor escolhido foi {}, que da {:.0f} Cm, e {:.0f} Milímetros'.format(s1, cm, mm))