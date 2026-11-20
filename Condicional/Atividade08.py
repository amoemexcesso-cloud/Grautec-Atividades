'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:
'''
preco1 = float(input("Qual o Preço 1: "))
preco2 = float(input("Qual o Preço 2: "))
preco3 = float(input("Qual o Preço 3: "))

menor_preco = min(preco1, preco2, preco3)
print(f"Você deve comprar o produto que custa R$ {menor_preco:.2f}")
