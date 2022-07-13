from typing import List
from constantes import ESTADO_FINAL, POSICAO_VAZIA
from funcoes_distancia import *

DISTANCIA = "distancia"
NODO = "nodo"


"""
Conjunto de funções auxiliares para o calculo de A* Manhattan
"""

def calcula_distancia_posicao(estado_atual:str,numero:str)->int:
    posicao_correta = ESTADO_FINAL.find(numero)
    posicao_atual = estado_atual.find(numero)
    
    distancia_horizontal = calcula_distancia_horizontal(posicao_atual,posicao_correta)
    distancia_vertical = calcula_distancia_vertical(posicao_atual,posicao_correta)
    return distancia_horizontal+distancia_vertical

def calcula_distancia_manhattan(estado,custo=0):
    distancia_manhatan = 0
    for pos in range(len(estado)):
        if estado[pos] != ESTADO_FINAL[pos] and estado[pos] != POSICAO_VAZIA:
            distancia_manhatan += calcula_distancia_posicao(estado,estado[pos])
    return distancia_manhatan

def desempilha(lista):
    return lista.pop()
