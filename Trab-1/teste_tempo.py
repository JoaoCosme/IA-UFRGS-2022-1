import time
from solucao import bfs,dfs

'''template usado para testes de desempenho de bfs e dfs
os valores de tempo dependem da maquina e das especificacoes dela'''

#testes
estado = '2_3541687'

print("BUSCA POR LARGURA - BFS")
tempo_inicial = time.time()
print("custo: ", len(bfs(estado)))
tempo_final = time.time()
print("tempo total de execucao: ", tempo_final - tempo_inicial, "segundos")

print("BUSCA POR PROFUNDIDADE - DFS")
tempo_inicial = time.time()
print("custo: ", len(dfs(estado)))
tempo_final = time.time()
print("tempo total de execucao: ", tempo_final - tempo_inicial, "segundos")