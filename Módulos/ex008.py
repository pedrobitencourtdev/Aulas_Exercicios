#analisando triângulo
#colocando cores no python \033[1;32m < Código


print('\033[1;32m-=' * 12)
print('\033[1;32mANALIZADOR DE TRIÂNGULOS')
print('-=' * 12)
# para calcular os lado temos que calcular se o resultado de r1 é menor que a soma dos outros 2 ex r1 < r2 + r3
r1 = float(input('\033[1;33mDigite o primeiro valor: '))
r2 = float(input('\033[1;34mDigite o segundo valor: '))
r3 = float(input('\033[1;35mDigite o terceiro valor: '))

if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print('\033[1;32mOs segmentos acima podem formar um triângulo!')
else:
    print('\033[1;31mOs segmentos acima não podem formar um triângulo! ')