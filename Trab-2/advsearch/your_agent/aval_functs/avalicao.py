from typing import List
from advsearch.othello.board import Board
import advsearch.your_agent.aval_functs.funcoes_avaliacao as funcoes_avaliacao

PESO_QUANTIDADE_PECAS = 1
avaliacoes:List = [(funcoes_avaliacao.avaliacao_quantidade_de_pecas,PESO_QUANTIDADE_PECAS)]



def avalia(board:Board,cor):
    pontuacao_total = 0
    for avaliacao in avaliacoes:
        resultado_avaliacao = avaliacao[0](board,cor)
        pontuacao_total += resultado_avaliacao*avaliacao[1]
    return pontuacao_total
