from constantes import NUMERO_COLUNAS,NUMERO_LINHAS

def calcula_distancia_vertical(posicao_correta, posicao_atual): 
    return abs(posicao_correta//NUMERO_LINHAS-posicao_atual//NUMERO_LINHAS)
def calcula_distancia_horizontal(posicao_correta, posicao_atual):
    return abs(posicao_correta%NUMERO_COLUNAS-posicao_atual%NUMERO_COLUNAS)
    
def na_coluna_correta(posicao_correta,posicao_atual):
    return calcula_distancia_horizontal(posicao_correta,posicao_atual)==0

def na_linha_correta(posicao_correta,posicao_atual):
    return calcula_distancia_vertical(posicao_correta,posicao_atual)==0

   