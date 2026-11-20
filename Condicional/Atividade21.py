'''
Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''
# Leitura dos dados
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
op = input("Escolha a operação (+, -, *, /): ")

# Cálculo do resultado
if op == "+": resultado = num1 + num2
elif op == "-": resultado = num1 - num2
elif op == "*": resultado = num1 * num2
elif op == "/": resultado = num1 / num2
else: resultado = 0

print(f"\nResultado: {resultado}")

# Verificações diretas
par_impar = "par" if resultado % 2 == 0 else "ímpar"
positivo_negativo = "positivo" if resultado >= 0 else "negativo"
inteiro_decimal = "inteiro" if resultado.is_integer() else "decimal"

# Exibe a frase com as características
print(f"O número é {par_impar}, {positivo_negativo} e {inteiro_decimal}.")
