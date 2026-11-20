'''
João, um pescador, precisa controlar o peso dos 
peixes pescados. O limite estabelecido é de 50 kg. 
Para cada quilo excedente, é cobrada uma multa de 
R$ 4,00. Faça um programa que leia o peso total 
dos peixes, calcule quantos quilos ultrapassaram 
o limite e o valor da multa. Se não houver excesso,
a multa será zero. Mostre os resultados com mensa
gens adequadas.
Resposta / código:
'''
peso_total = float(input("Digite o peso total dos peixes: "))

limite = 50
taxa_multa_por_quilo = 4.00

if peso_total > limite:
    excesso = peso_total - limite
    multa = excesso * taxa_multa_por_quilo
else:
    excesso = 0.0
    multa = 0.0

print("--- Relatório de Pesca ---")
print(f"Peso total: {peso_total:.2f} kg")
print(f"Quilos excedentes: {excesso:.2f} kg")
print(f"Valor da multa: R$ {multa:.2f}")