# IA 2022/1 - GRUPO 5

|Nome|Cartao|Turma|
|---|---|----|
|Alice Santin Varella| 00259915 | B 
|Joao Pedro Cosme da Silva|00314792 |A
|Eduardo André Leite | 00287684| A

## Detalhes de Implementação

### Função de Parada

Para a função de parada, foi estabelecida uma profundidade máxima fixa de 5. 

Testes foram realizados com profundidades 7, 6 e 5. Com profundidade 7, o alfa_beta_player era desclassificado devido ao alto número de timeouts. Para a profundidade 6, após 10 partidas contra um randomplayer, constatou-se um win rate de 80%. Todavia, um número relativamente alto de timeouts aconteceu entre as partidas, o que tornou a profundidade 6 um alto candidato a futuras desclassificações em torneios.

Portanto, com um win rate de 70% a profundidade máxima setada para este algoritmo foi 5, garantindo um índice de vitórias relativamente bom e poucas jogadas inválidas.

Tabelas com as pontuações e desempenhos do alfa_beta_player são apresentados na seção de Testes.

### Funções de Avaliação

Para a avaliação dos estados de parada, foi utilizado o somatório de diversos critérios, no modelo

$\sum_ {i}^{n} f_i(estado)\times w_i$

As avaliações utilizadas foram:

+ Quantidade de Peças do Jogador
+ Minização de espaços vazios
+ Maximização da diferença cor jogador x cor adversario
+ Avaliação se estado é terminal e vitoria do jogador

As avaliações abaixo foram retiradas do artigo "An Analysis of Heuristics in Othello", disponivel neste [link](https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf)

+ Estabilidade → Nesta avaliação testamos a porcentagem de peças em lugares com baixa chance de serem captuados
+ Cantos capturados → cantos nao podem ser flanqueados e, logo, sao excelentes posições
+ Mobilidade → Quantas proximas jogadas nos temos em relação a nosso oponente

### Poda Alfa-beta

## Testes