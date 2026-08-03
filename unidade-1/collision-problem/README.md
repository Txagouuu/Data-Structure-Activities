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

## 6. Declaração de Uso de Inteligência Artificial

* **Ferramenta utilizada:** Gemini (Google)
* **Finalidade de sua utilização:** Auxílio na estruturação dos códigos em Python para a geração dos vetores e medição de tempo, compreensão matemática das colisões e formatação do relatório final em Markdown.
* **Etapas da atividade em que foi empregada:** Refinamento da lógica de medição de performance (`time.perf_counter`), estruturação da tabela comparativa e embasamento teórico para as respostas às questões de análise (realizado após a etapa de reflexão inicial do desafio).
* **Procedimentos adotados para verificar as informações:** Execução exaustiva dos códigos no ambiente de desenvolvimento local utilizando os valores de N exigidos (10 a 100.000). Realização de repetições dos testes (mínimo de 5 vezes para cada valor de N) para garantir que os tempos médios e a contagem de colisões refletissem a realidade do hardware utilizado.
* **Erros, limitações ou inconsistências identificados:** Em conformidade com as restrições da atividade, a IA não foi utilizada para pular a etapa de raciocínio da segunda versão. Após a modelagem do problema, a ferramenta foi consultada para validar abordagens sem colisões (como o algoritmo de *Fisher-Yates*) e explicar cientificamente o comportamento de escalabilidade dos tempos de execução.
* **Alterações realizadas pelo estudante:** Execução local de todas as baterias de testes para a coleta e inserção de dados *próprios* e reais na tabela comparativa, além da revisão final do código para garantir o domínio sobre a lógica de embaralhamento e manipulação dos vetores.
* **Indicação das partes do trabalho que receberam apoio da ferramenta:** Código-fonte base para a versão 1 (`preencher_vetor_v1`), estrutura de formatação da tabela de resultados, referências teóricas utilizadas na seção de Análise e formatação geral do documento.