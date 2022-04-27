#aqui você pode validar uma string, também, não esqueça de usar .strip para quebrar os espaços

cid = str(input('Em que cidade você nasceu:? ')).strip()
print(cid[:5].lower() == 'santo')
