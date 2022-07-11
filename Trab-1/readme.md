# IA 2022/1 - GRUPO 5

Alice Santin Varella - 00259915

Joao Pedro Cosme da Silva --00314792

# Detalhes de Implementação

A classe Nodo foi separada em um arquivo `nodo.py` a fim de que pudesse ser usada para tipar parametros e variaveis em diversos arquivos sem causa refêrencia circular quando estes fossem usados em `solucao.py`

# Resultados dos testes para o estado "2_3541687":

## BUSCA POR LARGURA - BFS
total custo:  23

total nodos explorados:  100788

tempo total de execucao:  0.929417610168457 segundos

## BUSCA POR PROFUNDIDADE - DFS

total custo:  101601

total nodos explorados:  154161

tempo total de execucao:  1.3857574462890625 segundos

## BUSCA A* - DISTANCIA MANHATTAN




## REFERÊNCIAS:

A função booleana solucionavel(estado) foi implementada com base nas informações retiradas da seção *Detecting Unsolvable Boards* sobre o Slider Puzzle no link https://www.cs.princeton.edu/courses/archive/spring21/cos226/assignments/8puzzle/specification.php
