import random
import time

def numero_ja_existe(vetor, numero):
    return numero in vetor

def preencher_vetor_v1(N):
    vetor = []
    colisoes = 0
    sorteios = 0
    
    inicio = time.perf_counter()
    
    while len(vetor) < N:
        numero = random.randint(1, N)
        sorteios += 1
        
        if numero_ja_existe(vetor, numero):
            colisoes += 1
        else:
            vetor.append(numero)
            
    fim = time.perf_counter()
    tempo_execucao = fim - inicio
    
    return vetor, sorteios, colisoes, tempo_execucao

def preencher_vetor_v2(N):
    vetor = list(range(1, N + 1)) 
    
    inicio = time.perf_counter()
    
    # 2. Embaralha usando Fisher-Yates
    for i in range(N - 1, 0, -1):
        # Sorteia um índice válido de 0 até i
        j = random.randint(0, i)
        # Troca os elementos de posição
        vetor[i], vetor[j] = vetor[j], vetor[i]
        
    fim = time.perf_counter()
    tempo_execucao = fim - inicio
    
    return vetor, tempo_execucao

# Execução da Versão 1
N = int(input("Informe o valor de N: "))

if N > 0:
    vetor_v1, sorteios, colisoes, tempo = preencher_vetor_v1(N)
    print("\n--- RESULTADOS VERSÃO 1 ---")
    #print(f"Vetor gerado: {vetor_v1}")
    print(f"Quantidade de números sorteados: {sorteios}")
    print(f"Quantidade de números armazenados: {N}")
    print(f"Quantidade de colisões: {colisoes}")
    print(f"Tempo de execução: {tempo:.6f} segundos")

# Execução da Versão 2
if N > 0:
    vetor_v2, tempo_v2 = preencher_vetor_v2(N)
    print("\n--- RESULTADOS VERSÃO 2 ---")
    # print(f"Vetor gerado: {vetor_v2}")
    print(f"Quantidade de números armazenados: {N}")
    print(f"Quantidade de colisões: 0")
    print(f"Tempo de execução: {tempo_v2:.6f} segundos")