'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

nota1 = float(input("Digite a Primeira Nota: "))
nota2 = float(input("Digite a Segunda Nota: "))

media = (nota1 + nota2) / 2

print("A média do Aluno(a) é:", media)

if media == 10.0:
    print("Aprovado com Distinção")
elif media >= 7.0:
    print("O Aluno foi Aprovado, Parabéns")
else:
    print("O aluno foi Reprovado")

