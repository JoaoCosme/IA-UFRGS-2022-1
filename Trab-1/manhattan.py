from solucao import Nodo, ESTADO_FINAL, POSICAO_VAZIA,NUMERO_COLUNAS,NUMERO_LINHAS

def calcula_distancia_posicao(estado_atual:str,numero:str)->int:
    posicao_correta = ESTADO_FINAL.find(numero)
    posicao_atual = estado_atual.find(numero)
    
    
    calcula_distancia_vertical = lambda posicao_correta, posicao_atual: abs(posicao_correta//NUMERO_LINHAS-posicao_atual//NUMERO_LINHAS)
    calcula_distancia_horizontal = lambda posicao_correta, posicao_atual:abs(posicao_correta%NUMERO_COLUNAS-posicao_atual%NUMERO_COLUNAS)
    
    na_coluna_correta = lambda posicao_correta,posicao_atual:calcula_distancia_vertical(posicao_correta,posicao_atual)==0
    na_linha_correta = lambda posicao_correta,posicao_atual:abs(posicao_correta-posicao_atual)<2
    
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