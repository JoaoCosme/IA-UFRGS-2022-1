
from operator import mod
from solucao import Nodo, ESTADO_FINAL


def calcula_distancia_posicao(estado_atual:str,numero:str)->int:
    posicao_correta = ESTADO_FINAL.find(numero)
    posicao_atual = estado_atual.find(numero)
    return abs(posicao_correta - posicao_atual)
    

def calcula_distancia_manhattan(nodo:Nodo):
    distancia_manhatan = 0
    for pos in range(len(nodo.estado)):
        if nodo.estado[pos] != ESTADO_FINAL[pos] and nodo.estado[pos] != "_":
            distancia_manhatan += calcula_distancia_posicao(nodo.estado,nodo.estado[pos])
            
    return distancia_manhatan