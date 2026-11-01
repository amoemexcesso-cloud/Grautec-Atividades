'''
Faça um programa que pergunte em que turno você estuda. Peça para digitar:
M - Matutino
V - Vespertino
N - Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
turno = input("Em que turno você estuda? digite M, V ou N. ").upper()

if turno == "M":
    print("O dia nem começou e eu já fui derrotado umas 3 vezes, bom dia!")

elif turno == "V":
    print("Não deixe pra fazer amanhã a merda você pode fazer hoje, boa tarde!")

elif turno == "N":
    print("Boa noite bruno!")

else:
    print("Tá moscando fio?")