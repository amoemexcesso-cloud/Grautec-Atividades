'''
Faça um programa que peça uma temperatura em graus
Fahrenheit, converta-a para Celsius e mostre o 
resultado.
Fórmula: C = 5 × ((F − 32) / 9).
Resposta / código:
'''
Fahrenheit = float(input(" Digite a temperatura em Fahrenheit: "))
Fahrenheit = Fahrenheit - 32
multiplicacao = Fahrenheit * 5
divisao = multiplicacao / 9
print("O valor específico em Celsius é", divisao)
