'''
Faça um programa que pergunte quanto você ganha 
por hora e quantas horas trabalhou no mês. Calcule
 o salário bruto e os descontos de Imposto de Ren-
 da (11%), INSS (8%) e sindicato (5%). Mostre os 
 valores de cada item e o salário líquido, usando 
 o modelo:

+ Salário Bruto: R$ ...
− IR (11%): R$ ...
− INSS (8%): R$ ...
− Sindicato (5%): R$ ...
= Salário Líquido: R$ …

Salário líquido = salário bruto − total dos descontos.
Resposta / código:
'''
hora_por_dia = float(input("Digite o valor da Hora: R$ "))
total_horas_mes = int(input("quantas horas trabalhou no mês "))

sl_bruto = hora_por_dia * total_horas_mes
ir = -(sl_bruto * 0.11)
inss = -(sl_bruto * 0.08)
sindicato = -(sl_bruto * 0.05)

total_descontos = ir + inss + sindicato

print("---Holerite---")
print(f"Salário Bruto: R$ {sl_bruto:.2f}")
print(f"ir: R$ {ir:.2f}")
print(f"inss: R$ {inss:.2f}")
print(f"sindicato: R$ {sindicato:.2f}")
print(f"Total de Descontos: R$ {-total_descontos:.2f}")
print(f"Total Liquido: R$ {sl_bruto -- total_descontos:.2f}")
