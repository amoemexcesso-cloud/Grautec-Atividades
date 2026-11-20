'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
'''
<<<<<<< HEAD:Estruturas de Repetição/Ativ07.py
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

inicio = min(num1, num2)
fim = max(num1, num2)

print(f"\nNúmeros no intervalo entre {inicio} e {fim}:")

for i in range(inicio + 1, fim):
  print(i)
=======
n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o segundo número "))

for i in range (n1, n2+1):
    print(i)