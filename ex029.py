#calculo de ângulo seno, cosseno, tangente
#leia um angulo e calcule o valor do seno, cosseno e tangente desse ângulo

import math
an = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o seno de {:.2f}'.format(an, seno))
cos = math.cos(math.radians(an))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tan))
