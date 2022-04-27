#usando o comando split para pegar somente o primeiro nome da pessoa ex:
import emoji

frase = str(input('Digite seu nome completo: '))
dividido = frase.split()
coracao = emoji.emojize(':red_heart:')

print('Olá',dividido [0], coracao)