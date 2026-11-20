'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
numeros = []

for i in range(5):
  num = float(input(f"Digite o {i+1}º número: "))
  numeros.append(num)

soma = sum(numeros)
media = soma / len(numeros)

print(f"\nA soma dos números é: {soma}")
print(f"A média dos números é: {media}")


