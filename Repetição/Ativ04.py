'''
Faça um programa que leia 5 números e informe o maior número.
'''
# 1. Você precisa criar a variável soma antes de começar o loop
soma = 0

for i in range(1, 8):
    numero = float(input(f"Digite o {i}º número: "))
    
    # 2. Para somar o número atual, use: soma = soma + numero (ou soma += numero)
    soma = soma + numero 

# Fora do loop, exibe o resultado
print(f"\nA soma dos números é: {soma}")
