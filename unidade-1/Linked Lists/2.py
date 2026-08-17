class Tipo_LUE_Matricial:
    """Nó para Lista Simplesmente Encadeada em Vetor (Matricial)."""
    def __init__(self, info, elo=-1):
        self.info = info
        self.elo = elo


def concatenar_lue_matricial(vetor, comeco_a, comeco_b):
    if comeco_a == -1:
        return comeco_b
    
    atual = comeco_a
    # Avança até o último nó da lista A
    while vetor[atual].elo != -1:
        atual = vetor[atual].elo
        
    # Conecta o final de A ao começo de B
    vetor[atual].elo = comeco_b
    return comeco_a

# --- TESTE EXERCÍCIO 2 ---
# Lista A (índice 0 -> 1), Lista B (índice 2 -> 3)
vetor_ex2 = [
    Tipo_LUE_Matricial('A1', 1), Tipo_LUE_Matricial('A2', -1),
    Tipo_LUE_Matricial('B1', 3), Tipo_LUE_Matricial('B2', -1)
]
novo_comeco = concatenar_lue_matricial(vetor_ex2, 0, 2)
atual = novo_comeco
print("Ex 2 - Lista concatenada:", end=" ")
while atual != -1:
    print(vetor_ex2[atual].info, end=" -> ")
    atual = vetor_ex2[atual].elo
print("FIM")