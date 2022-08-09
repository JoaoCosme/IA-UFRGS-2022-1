
from tkinter.font import BOLD
from advsearch.othello.board import Board

inverte_cor = lambda cor: Board.WHITE if cor == Board.BLACK else Board.BLACK

def avaliacao_quantidade_de_pecas(board:Board,cor):
    return board.num_pieces(cor) - board.num_pieces(inverte_cor(cor))
    
def avaliacao_menos_espacos_vazios(board:Board,cor):
    return board.num_pieces(Board.EMPTY)