#calculand nota dos alunos e aprovando ou reprovando
from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
media = (n1 + n2)/ 2
print('Nome do Aluno')
print('{:=^40}'.format(nome))
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('Calculando nota...')
    sleep(3)
    print('Sua média foi {:.1f}, você está \033[1;31mREPROVADO'.format(media))
elif media >= 5 and media < 6.9:
    print('Calculando nota...')
    sleep(3)
    print('Sua Média foi {:.1f} você está em: \033[1;33mRECUPERAÇÃO'.format(media) )
elif media >= 7.0:
    print('Calculando nota...')
    sleep(3)
    print('Sua média foi {:.1f} você está: \033[1;32mAPROVADO'.format(media))
#===========================Fim==============================