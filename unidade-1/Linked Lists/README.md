# RELATÓRIO DE ATIVIDADE PRÁTICA / ESTUDO INDEPENDENTE

**Disciplina:** Estrutura de Dados

**Estudante(s):** Tiago Andrei de Almeida Mendonça

**Atividade:** Implementação e Manipulação de Listas Encadeadas (Simples, Duplas, Matricial e Dinâmica)

---

## 1. Descrição da Solução

Desenvolvimento de um sistema em Python contendo a implementação do zero de estruturas de dados baseadas em Listas Encadeadas, sem a utilização de tipos nativos da linguagem (como `list` ou `collections.deque`). A solução engloba a modelagem orientada a objetos dos nós e a construção da lógica procedural para manipulação de ponteiros (referências de memória) e índices simulados (alocação matricial).

O projeto atende a 8 operações distintas solicitadas na atividade:

1. **Contagem de nós** em Lista Simplesmente Encadeada (LUE) Matricial.
2. **Concatenação** de duas LUEs Matriciais.
3. **Busca de elemento ausente** entre duas LUEs Matriciais.
4. **Intercalação ordenada** de LUEs Matriciais.
5. **Inversão de apontadores** em LUE com Alocação Dinâmica.
6. **Inversão de apontadores** em Lista Duplamente Encadeada (LDE) Dinâmica.
7. **Concatenação** de LDEs Dinâmicas.
8. **Avaliação de Polinômio** $P(x) = \sum A_i \cdot x^i$ armazenado em LDE Dinâmica.

A arquitetura foi estruturada aplicando princípios de segregação de responsabilidades: as definições das entidades (`Tipo_LUE_Matricial`, `Tipo_LDE_Dinamica`, etc.) foram isoladas em um módulo de classes para evitar acoplamento e efeitos colaterais na execução (*side effects*).

## 2. Instruções de Compilação e Execução

* **Linguagem / Ambiente:** Python 3.13.3
* **Como executar:** A solução foi construída utilizando a separação entre as definições de estrutura e o script executor. Abra o terminal na pasta raiz do código-fonte e digite `python main.py` (ou o nome do arquivo que contém os blocos de teste). O programa rodará no console imprimindo o estado das listas encadeadas antes e após cada uma das 8 operações.

## 3. Casos de Teste e Evidências de Funcionamento

* **Teste - Exercício 6 (Inversão de LDE Dinâmica):** Criação de uma lista duplamente encadeada com os nós apontando fisicamente nas direções `A <-> B <-> C`. O algoritmo de inversão permuta os elos `elop` (próximo) e `eloa` (anterior).
* **Resultado esperado:** A função deve retornar o último nó como a nova cabeça da lista e, ao ser percorrida através de `elop`, imprimir a ordem lógica inversa (`C <-> B <-> A <-> NULO`), realizando a travessia em tempo linear $O(N)$ e espaço constante $O(1)$.
* **Resultado obtido:** Os apontadores foram invertidos com sucesso. O comportamento na manipulação da memória dinâmica refletiu a teoria sem perda de referências (vazamento de memória).



*(Lembre-se de substituir o caminho abaixo pelo print real do seu terminal rodando o código)*


## 4. Referências Consultadas

* Documentação oficial do Python (classes e manipulação de instâncias).
* CARRARD, Marcos C. Algoritmos e estruturas de dados — partes 1 e 2. Ed. UNIJUÍ.
* Google Gemini.

---

## 7. Declaração de Uso de Inteligência Artificial

* **Ferramenta utilizada:** Google Gemini.
* **Finalidade de sua utilização:** Apoio na conversão de lógicas em pseudocódigo para a linguagem Python com restrições rigorosas (sem uso de coleções nativas), resolução de problemas de arquitetura de software (*circular imports* no particionamento de módulos), bem como aprofundamento teórico sobre os impactos operacionais entre alocação matricial e alocação dinâmica.
* **Etapas da atividade em que foi empregada:** Durante a fase de codificação dos 8 algoritmos de manipulação das listas, no diagnóstico de falhas de importação de arquivos Python e na estruturação da marcação semântica deste relatório em Markdown.
* **Procedimentos adotados para verificar as informações:** Todos os scripts gerados foram submetidos a testes rigorosos em ambiente local para validar as conexões dos elos (`elo`, `elop`, `eloa`) e a sinalização de término de listas (`-1` e `None`). Validou-se que a complexidade algorítmica exigida nos enunciados originais foi respeitada.
* **Erros, limitações ou inconsistências identificados:** Durante o desacoplamento do código sugerido em múltiplos arquivos, a ferramenta gerou inicialmente um cenário de importação circular (*circular import Error*) por não delimitar corretamente o ponto de entrada (`__main__`).
* **Alterações realizadas pelo estudante:** O projeto foi refatorado aplicando boas práticas de Engenharia de Software. As classes base foram isoladas de forma unidirecional no arquivo `classes.py`, enquanto a lógica de testes e operações ficou contida no arquivo principal de execução, garantindo escalabilidade e modularidade.
* **Indicação das partes do trabalho que receberam apoio da ferramenta:** Implementação das lógicas iterativas de travessia e inversão de ponteiros, explicação teórica de fundamentos estruturais e formatação final do documento.