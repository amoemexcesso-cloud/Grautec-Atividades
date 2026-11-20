'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
# 1. Inicializamos a lista vazia para guardar os números
numeros = []

# 2. Criamos o loop para ler os 5 números
for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)  # Guarda o número digitado na lista

# 3. Fazemos os cálculos DEPOIS que o loop recolheu todos os números
soma = sum(numeros)      # sum() soma todos os elementos da lista
media = soma / 5         # Agora dividimos o total por 5

# 4. Exibimos o resultado final (usando o 'f' antes das aspas para as variáveis funcionarem)
print(f"\nA soma é {soma} e a média é {media}")