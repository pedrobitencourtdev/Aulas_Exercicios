#calcular desconto
#basta ter atenção na hora de calcular, uma variável vai tirar o valor do desconto aí você soma o valor inserido - o valor de desconto
x = int(input('Digite o valor do Produto: R$ '))
calc = (x * 5) / 100
total = x - calc
print('O valor do produto é {} e com o desconto de 5% ficará {}'.format(x, total))