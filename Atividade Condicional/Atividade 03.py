'''
Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminino
M - Masculino
Sexo Inválido.
'''
letra = input("qual seu gênero F ou M: ")

if letra == "F":
    print("Feminino")
elif letra == "M":
    print("Masculno")
else:
    print("sexo inválido")
