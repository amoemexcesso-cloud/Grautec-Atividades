'''
Tendo como dado de entrada o tamanho de um arquivo
em gigabytes, construa um algoritmo que faça a con-
versão para megabytes.
Fórmula: MB = GB × 1024.
Resposta / código:
'''
tamanho = float(input("Digite o tamanho do arquivo em gigabyte: "))
megabytes = int(tamanho * 1024)
print(f"O tamanho do arquivo em megabytes é: {megabytes}")