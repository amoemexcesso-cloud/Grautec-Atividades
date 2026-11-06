'''
Faça um programa que peça dois números inteiros e 
um número real. Calcule e mostre:
• o produto do dobro do primeiro pela metade do 
segundo;
• a soma do triplo do primeiro com o terceiro;
• o terceiro número elevado ao cubo.
Resposta / código:
'''
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num_real = float(input("Digite um número real: "))
resultado_1 = (num1 * 2) * (num2 / 2)
resultado_2 = (num1 * 3) + num_real
resultado_3 = num_real**3

print("--- Resultados ---")
print(f"O produto do dobro do primeiro pela metade do segundo: {resultado_1}")
print(f"A soma do triplo do primeiro com o terceiro: {resultado_2}")
print(f"O terceiro número elevado ao cubo: {resultado_3:.3f}")






