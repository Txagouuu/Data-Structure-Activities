class Tipo_LUE_Matricial:
    """Nó para Lista Simplesmente Encadeada em Vetor (Matricial)."""
    def __init__(self, info, elo=-1):
        self.info = info
        self.elo = elo

def contar_nos_lue_matricial(vetor, comeco):
    contador = 0
    atual = comeco
    while atual != -1:
        contador += 1
        atual = vetor[atual].elo
    return contador

# --- TESTE EXERCÍCIO 1 ---
# Vetor simulando a memória: Lista lógica -> A (índice 0) -> B (índice 2) -> C (índice 1)
vetor_ex1 = [
    Tipo_LUE_Matricial('A', 2),  # Índice 0
    Tipo_LUE_Matricial('C', -1), # Índice 1
    Tipo_LUE_Matricial('B', 1)   # Índice 2
]
print(f"Ex 1 - Total de nós válidos: {contar_nos_lue_matricial(vetor_ex1, 0)}") 
# Saída esperada: 3