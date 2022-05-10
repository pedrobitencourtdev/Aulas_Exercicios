print('Bem vindo a companhia de Logística João Pedro Gonçalves da Costa Silverio S.A')
import funçõesROTA
dimensoes = funçõesROTA.dimensoesObjeto()
peso = funçõesROTA.pesoObjeto()
rota = funçõesROTA.rotaObjeto()
calc = dimensoes * peso * rota
print('Total a pagar (R$) {:.2f} Dimensoes: {} * Peso {} * Rota {}'.format(dimensoes*peso*rota, dimensoes, peso, rota))
