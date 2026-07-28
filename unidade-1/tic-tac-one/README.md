# RELATÓRIO DE ATIVIDADE PRÁTICA / ESTUDO INDEPENDENTE

**Disciplina:** Estrutura de Dados  
**Estudante(s):** [Tiago Andrei de Almeida Mendonça]  
**Atividade:** [Atividade Diagnóstica - Jogo da Velha]  
**Data de Entrega:** [27/07/2026]  

---

## 1. Descrição da Solução

[Escreva sua descrição aqui. Ex: "Desenvolvimento de um Jogo da Velha básico utilizando matrizes 3x3 em Python, com jogadas aleatórias do computador e validação de coordenadas."]

## 2. Instruções de Compilação e Execução

* **Linguagem / Ambiente:** [Ex: Python 3.10]
* **Como executar:** [Ex: "Abra o terminal na pasta do arquivo e digite `python jogo_da_velha.py`. O programa rodará diretamente no console."]


### 3. Respostas às Questões para Reflexão

1. **Como o tabuleiro foi representado na memória?**
   O tabuleiro foi representado na memória por meio de uma estrutura de matriz bidimensional. Em Python, isso foi implementado utilizando uma lista de listas com dimensões $3 \times 3$, onde cada sublista representa uma linha do tabuleiro.

2. **Qual valor foi utilizado para identificar uma posição vazia?**
   Foi utilizado o caractere de espaço em branco (`' '`).

3. **Como foi realizado o sorteio de quem começa?**
   O sorteio foi realizado utilizando a biblioteca padrão de aleatoriedade (em Python, a função `random.choice(['X', 'O'])`). Essa função escolhe pseudoaleatoriamente um dos elementos fornecidos, garantindo $50\%$ de probabilidade para cada participante iniciar a partida.

4. **Como o computador garante que não jogará em uma posição ocupada?**
   O computador utiliza uma estrutura de repetição (`while`). Ele sorteia aleatoriamente as coordenadas de linha e coluna; em seguida, chama a função `posicaoVazia` para verificar se a célula sorteada contém o caractere vazio (`' '`). Se a posição estiver ocupada, a condição falha e o laço repete o sorteio até encontrar e preencher uma posição livre.

5. **Como o programa identifica que o tabuleiro está cheio?**
   Por meio da função `tabuleiroCheio`, que varre toda a matriz do jogo. Ela percorre cada linha e verifica se o caractere vazio (`' '`) ainda está presente em alguma célula. Se a matriz for totalmente percorrida sem encontrar espaços em branco, a função conclui que o tabuleiro está cheio (o que, caso não haja vencedor, indica empate).

6. **Como foram verificadas as linhas, colunas e diagonais?**
   As verificações foram feitas acessando diretamente os índices correspondentes da matriz $3 \times 3$ e comparando-os com o símbolo do jogador atual (`'X'` ou `'O'`). Por exemplo, para verificar uma linha, o programa checa se as colunas 0, 1 e 2 daquela linha específica contêm o mesmo símbolo simultaneamente. O mesmo princípio posicional foi aplicado para colunas e diagonais (principal e secundária).

7. **Que alterações seriam necessárias para utilizar um tabuleiro de tamanho diferente?**
   * Modificar a etapa de inicialização para gerar uma matriz de dimensão $N \times N$.
   * Alterar os limites das validações das entradas do usuário e do sorteio aleatório do computador (passando a aceitar de $1$ a $N$).
   * Refatorar as funções de verificação de vitória (linhas, colunas e diagonais). Em vez de checar posições fixas, seria necessário utilizar laços de repetição (como o `for`) para verificar se $N$ elementos consecutivos daquela estrutura são idênticos.

8. **Quais partes da solução poderiam constituir um Tipo Abstrato de Dados (TAD) denominado JogoDaVelha?**
   Um Tipo Abstrato de Dados encapsula dados (estado) e as operações (comportamentos) que manipulam esses dados.
   * **Dados (Estado):** A matriz $3 \times 3$ que armazena o tabuleiro e a variável que controla o turno atual.
   * **Operações (Métodos):** Funções como `inicializarTabuleiro()`, `posicaoValida()`, `inserirJogada()`, `verificarVitoria()`, `tabuleiroCheio()` e `exibirTabuleiro()`.

## 4. Referências Consultadas

* Gemini Pro

---

## 5. Declaração de Uso de Inteligência Artificial

* **Ferramenta utilizada:** Gemini (Google)
* **Finalidade de sua utilização:** Auxílio na estruturação e modularização do código-fonte em Python para o Jogo da Velha, elaboração de uma base para as respostas às questões de reflexão e criação do template de formatação do relatório.
* **Etapas da atividade em que foi empregada:** Desenvolvimento da lógica inicial do programa (criação da matriz, validações e turnos), estruturação do relatório final e revisão teórica das questões de reflexão.
* **Procedimentos adotados para verificar as informações:** Leitura integral do código gerado para compreensão da lógica, execução local no próprio ambiente de desenvolvimento (IDE/Terminal) e realização prática dos casos de teste exigidos pelo roteiro (verificação de posições inválidas, detecção de vitória nas linhas/colunas/diagonais e verificação de empate).
* **Erros, limitações ou inconsistências identificados:** Foi necessário analisar o código para garantir que o computador realmente fizesse apenas jogadas aleatórias (sem tentar vencer ou bloquear o jogador), cumprindo rigorosamente a restrição da Etapa 1 do roteiro. A IA atendeu ao requisito, mas a validação dessa ausência de "estratégia" foi confirmada manualmente durante os testes.
* **Alterações realizadas pelo estudante:** Execução dos testes práticos para a geração dos 2 prints obrigatórios inseridos no relatório, preenchimento dos dados pessoais e revisão final do código para garantir o domínio total sobre a manipulação da matriz 3x3.
* **Indicação das partes do trabalho que receberam apoio da ferramenta:** Código-fonte principal (`jogo_da_velha.py`), base das respostas às questões de reflexão e formatação do arquivo Markdown.