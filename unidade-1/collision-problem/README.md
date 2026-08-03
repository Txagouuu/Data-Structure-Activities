### 3.4 Critério adicional

* **Todos os números podem ocupar qualquer posição?**
Sim. A lógica de troca do algoritmo garante que qualquer número presente no vetor tem a chance de ser movido para qualquer índice.
* **Todas as posições podem receber qualquer número?**
Sim. A matemática do embaralhamento garante que toda posição tem exatamente a mesma probabilidade de receber qualquer um dos números disponíveis.
* **O método utilizado favorece alguma posição?**
Não. O embaralhamento utilizado (algoritmo de Fisher-Yates) é neutro e perfeitamente uniforme, não criando viés de probabilidade para nenhuma parte do vetor.
* **O número de operações depende da sorte ou é previamente limitado?**
É previamente limitado. Independentemente da sorte, o algoritmo sempre executará exatamente um número fixo de operações de inserção (N) e operações de troca (N - 1), garantindo um tempo de execução constante e previsível.

---

## 4. COMPARAÇÃO ENTRE AS VERSÕES

As duas versões deverão ser executadas com os mesmos valores de N.

**Resultados dos testes (Média de 5 execuções):**

| N | Colisões da versão 1 | Tempo da versão 1 | Tempo da versão 2 |
| --- | --- | --- | --- |
| **10** | 18 | 0,000021 s | 0,000006 s |
| **100** | 421 | 0,000485 s | 0,000045 s |
| **1.000** | 6.482 | 0,028100 s | 0,000480 s |
| **10.000** | 87.954 | 1,852000 s | 0,004900 s |
| **100.000** | 1.109.135 | 172,450000 s | 0,051200 s |


---

## 5. QUESTÕES PARA ANÁLISE

**1. Por que a primeira versão produz colisões?**
Porque o sorteio aleatório não guarda memória dos valores já gerados. O programa sorteia um número usando sempre o intervalo total de 1 a N, permitindo que um valor que já está armazenado no vetor seja escolhido novamente.

**2. O número de colisões aumenta quando N cresce?**
Sim, e aumenta de forma expondecial. Conforme N se torna muito grande, o espaço "livre" no vetor demora mais para ser preenchido, exigindo que o programa descarte cada vez mais sorteios repetidos antes de encontrar um espaço no vetor.

**3. Por que as últimas posições tendem a exigir mais sorteios?**
Pois a probabilidade de sortear um número que ainda não foi diminui progressivamente. Para preencher a última posição do vetor, N - 1 números já foram usados. Isso significa que a chance de o gerador aleatório acertar exatamente o único número que falta é de apenas 1 em N, causando uma enorme quantidade de colisões antes do acerto.

**4. É possível determinar previamente quantos sorteios a primeira versão realizará?**
Não é possível determinar com exatidão, pois o resultado depende do acaso inerente à geração pseudoaleatória. No entanto, é possível prever uma *média estatística*, mas o número exato de sorteios varia a cada execução.

**5. Quantas operações principais são realizadas na segunda versão?**
A segunda versão executa um número exato e invariável de operações: N inserções seguidas de N - 1 operações de troca.

**6. Qual versão apresentou menor tempo?**
A Versão 2 apresentou um tempo menor. A diferença entre as duas lógicas torna-se grande à medida que N cresce, provando que a Versão 2 é mais otimizado.

**7. A segunda versão elimina completamente as repetições?**
Sim. Como o vetor inicial é preenchido com valores únicos e o algoritmo apenas troca a posição desses valores dentro do próprio vetor, é matematicamente impossível ocorrer a duplicação de um número.

**8. Como o estudante garantiu que nenhum número foi perdido?**
 Todos os números de 1 a N foram inseridos ordenadamente. O algoritmo subsequente apenas manipula os índices para realizar permutações, sem apagar valores ou inserir dados externos, preservando todos os números iniciais.

**9. A estratégia criada gera sempre a mesma sequência?**
Não. Como os índices escolhidos para realizar as trocas são selecionados de forma pseudoaleatória em cada repetição do laço, o resultado final da permutação será diferente a cada nova execução do programa.

**10. Qual das duas soluções é mais adequada para valores elevados de N?**
A Versão 2 é a única solução adequada para valores elevados. A Versão 1 possui uma complexidade de tempo muito alto, que trava o sistema em amostras maiores. Já a Versão 2 possui eficiência linear, mantendo o alto desempenho e o tempo de resposta baixo mesmo para conjuntos de dados massivos.

## 5. Declaração de Uso de Inteligência Artificial

* **Ferramenta utilizada:** Gemini (Google)
* **Finalidade de sua utilização:** Auxílio na estruturação e modularização do código-fonte em Python para o Jogo da Velha, elaboração de uma base para as respostas às questões de reflexão e criação do template de formatação do relatório.
* **Etapas da atividade em que foi empregada:** Desenvolvimento da lógica inicial do programa (criação da matriz, validações e turnos), estruturação do relatório final e revisão teórica das questões de reflexão.
* **Procedimentos adotados para verificar as informações:** Leitura integral do código gerado para compreensão da lógica, execução local no próprio ambiente de desenvolvimento (IDE/Terminal) e realização prática dos casos de teste exigidos pelo roteiro (verificação de posições inválidas, detecção de vitória nas linhas/colunas/diagonais e verificação de empate).
* **Erros, limitações ou inconsistências identificados:** Foi necessário analisar o código para garantir que o computador realmente fizesse apenas jogadas aleatórias (sem tentar vencer ou bloquear o jogador), cumprindo rigorosamente a restrição da Etapa 1 do roteiro. A IA atendeu ao requisito, mas a validação dessa ausência de "estratégia" foi confirmada manualmente durante os testes.
* **Alterações realizadas pelo estudante:** Execução dos testes práticos para a geração dos 2 prints obrigatórios inseridos no relatório, preenchimento dos dados pessoais e revisão final do código para garantir o domínio total sobre a manipulação da matriz 3x3.
* **Indicação das partes do trabalho que receberam apoio da ferramenta:** Código-fonte principal (`main.py`) para a contrução da primeira versão.