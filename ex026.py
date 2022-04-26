#transformar número float em número inteiro atraves das bibliotecas.
import math
s1 = float(input('Insira um número real!'))
print('O valor que você escolheu foi {}, o valor inteiro dele é: {} '.format(s1, math.trunc(s1)))
#posso usar da seguinte forma também
s1 = float(input('Insira um número real!'))
print('O valor que você escolheu foi {}, o valor inteiro dele é: {} '.format(s1, int(s1)))
