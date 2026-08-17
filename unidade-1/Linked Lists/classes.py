# --- ESTRUTURAS DINÂMICAS ---
class Tipo_LUE_Dinamica:
    """Nó para Lista Simplesmente Encadeada com Alocação Dinâmica."""
    def __init__(self, info):
        self.info = info
        self.elo = None

class Tipo_LDE_Dinamica:
    """Nó para Lista Duplamente Encadeada com Alocação Dinâmica."""
    def __init__(self, info):
        self.info = info
        self.elop = None  # Elo Próximo
        self.eloa = None  # Elo Anterior

class Tipo_Polinomio:
    """Nó para armazenar os termos de um polinômio em LDE."""
    def __init__(self, a, i):
        self.a = a  # Coeficiente
        self.i = i  # Expoente
        self.elop = None
        self.eloa = None