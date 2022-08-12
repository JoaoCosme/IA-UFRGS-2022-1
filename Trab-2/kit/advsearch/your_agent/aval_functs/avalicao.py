from typing import List
from advsearch.othello.board import Board
import advsearch.your_agent.aval_functs.funcoes_avaliacao as funcoes_avaliacao

#Conjunto de tuplas avaliacao/peso
avaliacoes: List = [(funcoes_avaliacao.avaliacao_quantidade_de_pecas, 40),
                    (funcoes_avaliacao.avaliacao_menos_espacos_vazios, 10),
                    (funcoes_avaliacao.avaliacao_diferenca_pecas, 10),
                    (funcoes_avaliacao.avaliacao_e_vitoria, 100),
                    (funcoes_avaliacao.avaliacao_mobilidade,20),
                    (funcoes_avaliacao.avalia_cantos_capturados,20),
                    (funcoes_avaliacao.avalia_estabilidade,40)]
                    
# pesos originais: 10,10,10,100,10,200,300

def avalia(board: Board, cor):
    pontuacao_total = 0
    for avaliacao in avaliacoes:
        resultado_avaliacao = avaliacao[0](board, cor)
        pontuacao_total += resultado_avaliacao*avaliacao[1]
    return pontuacao_total
