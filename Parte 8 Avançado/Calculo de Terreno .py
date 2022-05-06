# função com calculo de terreno
def calcular_terreno():
    cumprimento = float(input('cumprimento do Terreno: '))
    largura = float(input('Largura do Terreno: '))
    area = largura * cumprimento
    tamanho = area / 2
    print(f'A área de um terreno com {cumprimento:.2f}m de cumprimento e {largura:.2f}m de largura é {tamanho:.2f}m²')


calcular_terreno()
