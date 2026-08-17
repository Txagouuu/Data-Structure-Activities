class Tipo_LDE_Dinamica:
    """Nó para Lista Duplamente Encadeada com Alocação Dinâmica."""
    def __init__(self, info):
        self.info = info
        self.elop = None  # Elo Próximo
        self.eloa = None  # Elo Anterior

def inverter_lde_dinamica(comeco):
    atual = comeco
    novo_comeco = None
    
    while atual is not None:
        # Troca os ponteiros anterior e próximo
        temp = atual.elop
        atual.elop = atual.eloa
        atual.eloa = temp
        
        # Atualiza o novo começo a cada iteração (o último nó válido será o retorno)
        novo_comeco = atual
        atual = temp  # 'temp' guarda o que antes era o próximo nó
        
    return novo_comeco

# --- TESTE EXERCÍCIO 6 ---
n1 = Tipo_LDE_Dinamica("A")
n2 = Tipo_LDE_Dinamica("B")
n1.elop = n2; n2.eloa = n1

comeco_lde_inv = inverter_lde_dinamica(n1)
atual = comeco_lde_inv
print("Ex 6 - LDE invertida:", end=" ")
while atual is not None:
    print(atual.info, end=" <-> ")
    atual = atual.elop
print("NULO")