def dimensoesObjeto():
    """Esse código é responsável pela entrada dos dados
    que calcula a dimensão do pacote multiplicando os mesmos
    e dando condições que estão dentro do enunciado
    """
    while True:
        try:
            co = int(input('Digite comprimento do pacote em (cm): '))
            larg = int(input('Digite a largura do pacote em (cm): '))
            alt = int(input('Digite a altura do pacote em (cm): '))
            volume = co * larg * alt
            preco = 0
            while volume >= 100000:
                print('Não aceitamos objetos tão grandes')
                print('Entre com as dimensões novamente')
                co = int(input('Digite comprimento do pacote em (cm): '))
                larg = int(input('Digite a largura do pacote em (cm): '))
                alt = int(input('Digite a altura do pacote em (cm): '))
                volume = co * larg * alt
            print(f'O volume em cm é {volume}')
            if 0 < volume <= 1000:
                preco = 10
            elif 1001 < volume <= 10000:
                preco = 20
            elif 10001 < volume <= 30000:
                preco = 30
            elif 30001 < volume <= 100000:
                preco = 50
            return preco
        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não numérico.')


def pesoObjeto():
    """Esse código é responsável pela entrada dos dados
      que calcula o peso do pacote aplicando os mesmos
      e dando condições que estão dentro do enunciado
      """
    while True:
        try:
            peso1 = float(input('Digite peso pacote em (Kg): '))
            if 0.1 < peso1 <= 0.10:
                peso1 = 1
            elif 0.11 < peso1 < 1.0:
                peso1 = 1.5
            elif 1.10 < peso1 <= 10:
                peso1 = 2
            elif 10.1 < peso1 <= 30:
                peso1 = 3
            elif peso1 > 30:
                print('Não aceitamos objetos tão pesados')
            return peso1
        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não numérico.')


def rotaObjeto():
    """Esse código é responsável pela entrada dos dados
      que calcula a a rota do pacote multiplicando os mesmos
      e dando condições que estão dentro do enunciado
      """
    while True:
        try:
            print("""Escolha uma rota
            RS - De Rio de Janeiro até São Paulo
            SR - De São Paulo até Rio de Janeiro
            BS - De Brasília até São Paulo
            SB - De São Paulo até Brasília
            BR - De Brasília até Rio de Janeiro
            RB - De Rio até Brasília
            """)
            rote = str(input('Selecione uma Rota: ')).strip().upper()
            if rote == 'RS':
                rote = 1
            elif rote == 'SR':
                rote = 1
            elif rote == 'BS':
                rote = 1.2
            elif rote == 'SB':
                rote = 1.2
            elif rote == 'BR':
                rote = 1.5
            elif rote == 'RB':
                rote = 1.5
            return rote
        except ValueError:
            print('Você digitou uma rota que não existe.')