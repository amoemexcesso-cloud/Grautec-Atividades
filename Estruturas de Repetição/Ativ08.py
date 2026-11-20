'''
Altere o programa anterior para mostrar no final a soma dos números.
'''
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

inicio = min(num1, num2)
fim = max(num1, num2)

print(f"\nNúmeros no intervalo entre {inicio} e {fim}:")

soma = 0

for i in range(inicio + 1, fim):
  print(i)
  soma += i  # Adiciona o número atual à soma total

print(f"\nA soma de todos os números do intervalo é: {soma}")
