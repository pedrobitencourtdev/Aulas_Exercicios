#verificando uma string de forma mais produnda
#aqui eu posso contar quantas vezes a letra escolhida aparece na frase
#colocar 2 função no mesmo input
frase = str(input('Digite uma frase: ')).lower().strip()
pergunta = str(input('Qual letra você quer contar na frase? ')).lower().strip()

print('A letra', pergunta, 'aparece {} vezes na frase'.format(frase.count(pergunta), frase.lower(), pergunta.lower()))
print('A primeira letra', pergunta,'apareceu na posição {}'.format(frase.find(pergunta), frase.lower(), pergunta.lower()))
print('A ultima letra',pergunta, 'apareceu na posição {}'.format(frase.rfind(pergunta), frase.lower(), pergunta.lower())) #aqui com o rfind vai buscar a ultima vez que apareceu a letra escolhida na frase.