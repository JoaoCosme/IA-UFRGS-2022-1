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

### Poda Alfa-beta

## Testes