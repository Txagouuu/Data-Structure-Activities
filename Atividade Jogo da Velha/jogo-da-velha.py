import random
import time

def inicializarTabuleiro():
    """Cria e retorna uma matriz 3x3 preenchida com espaços vazios."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def exibirTabuleiro(tabuleiro):
    """Exibe o tabuleiro formatado com coordenadas de 1 a 3."""
    print("\n         Colunas")
    print("        1   2   3")
    print("      +---+---+---+")
    for i in range(3):
        print(f"  {i+1}   | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
        print("      +---+---+---+")
    print()

def sortearQuemComeca():
    """Sorteia e retorna 'X' (Jogador) ou 'O' (Computador)."""
    return random.choice(['X', 'O'])

def posicaoValida(linha, coluna):
    """Verifica se a linha e a coluna estão entre 1 e 3."""
    return 1 <= linha <= 3 and 1 <= coluna <= 3

def posicaoVazia(tabuleiro, linha, coluna):
    """Verifica se a posição escolhida está vazia. Subtrai 1 para o índice da matriz."""
    return tabuleiro[linha-1][coluna-1] == ' '

def jogadaDoJogador(tabuleiro):
    """Gerencia a entrada de dados do jogador e as validações."""
    while True:
        try:
            print("Sua vez!")
            linha = int(input("Informe a linha (1-3): "))
            coluna = int(input("Informe a coluna (1-3): "))
            
            if not posicaoValida(linha, coluna):
                print("Posição inválida. A linha e a coluna devem estar entre 1 e 3.\n")
                continue
                
            if not posicaoVazia(tabuleiro, linha, coluna):
                print("Posição ocupada. Escolha outra posição.\n")
                continue
                
            tabuleiro[linha-1][coluna-1] = 'X'
            break
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.\n")

def jogadaDoComputador(tabuleiro):
    """Sorteia aleatoriamente uma posição até encontrar uma vazia."""
    print("Vez do computador (O)...")
    time.sleep(1) # Pequena pausa para simular o "pensamento"
    while True:
        linha = random.randint(1, 3)
        coluna = random.randint(1, 3)
        
        if posicaoVazia(tabuleiro, linha, coluna):
            tabuleiro[linha-1][coluna-1] = 'O'
            print(f"O computador jogou na posição: linha {linha}, coluna {coluna}.")
            break

def verificarLinhas(tabuleiro, simbolo):
    for i in range(3):
        if tabuleiro[i][0] == simbolo and tabuleiro[i][1] == simbolo and tabuleiro[i][2] == simbolo:
            return True
    return False

def verificarColunas(tabuleiro, simbolo):
    for j in range(3):
        if tabuleiro[0][j] == simbolo and tabuleiro[1][j] == simbolo and tabuleiro[2][j] == simbolo:
            return True
    return False

def verificarDiagonais(tabuleiro, simbolo):
    # Diagonal principal
    if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
        return True
    # Diagonal secundária
    if tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:
        return True
    return False

def verificarVitoria(tabuleiro, simbolo):
    """Verifica se o símbolo atingiu alguma condição de vitória."""
    return verificarLinhas(tabuleiro, simbolo) or \
           verificarColunas(tabuleiro, simbolo) or \
           verificarDiagonais(tabuleiro, simbolo)

def tabuleiroCheio(tabuleiro):
    """Verifica se não existem mais espaços vazios no tabuleiro."""
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    return True

def jogar():
    """Função principal que controla o fluxo da partida."""
    print("="*35)
    print("      JOGO DA VELHA BÁSICO")
    print("="*35)
    
    tabuleiro = inicializarTabuleiro()
    turno_atual = sortearQuemComeca()
    
    if turno_atual == 'X':
        print("O jogador X começará a partida.")
    else:
        print("O computador O começará a partida.")
        
    exibirTabuleiro(tabuleiro)
    
    while True:
        if turno_atual == 'X':
            jogadaDoJogador(tabuleiro)
            if verificarVitoria(tabuleiro, 'X'):
                exibirTabuleiro(tabuleiro)
                print("O jogador X venceu a partida!")
                break
            turno_atual = 'O'
            
        else:
            jogadaDoComputador(tabuleiro)
            if verificarVitoria(tabuleiro, 'O'):
                exibirTabuleiro(tabuleiro)
                print("O computador O venceu a partida!")
                break
            turno_atual = 'X'
            
        exibirTabuleiro(tabuleiro)
        
        if tabuleiroCheio(tabuleiro):
            print("A partida terminou empatada.")
            break

# Ponto de entrada do programa
if __name__ == "__main__":
    jogar()