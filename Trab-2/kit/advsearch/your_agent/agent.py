import imp
import random
import sys
from advsearch.othello.board import Board
from advsearch.your_agent.aval_functs.avalicao import avalia

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

# Deve receber sempre a cor do nosso jogador
# Retorna um inteiro com a pontuação de determiando estado
def avalia(board:Board,cor)->int:
    return avalia(board,cor)

def make_move(the_board:Board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    posicoes = the_board.legal_moves(color)
    max_aval = -100
    melhor_pos = None
    
    copia_board = the_board
    
    for posicao in posicoes:
        copia_board.process_move(posicao,color)
        avaliacao = avalia(copia_board,color)
        if avaliacao > max_aval:
            max_aval = avaliacao
            melhor_pos = posicao
        copia_board = the_board
    
    
    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada com as pretas.
    # Remova-o e coloque a sua implementacao da poda alpha-beta
    return melhor_pos

