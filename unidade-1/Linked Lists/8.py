class Tipo_Polinomio:
    """Nó para armazenar os termos de um polinômio em LDE."""
    def __init__(self, a, i):
        self.a = a  # Coeficiente
        self.i = i  # Expoente
        self.elop = None
        self.eloa = None

def avaliar_polinomio(comeco_polinomio, x):
    resultado = 0
    atual = comeco_polinomio
    
    while atual is not None:
        # Ai * x^i
        resultado += atual.a * (x ** atual.i)
        atual = atual.elop
        
    return resultado

# --- TESTE EXERCÍCIO 8 ---
# Representando P(x) = 3x^2 + 2x^1 + 5x^0
# Se x = 2, P(2) = 3(4) + 2(2) + 5 = 12 + 4 + 5 = 21
t1 = Tipo_Polinomio(a=3, i=2)
t2 = Tipo_Polinomio(a=2, i=1)
t3 = Tipo_Polinomio(a=5, i=0)
t1.elop = t2; t2.eloa = t1
t2.elop = t3; t3.eloa = t2

valor_x = 2
resultado = avaliar_polinomio(t1, valor_x)
print(f"Ex 8 - Valor do polinômio P({valor_x}) = {resultado}")
# Saída esperada: 21