'''
texto = input("Digite uma palavra ou frase: ").lower()
vogais = "aeiouáéíóúãõâêîôû"
total_vogais = 0

# enumerate com start=1 numera cada caractere a partir da posição 1
for posicao, caractere in enumerate(texto, start=1):
    if caractere in vogais:
        total_vogais += 1
        print(f"Vogal '{caractere}' encontrada na posição {posicao}")

print(f"Total de vogais: {total_vogais}")

'''
def somar_tres_numeros(a, b, c):
    resultado = a + b + c
    return resultado

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

total = somar_tres_numeros(n1, n2, n3)

print("A soma dos três números é:", total)