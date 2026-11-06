'''
Tendo como dado de entrada o tamanho de um arquivo
em gigabytes, construa um algoritmo que faça a con-
versão para megabytes e kilobytes. Mostre os dois
resultados.
Fórmulas: MB = GB × 1024; KB = GB × 1024 × 1024.
Resposta / código:
'''
tamanho = float(input("Digite o tamanho do arquivo em gigabyte: "))
resultado_mb = (tamanho * 1024)
resultado_kb = (resultado_mb * 1024)

print("--- Resultados ---")
print(f"O valor em Megabytes é: {resultado_mb}")
print(f"O valor em Kilobytes é: {resultado_kb}")
