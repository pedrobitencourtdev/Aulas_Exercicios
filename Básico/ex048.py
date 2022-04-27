#vericando nome se tem uma palavra que você quer e sempre lembre de mudar pra maiúsculo ou minusculo para não dar erro no programa.
nome = str(input('Digite seu nome Completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
