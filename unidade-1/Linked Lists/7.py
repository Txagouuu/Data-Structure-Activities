class Tipo_LDE_Dinamica:
    """Nó para Lista Duplamente Encadeada com Alocação Dinâmica."""
    def __init__(self, info):
        self.info = info
        self.elop = None  # Elo Próximo
        self.eloa = None  # Elo Anterior

        
def concatenar_lde_dinamica(comeco_a, comeco_b):
    if comeco_a is None:
        return comeco_b
    if comeco_b is None:
        return comeco_a

    atual = comeco_a
    # Percorre até encontrar o último nó de A
    while atual.elop is not None:
        atual = atual.elop

    # Conecta as listas nas duas direções
    atual.elop = comeco_b
    comeco_b.eloa = atual

    return comeco_a

# --- TESTE EXERCÍCIO 7 ---
n1 = Tipo_LDE_Dinamica("X")
n2 = Tipo_LDE_Dinamica("Y")
novo_comeco_lde = concatenar_lde_dinamica(n1, n2)
atual = novo_comeco_lde
print("Ex 7 - LDE concatenada:", end=" ")
while atual is not None:
    print(atual.info, end=" <-> ")
    atual = atual.elop
print("NULO")