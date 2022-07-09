from solucao import Nodo, ESTADO_FINAL, POSICAO_VAZIA


NUMERO_COLUNAS = 3

def calcula_distancia_posicao(estado_atual:str,numero:str)->int:
    posicao_correta = ESTADO_FINAL.find(numero)
    posicao_atual = estado_atual.find(numero)
    
    na_coluna_correta = lambda posicao_correta,posicao_atual:posicao_correta%NUMERO_COLUNAS ==posicao_atual%NUMERO_COLUNAS
    na_linha_correta = lambda posicao_correta,posicao_atual:abs(posicao_correta-posicao_atual)<2
    
    if na_linha_correta(posicao_correta,posicao_atual) :
        return abs(posicao_correta-posicao_atual)
    elif na_coluna_correta(posicao_correta,posicao_atual):
        return abs(posicao_correta//3-posicao_atual//3)    
    else:
        distancia_horizontal = abs(posicao_correta%3-posicao_atual%3)
        distancia_vertical = abs(posicao_correta//3-posicao_atual//3)
        return distancia_horizontal+distancia_vertical
    

def calcula_distancia_manhattan(nodo:Nodo):
    distancia_manhatan = 0
    for pos in range(len(nodo.estado)):
        if nodo.estado[pos] != ESTADO_FINAL[pos] and nodo.estado[pos] != POSICAO_VAZIA:
            distancia_manhatan += calcula_distancia_posicao(nodo.estado,nodo.estado[pos])
            
    return distancia_manhatan