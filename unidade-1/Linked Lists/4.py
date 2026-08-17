class Tipo_LUE_Matricial:
    """Nó para Lista Simplesmente Encadeada em Vetor (Matricial)."""
    def __init__(self, info, elo=-1):
        self.info = info
        self.elo = elo

def intercalar_ordenadas_matricial(vetor, comeco_a, comeco_b):
    if comeco_a == -1: return comeco_b
    if comeco_b == -1: return comeco_a

    # Define quem será o primeiro elemento da lista C
    if vetor[comeco_a].info <= vetor[comeco_b].info:
        comeco_c = comeco_a
        atual_a = vetor[comeco_a].elo
        atual_b = comeco_b
    else:
        comeco_c = comeco_b
        atual_a = comeco_a
        atual_b = vetor[comeco_b].elo

    atual_c = comeco_c

    # Percorre ambas as listas intercalando
    while atual_a != -1 and atual_b != -1:
        if vetor[atual_a].info <= vetor[atual_b].info:
            vetor[atual_c].elo = atual_a
            atual_c = atual_a
            atual_a = vetor[atual_a].elo
        else:
            vetor[atual_c].elo = atual_b
            atual_c = atual_b
            atual_b = vetor[atual_b].elo

    # Anexa o restante da lista que não chegou ao fim
    if atual_a != -1:
        vetor[atual_c].elo = atual_a
    else:
        vetor[atual_c].elo = atual_b

    return comeco_c

# --- TESTE EXERCÍCIO 4 ---
# Lista A: 1(idx 0) -> 5(idx 1) -> 9(idx 2)
# Lista B: 2(idx 3) -> 6(idx 4)
vetor_ex4 = [
    Tipo_LUE_Matricial(1, 1), Tipo_LUE_Matricial(5, 2), Tipo_LUE_Matricial(9, -1),
    Tipo_LUE_Matricial(2, 4), Tipo_LUE_Matricial(6, -1)
]
novo_comeco_c = intercalar_ordenadas_matricial(vetor_ex4, 0, 3)
atual = novo_comeco_c
print("Ex 4 - Lista intercalada ordenada:", end=" ")
while atual != -1:
    print(vetor_ex4[atual].info, end=" -> ")
    atual = vetor_ex4[atual].elo
print("FIM")