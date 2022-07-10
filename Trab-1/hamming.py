from typing import List
from constantes import ESTADO_FINAL, TAMANHO_ESTADO

def calcula_distancia_hamming(estado_atual:str,estado_final:str)->int: #dados 2 estados, devolve o valor definido pela quantidade de números diferentes em cada posião da string
    i = 0 #variável de controle do while
    custo = 0 #guarda o valor da distancia de Hamming
    if len(estado_atual)!= TAMANHO_ESTADO or len(ESTADO_FINAL)!= TAMANHO_ESTADO: #testa se as strings dos estados estão com tamanho correto
        print("Tamanhos das strings de estado diferentes")
        return None
    else:
        while i < TAMANHO_ESTADO: #enquanto variável de controle for menor que tamanho das strings de estado...
            if estado_atual[i] != estado_final[i]: #compara os números na mesma posição dos estados
                custo = custo + 1
            i = i + 1
        return custo #retorna o valor da distancia de Hamming

def desempilha(lista):
    return lista.pop()
