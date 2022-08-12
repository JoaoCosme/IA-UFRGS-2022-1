# IA 2022/1 - GRUPO 5

|Nome|Cartao|Turma|
|---|---|----|
|Alice Santin Varella| 00259915 | B 
|Joao Pedro Cosme da Silva|00314792 |A
|Eduardo André Leite | 00287684| A

## Detalhes de Implementação

### Função de Parada

Uma função booleana de nome `condicao_parada()` testa diferentes condições que fazem a operação ser finalizada: alcance da profundidade máxima, estado terminal do tabuleiro ou inexistência de jogadas legais a serem feitas.

Para a função de parada, foi estabelecida uma profundidade máxima fixa de 3. 

Testes foram realizados com profundidades 3, 5, 6 e 7. Com profundidade 7, o alfa_beta_player era constantemente desclassificado devido ao alto número de timeouts. A profundidade 6 mostrou-se muito instável, com uma ocorrência de desclassificação, um empate, e várias derrotas. As profundidades 3 e 5 apresentaram desempenho muito similar. Foi escolhida a profundidade 3 com o intuito de mesclar eficiência de tempo com bom índice de vitórias.

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

## **1. randomplayer vs alfa_beta_player**

Heurísticas das funções de avaliação selecionadas:

**quantidade_de_pecas**: 20

**menos_espacos_vazios**: 10

**diferenca_pecas**: 10

**e_vitoria**: 100

**mobilidade**: 10

**cantos_capturados**: 20

**estabilidade**: 40

## **TESTE 1**: Profundidade =  3

|#|Pontuação randomplayer|Pontuação alfa_beta|Vitória alfa_beta|
|--|--------|--------|--------|
|1|11|53|x|
|2|25|39|x|
|3|27|37|x|
|4|29|35|x|
|5|24|40|x|
|6|24|40|x|
|7|35|29||
|8|14|50|x|
|9|28|36|x|
|10|23|41|x

Win% = 90%

## **TESTE 2**: Profundidade =  5

|#|Pontuação randomplayer|Pontuação alfa_beta|Vitória alfa_beta|
|--|--------|--------|--------|
|1|15|49|x|
|2|30|34|x|
|3|32|32|Draw|
|4|20|44|x|
|5|13|51|x|
|6|19|45|x|
|7|11|53|x|
|8|15|49|x|
|9|28|36|x|
|10|23|41|x|

Win% = 90%

## **TESTE 3** Profundidade = 6

|#|Pontuação randomplayer|Pontuação alfa_beta|Vitória alfa_beta|
|--|--------|--------|--------|
|1|42|22||
|2|33|31||
|3|29|35|x|
|4|36|28||
|5|17|47|x|
|6|13|51|x|
|7|19|45|x|
|8|21|7|DISQUALIFIED|
|9|31|33|x|
|10|32|32|Draw|

Win% = 50%

**P.S: Profundidade = 6 apresenta muitos timeouts durante as partidas. Não é recomendado o uso dessa profundidade.**

## **TESTE 4**: Profundidade =  7

Foi obtida a mensagem de desclassificação em 5 testes consecutivos: 

**Player 2 (advsearch.alfa_beta_player) DISQUALIFIED! Too many illegal move attempts.
End of game reached!**

## **2.alfa_beta_player1 vs alfa_beta_player2**

**Profundidade máxima = 3** (ambos)

## **TESTE 1**

|avalia|alfa_beta_player1|alfa_beta_player2|
|--|----|----|
|**quantidade_de_pecas**|20|20|
|**menos_espacos_vazios**|10|10|
|**diferenca_pecas**|10|10|
|**e_vitoria**|100|100|
|**mobilidade**|10|20|
|**cantos_capturados**|20|30|
|**estabilidade**|40|40|

|Pontuação alfa_beta1|Pontuação alfa_beta2|Vitória|
|--------|--------|--------|
|33|31|alfa_beta1|

## **TESTE 2**

|avalia|alfa_beta_player1|alfa_beta_player2|
|--|----|----|
|**quantidade_de_pecas**|20|10|
|**menos_espacos_vazios**|10|10|
|**diferenca_pecas**|10|10|
|**e_vitoria**|100|100|
|**mobilidade**|10|20|
|**cantos_capturados**|20|100|
|**estabilidade**|40|30|

|Pontuação alfa_beta1|Pontuação alfa_beta2|Vitória|
|--------|--------|--------|
|33|31|alfa_beta1|

## **TESTE 3**

|avalia|alfa_beta_player1|alfa_beta_player2|
|--|----|----|
|**quantidade_de_pecas**|20|20|
|**menos_espacos_vazios**|10|10|
|**diferenca_pecas**|10|10|
|**e_vitoria**|100|100|
|**mobilidade**|10|10|
|**cantos_capturados**|20|20|
|**estabilidade**|40|40|

|Pontuação alfa_beta1|Pontuação alfa_beta2|Vitória|
|--------|--------|--------|
|35|29|alfa_beta1|

**OBS: neste caso, ganhou quem foi o primeiro a jogar.**

## **TESTE 4**

|avalia|alfa_beta_player1|alfa_beta_player2|
|--|----|----|
|**quantidade_de_pecas**|20|80|
|**menos_espacos_vazios**|10|20|
|**diferenca_pecas**|10|10|
|**e_vitoria**|100|400|
|**mobilidade**|10|20|
|**cantos_capturados**|20|100|
|**estabilidade**|40|70|

|Pontuação alfa_beta1|Pontuação alfa_beta2|Vitória|
|--------|--------|--------|
|33|31|alfa_beta1|

A sequência *[20,10,10,100,10,20,40]* apresenta os melhores resultados nos testes.