'''
Faça um programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = input("Insira uma letra: ")

if letra not in "aeiou":
    print("Consoante")

else:
    print("vogal")