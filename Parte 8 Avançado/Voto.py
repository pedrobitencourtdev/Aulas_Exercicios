def voto(ent=0):
    from datetime import datetime
    atual = datetime.now().year
    nasc = int(input('Digite o ano de nascimento: '))
    ano = atual - nasc
    print(f'Sua idade atual é {ano} anos')
    if 18 <= ano < 68:
        print('Voto Obrigatório!')
    elif 16 <= ano <= 18 or ano >= 68:
        print('Voto Opcional!')
    else:
        if ano < 16:
            print('Você não tem direito a voto!')
    return


voto()
