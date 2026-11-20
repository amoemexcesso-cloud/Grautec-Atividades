'''
Faça um programa que leia três números e mostre-os em ordem decrescente:
'''
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))

ordem = sorted([num1, num2, num3], reverse=True)

print("Ordem decrescente:", *ordem)
