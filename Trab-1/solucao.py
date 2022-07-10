from typing import List
import manhattan
from nodo import Nodo
from constantes import ESTADO_FINAL
from fila_nodo import Lista_Prio_Nodo
from collections import deque

def cria_nodo(estado, pai, acao, custo):
    return Nodo(estado, pai, acao, custo)
                        
def sucessor(estado):
    acoes_possiveis = []
    indice = estado.find('_')
    if pode_mover_abaixo(indice):
        acoes_possiveis.append("abaixo")
    if pode_mover_acima(indice):
        acoes_possiveis.append("acima")
    if pode_mover_direita(indice):
        acoes_possiveis.append("direita")
    if pode_mover_esquerda(indice):
        acoes_possiveis.append("esquerda")
    return determina_estados(acoes_possiveis, estado, indice)
    
'''Funções auxiliares da função sucessor:
ação direita: swap [i] com [i+1] || pode ir para direita se índice != 2, != 5 != 8
ação esquerda: swap [i] com [i-1] || pode ir para esquerda se índice != 0, != 3, != 6
ação cima: swap [i] com [i-3] || pode mover para cima quando índice > 2
ação baixo: swap[i] com [i+3] || pode mover para baixo quando índice < 6
'''
#funções que encontram movimentos possíveis:
def pode_mover_direita(indice):
    if indice not in (2,5,8):
        return True
    else:
        return False

def pode_mover_esquerda(indice):
    if indice not in (0,3,6):
        return True
    else:
        return False

def pode_mover_abaixo(indice):
    if indice < 6:
        return True
    else:
        return False

def pode_mover_acima(indice):
    if indice > 2:
        return True
    else:
        return False

#cria estados atualizados
def novo_estado(estado, indice, novo_indice):
    prox_estado = list(estado)
    prox_estado[indice], prox_estado[novo_indice] = prox_estado[novo_indice], prox_estado[indice]
    return ''.join(prox_estado)

#cria tuplas de sucessores
def determina_estados(acoes_possiveis, estado, indice):
    sucessores = []
    for acao in acoes_possiveis:
        if acao == "direita":
            sucessores.append((acao, novo_estado(estado, indice, indice+1)))
        elif acao == "esquerda":
            sucessores.append((acao, novo_estado(estado, indice, indice-1)))
        elif acao == "acima":
            sucessores.append((acao, novo_estado(estado, indice, indice-3)))
        elif acao == "abaixo":
            sucessores.append((acao, novo_estado(estado, indice, indice+3)))
    return sucessores


def e_estado_final(nodo:Nodo) -> bool:
    return nodo.estado == ESTADO_FINAL

def busca_grafo(funcao_desempilha,estado,fronteira:List):
    """
    Recebe umma funcao de desempilha (um metodo) e um estado inicial, executa
    entao o algoritmo padrao de busca usando essa funcao de desempilha na fronteira
    Retorna uma Lista com os passos dados para a solucao, ou None no caso de falha
    """
    conjunto_explorados:List[str] = []
    fronteira.append(Nodo(estado))
    falha:bool = False
    
    while not falha:
        if len(fronteira)==0 : return None
        estado_atual:Nodo = funcao_desempilha(fronteira)
        if estado_atual.custo > 25:
            return None
        
        if e_estado_final(estado_atual): return estado_atual.retorna_caminho()
        
        if estado_atual.estado not in conjunto_explorados:
            conjunto_explorados.append(estado_atual.estado)
            fronteira.extend(expande(estado_atual))
    
    return None

def expande(nodo) -> List[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    nodos_expandidos= sucessor(nodo.estado)#chama a função sucessor para criar os estados dos nodos filhos
    list=[]
    i= 0
    for x in nodos_expandidos:#para cada estado novo
        n= cria_nodo((nodos_expandidos[i][1]), nodo, nodos_expandidos[i][0], nodo.custo+1 )#cria um nodo flho
        list.append(n)#coloca os nodos filhos em uma lista de nodos iterável
        i= i+1
    return list
    
'''Funcoes auxiliares para bfs (e dfs):
solucionavel(estado): usa a funcao conta_inversoes(estado) para determinar se entrada tem solucao
acha_caminho(nodo, caminho) retorna lista de nodos percorridos da entrada até a solucao encontrada
nao_explorado(nodo, explorados) testa se o estado de um nodo ja foi atingido ou nao
expande_fronteira(nodo, fronteira) utiliza a funcao expande(nodo) para encontrar nodos filhos e aloca-os na lista'''

def solucionavel(estado):    
    if conta_inversoes(estado) % 2 == 0:
        return True
    return False

def conta_inversoes(estado):
    num_inversoes = 0
    for i in range(0,9):
        for j in range(i+1,9):
            if estado[j] != '_' and estado[i] != '_' and int(estado[i]) > int(estado[j]):
                num_inversoes += 1
    return num_inversoes

def acha_caminho(nodo, caminho):
    nodo_atual = nodo
    while nodo_atual.pai != None:
        caminho.append(nodo_atual)
        nodo_atual = nodo_atual.pai

def nao_explorado(nodo, explorados):
    if explorados.get(nodo.estado) == None:
        return True
    return False

def expande_fronteira(nodo, fronteira):
    for n in expande(nodo):
        fronteira.append(n)

def bfs(estado):
    '''primeiramente, testa se o estado de entrada é solucionavel. caso False, imediatamente retorna None.
    caso True, executa algoritmo de busca por largura.'''
    if solucionavel(estado):

        if estado == ESTADO_FINAL:
            return []
        
        solucao_encontrada = False
        explorados = {}
        fronteira = deque() #utiliza collections.deque para implementar a estrutura de dados e o método popleft() para Fila
        nodo_inicial = Nodo(estado, None, None, 0)
        fronteira.append(nodo_inicial)
    
        while not solucao_encontrada:
            if len(fronteira) == 0:
                return None
            
            nodo_atual = fronteira.popleft()

            if nodo_atual.estado == ESTADO_FINAL:
                caminho = []
                acha_caminho(nodo_atual, caminho)
                return list(reversed(caminho))
            
            if nao_explorado(nodo_atual, explorados):
                explorados[nodo_atual.estado] = nodo_atual
                expande_fronteira(nodo_atual, fronteira)
            
    return None


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    return busca_grafo(manhattan.desempilha,estado,Lista_Prio_Nodo())
