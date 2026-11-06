'''
Faça um programa para uma loja de tintas. Peça a 
área a ser pintada, em metros quadrados. Considere
que 1 litro de tinta cobre 3 m² e que cada lata
contém 18 litros e custa R$ 80,00. Informe quan-
tas latas inteiras devem ser compradas e o preço
total. Arredonde a quantidade de latas para cima.
Resposta / código:
'''
area = float(input("Digite a área a ser pintada (em m²): "))

litros_necessarios = area / 3

latas = math.ceil(litros_necessarios / 18)

preco_total = latas * 80

print(f"\nQuantidade de latas a serem compradas: {latas}")
print(f"Preço total: R$ {preco_total:.2f}")
