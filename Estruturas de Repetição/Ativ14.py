'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''
def resolver_euler_14():
    limite = 1000000
    # Dicionário de cache para guardar o comprimento já calculado de cada número
    cache = {1: 1}
    
    maior_comprimento = 0
    numero_vencedor = 0
    
    for i in range(1, limite):
        n = i
        caminho = []
        
        # Percorre a sequência até encontrar um número já calculado no cache
        while n not in cache:
            caminho.append(n)
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        
        # Recupera o comprimento do número que parou no cache
        comprimento_atual = cache[n]
        
        # Preenche o cache de trás para frente com os novos números descobertos
        for elemento in reversed(caminho):
            comprimento_atual += 1
            cache[elemento] = comprimento_atual
            
        # Atualiza o maior valor encontrado
        if cache[i] > maior_comprimento:
            maior_comprimento = cache[i]
            numero_vencedor = i
            
    print(f"Número: {numero_vencedor}")
    print(f"Termos: {maior_comprimento}")

resolver_euler_14()

