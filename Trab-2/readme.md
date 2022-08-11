# IA 2022/1 - GRUPO 5

|Nome|Cartao|Turma|
|---|---|----|
|Alice Santin Varella| 00259915 | B 
|Joao Pedro Cosme da Silva|00314792 |A
|Eduardo André Leite | 00287684| A

## Detalhes de Implementação

### Função de Parada

### Funções de Avaliação

Para a avaliação dos estados de parada, foi utilizado o somatório de diversos critérios, no modelo

$\sum_ {i}^{n} f_i(estado)\times w_i$

As avaliações utilizadas foram:

+ Quantidade de Peças do Jogador
+ Minização de espaços vazios
+ Maximização da diferença cor jogador x cor adversario
+ Minimização de proximos estados do oponente
+ Maximização de proximos estados do jogador
+ Avaliação se estado é terminal e vitoria do jogador

As avaliações abaixo foram retiradas do artigo "An Analysis of Heuristics in Othello", disponivel neste [link](https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf)

+ Estabilidade → Nesta avaliação testamos a porcentagem de peças em lugares com baixa chance de serem captuados
+ Cantos capturados → cantos nao podem ser flanqueados e, logo, sao excelentes posições
+ Mobilidade → Quantas proximas jogadas nos temos em relação a nosso oponente

### Poda Alfa-beta

## Testes