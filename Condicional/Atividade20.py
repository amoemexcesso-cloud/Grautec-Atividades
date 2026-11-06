'''
Faça um programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
'''
num = int(input("insira um número: "))

if num % 2 != 0:
    print("Número escolhido é impar")
else:
    print("Número escolhido é par")