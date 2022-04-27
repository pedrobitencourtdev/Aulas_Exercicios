#exercício, criar um programa que leia o nome completo de alguem e mostre o nome com todas as letras maiúscula
#o nome com todas minúsculas, quantas letras sem considerar espaços e quantas letras tem o primeiro nome
#analisador de textos

#nome com todas as letras maiúsculas
nome = str(input('Digite seu nome completo: ')).strip()#com a strip já elimina os espaços das extremidades
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper())) #letras maiúsculas
print('Seu nome em minúsculo é {}'.format((nome.lower()))) #letras minúsculas
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #Contando as letras e o nome count com o sinal de - tirou o espaço do meio entre das palavras
print('Seu primeiro nome tem {}'.format(nome.find(' '))) #aqui o primeiro nome é contado através do .find e espaços
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} Letras'.format(separa[0], len(separa[0]))) # segunda forma de fazer