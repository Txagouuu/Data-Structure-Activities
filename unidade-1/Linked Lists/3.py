class Tipo_LUE_Matricial:
    """Nó para Lista Simplesmente Encadeada em Vetor (Matricial)."""
    def __init__(self, info, elo=-1):
        self.info = info
        self.elo = elo

def primeiro_ausente(vetor, comeco_a, comeco_b):
    atual_a = comeco_a
    
    while atual_a != -1:
        valor_a = vetor[atual_a].info
        
        # Busca o valor_a na lista B
        atual_b = comeco_b
        encontrado_em_b = False
        
        while atual_b != -1:
            if vetor[atual_b].info == valor_a:
                encontrado_em_b = True
                break
            atual_b = vetor[atual_b].elo
            
        if not encontrado_em_b:
            return valor_a
            
        atual_a = vetor[atual_a].elo
        
    return None # Retorna None se todos de A estiverem em B

# --- TESTE EXERCÍCIO 3 ---
# Lista A: 10(idx 0) -> 20(idx 1) -> 30(idx 2)
# Lista B: 10(idx 3) -> 40(idx 4) -> 20(idx 5)
vetor_ex3 = [
    Tipo_LUE_Matricial(10, 1), Tipo_LUE_Matricial(20, 2), Tipo_LUE_Matricial(30, -1),
    Tipo_LUE_Matricial(10, 4), Tipo_LUE_Matricial(40, 5), Tipo_LUE_Matricial(20, -1)
]
print(f"Ex 3 - Primeiro ausente de A em B: {primeiro_ausente(vetor_ex3, 0, 3)}") 
# Saída esperada: 30