from dataclasses import FrozenInstanceError
from typing import List, Optional
import manhattan
import hamming
from nodo import Nodo
from constantes import ESTADO_FINAL, MANHATTAN, HAMMING
from fila_nodo import Lista_Prio_Nodo
from collections import deque

MAX_FRONTEIRA = 10000

def cria_nodo(estado, pai=None, acao=None, custo=0,astar:str=None):
    return Nodo(estado, pai, acao, custo,astar)
                        
def sucessor(estado):
    acoes_possiveis = []
    sucessores = []
    indice = estado.find('_')
    if pode_mover_abaixo(indice):
        acoes_possiveis.append("abaixo")
    if pode_mover_acima(indice):
        acoes_possiveis.append("acima")
    if pode_mover_direita(indice):
        acoes_possiveis.append("direita")
    if pode_mover_esquerda(indice):
        acoes_possiveis.append("esquerda")
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

def e_estado_final(nodo:Nodo) -> bool:
    return nodo.estado == ESTADO_FINAL

def busca_grafo(funcao_desempilha,estado,fronteira:List=[],astar:str=None):
    """
    Recebe umma funcao de desempilha (um metodo),um estado inicial e um tipo de fronteira
    executa entao o algoritmo padrao de busca usando essa funcao de desempilha na fronteira
    Retorna uma Lista com os passos dados para a solucao, ou None no caso de falha
    """
    
    conjunto_explorados = {}
    fronteira.append(cria_nodo(estado,astar=astar))
    falha:bool = False
    
    while not falha:
        if len(fronteira)==0: return None
        
        estado_atual:Nodo = funcao_desempilha(fronteira)
                
        if e_estado_final(estado_atual): 
            return estado_atual.retorna_caminho()
        
        if not conjunto_explorados.get(estado_atual.estado):
            conjunto_explorados[estado_atual.estado] = estado_atual
            
            expandidos = expande(estado_atual,astar)
                
            fronteira.extend(expandidos)    
    return None

def expande(nodo,astar:str=None) -> List[Nodo]:
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
        n= cria_nodo((nodos_expandidos[i][1]), nodo, nodos_expandidos[i][0], nodo.custo+1 ,astar)#cria um nodo flho
        list.append(n)#coloca os nodos filhos em uma lista de nodos iterável
        i= i+1
    return list


# def solucionavel(estado): 
#     Um estado de entrada do 8-puzzle é solucionavel se o numero de inversoes de posicoes e' par
#     esta funcao booleana recebe a string estado, converte os digitos nao vazios para inteiro e testa, para cada digito i, 
#     quantos digitos apos i na string sao menores que i (e deverao trocar de lugar)
#     se a contagem termina com numero par, retorna True (e' solucionavel). se termina impar, retorna False (nao solucionavel) 
#     num_inversoes = 0
#     for i in range(0,9):
#         for j in range(i+1,9):
#             if estado[j] != '_' and estado[i] != '_' and int(estado[i]) > int(estado[j]):
#                 num_inversoes += 1    
#     if num_inversoes % 2 == 0:
#         return True
#     return False


def bfs(estado):
    '''O conjunto nodos_explorados e' implementado como um dicionario onde os indices sao as chaves estado de cada Nodo.
    Estados iniciais sem solucao tendem a entrar em loop infinito e revisitar os mesmos estados multiplas vezes. 
    Se um estado nunca foi visitado (retorna None no metodo get() do dicionario), ele entra no dicionario e expande a fronteira.
    Se ja esta no dicionario, o algoritmo apenas busca o proximo elemento ja existente na fila.
    '''
    
    funcao = lambda deque:deque.popleft()
    pilha = deque()
    return busca_grafo(funcao,estado,pilha)


def dfs(estado):
    '''nao fornece solucao otima. diferenca entre bfs e dfs e' a estrutura de dados utilizada (no caso da dfs e' pilha).'''
    funcao = lambda deque:deque.pop()
    pilha = deque()
    return busca_grafo(funcao,estado,pilha)
    

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
    fronteira = Lista_Prio_Nodo()
    return busca_grafo(hamming.desempilha,estado,fronteira, HAMMING)


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    fronteira = Lista_Prio_Nodo()
    return busca_grafo(manhattan.desempilha,estado,fronteira, MANHATTAN)
