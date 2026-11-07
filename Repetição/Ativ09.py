'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
 
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
5 X 10 = 50
'''
tabuada = int(input("Insira qual tabuiada voce deseja: "))

#Tabuada de Multiplicação
print(f"\nTabuada de multiplicação de {tabuada}")

for i in range(1, 11):
    resultado = tabuada * i
    resultado2 = tabuada // i
    print(f"{tabuada} x {i} = {resultado} | {tabuada} / {i} = {resultado}")
