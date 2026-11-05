'''
A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Faça um programa capaz de gerar a série até o n-ésimo termo.
'''
n = int(input("Insira o termo que deseja descobrir: "))
ultimo = 1
penultimo = 1

if n == 1 or n == 2:
    print("1")
else:
    i = 3

    while i <= n: # i = 3
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        i += 1

print(termo)

