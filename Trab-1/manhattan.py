from solucao import Nodo, ESTADO_FINAL, POSICAO_VAZIA
from funcoes_distancia import *

def calcula_distancia_posicao(estado_atual:str,numero:str)->int:
    posicao_correta = ESTADO_FINAL.find(numero)
    posicao_atual = estado_atual.find(numero)
    
    if na_linha_correta(posicao_correta,posicao_atual) :
        return calcula_distancia_horizontal(posicao_atual,posicao_correta)
    elif na_coluna_correta(posicao_correta,posicao_atual):
        return calcula_distancia_vertical(posicao_atual,posicao_correta)   
    else:
        distancia_horizontal = calcula_distancia_horizontal(posicao_atual,posicao_correta)
        distancia_vertical = calcula_distancia_vertical(posicao_atual,posicao_correta)
        return distancia_horizontal+distancia_vertical
    

def calcula_distancia_manhattan(nodo:Nodo):
    distancia_manhatan = 0
    for pos in range(len(nodo.estado)):
        if nodo.estado[pos] != ESTADO_FINAL[pos] and nodo.estado[pos] != POSICAO_VAZIA:
            distancia_manhatan += calcula_distancia_posicao(nodo.estado,nodo.estado[pos])
            
    return distancia_manhatan