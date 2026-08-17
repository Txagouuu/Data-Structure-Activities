class Tipo_LUE_Dinamica:
    """Nó para Lista Simplesmente Encadeada com Alocação Dinâmica."""
    def __init__(self, info):
        self.info = info
        self.elo = None

def inverter_lue_dinamica(comeco):
    anterior = None
    atual = comeco
    
    while atual is not None:
        proximo = atual.elo
        atual.elo = anterior
        anterior = atual
        atual = proximo
        
    return anterior  # O último nó (anterior) é o novo começo

# --- TESTE EXERCÍCIO 5 ---
n1 = Tipo_LUE_Dinamica(1)
n2 = Tipo_LUE_Dinamica(2)
n3 = Tipo_LUE_Dinamica(3)
n1.elo = n2; n2.elo = n3

comeco_invertido = inverter_lue_dinamica(n1)
atual = comeco_invertido
print("Ex 5 - LUE invertida:", end=" ")
while atual is not None:
    print(atual.info, end=" -> ")
    atual = atual.elo
print("NULO")