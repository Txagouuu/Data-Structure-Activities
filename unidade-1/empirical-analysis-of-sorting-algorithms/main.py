import time
import random

def algoritmo_ordenacao(vetor):
    """
    Substitua o conteúdo desta função pelo algoritmo ensinado em sala de aula
    (Ex: Bubble Sort, Selection Sort). O padrão aqui é o Insertion Sort.
    """
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave

def main():
    print("="*85)
    print(" ANÁLISE DE DESEMPENHO DE ALGORITMO DE ORDENAÇÃO ".center(85))
    print("="*85)
    
    # 1. Entrada de Dados
    try:
        n_max = int(input("Digite o tamanho máximo do vetor (N) [ex: 2000]: "))
        salto = int(input("Digite o intervalo de saltos (ex: 500): "))
        m_amostras = int(input("Digite a qtde de amostras para o cenário aleatório (M): "))
    except ValueError:
        print("\nErro: Por favor, insira apenas números inteiros válidos.")
        return

    print("\nExecutando os testes... (Isso pode levar alguns segundos dependendo de N e M)\n")

    # Cabeçalho da Tabela
    print("-" * 85)
    print(f"{'Tamanho do Vetor':<18} | {'Crescente (s)':<18} | {'Decrescente (s)':<20} | {'Aleatório (Tempo Médio)':<22}")
    print("-" * 85)

    # 2. Cenários de Teste variando o tamanho do vetor
    for tamanho in range(salto, n_max + 1, salto):
        
        # Cenário A: Crescente (já ordenado)
        vetor_crescente = list(range(tamanho))
        inicio = time.perf_counter()
        algoritmo_ordenacao(vetor_crescente)
        tempo_crescente = time.perf_counter() - inicio

        # Cenário B: Decrescente (invertido)
        vetor_decrescente = list(range(tamanho, 0, -1))
        inicio = time.perf_counter()
        algoritmo_ordenacao(vetor_decrescente)
        tempo_decrescente = time.perf_counter() - inicio

        # Cenário C: Aleatório (Média de M execuções)
        tempo_total_aleatorio = 0
        for _ in range(m_amostras):
            # Gera um novo vetor aleatório para cada amostra
            vetor_aleatorio = [random.randint(0, tamanho) for _ in range(tamanho)]
            
            inicio = time.perf_counter()
            algoritmo_ordenacao(vetor_aleatorio)
            tempo_total_aleatorio += (time.perf_counter() - inicio)
            
        tempo_medio_aleatorio = tempo_total_aleatorio / m_amostras

        # 3. Saída Esperada (Impressão da linha da tabela)
        print(f"{tamanho:<18} | {tempo_crescente:<18.6f} | {tempo_decrescente:<20.6f} | {tempo_medio_aleatorio:<22.6f}")

    print("-" * 85)
    print("\nAnálise concluída com sucesso!")

if __name__ == "__main__":
    main()