'''
Faça um programa que leia 5 números e informe o maior número.
'''
numeros = []

for i in range(5):
  num = float(input(f"Digite o {i+1}º número: "))
  numeros.append(num)

maior = max(numeros)

print(f"O maior número informado foi: {maior}")
