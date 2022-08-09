from typing import List
from advsearch.othello.board import Board

avaliacoes:List = []
PESO_QUANTIDADE_PECAS = 1

inverte_cor = lambda cor: Board.BLACK if cor == Board.Black else Board.WHITE

def avalia(board:Board,cor):
    pontuacao_total = 0
    for avaliacao in avaliacoes:
        resultado_avaliacao = avaliacao(board,cor)
        pontuacao_total += resultado_avaliacao[0] + resultado_avaliacao[1]
    return pontuacao_total

def avaliacao_quantidade_de_pecas(board:Board,cor):
    return (board.num_pieces(cor) - board.num_pieces(inverte_cor(cor)),PESO_QUANTIDADE_PECAS)
    
