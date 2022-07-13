import time
from solucao import bfs,dfs, astar_hamming, astar_manhattan

'''template usado para testes de desempenho de bfs, dfs, a* Hamming e Manhattan
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

print("BUSCA A* - DISTANCIA HAMMING")
tempo_inicial = time.time()
print("custo: ", len(astar_hamming(estado)))
tempo_final = time.time()
print("tempo total de execucao: ", tempo_final - tempo_inicial, "segundos")

print("BUSCA A* - DISTANCIA MANHATTAN")
tempo_inicial = time.time()
print("custo: ", len(astar_manhattan(estado)))
tempo_final = time.time()
print("tempo total de execucao: ", tempo_final - tempo_inicial, "segundos")
