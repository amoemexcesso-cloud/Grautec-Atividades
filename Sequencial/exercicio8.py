'''
Faça um programa que pergunte quanto você ganha por
hora e o número de horas trabalhadas no mês. 
Calcule e mostre o salário total do mês.
Resposta / código:
'''
hora = float(input("Insira o valor da Hora: "))
'''
Horas Trabalhadas
'''
ht = float(input("Insira quantas horas foram trabalhadas: "))
dia = hora * ht
mes = dia * 30
print(mes)
