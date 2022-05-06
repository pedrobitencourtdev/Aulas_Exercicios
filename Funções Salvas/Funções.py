# função com calculo de terreno
def calcular_terreno():
    cumprimento = float(input('cumprimento do Terreno: '))
    largura = float(input('Largura do Terreno: '))
    area = largura * cumprimento
    tamanho = area / 2
    print(f'A área de um terreno com {cumprimento:.2f}m de cumprimento e {largura:.2f}m de largura é {tamanho:.2f}m²')


# Função para Printar linhas com mensagem no meio
def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


mensagem('Digite uma frase')