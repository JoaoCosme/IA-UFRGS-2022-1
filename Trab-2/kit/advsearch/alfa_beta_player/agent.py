from ftplib import error_reply
import random
import sys

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

#constante para condição de parada da poda alfa beta
PROFUNDIDADE_MAXIMA = 6

def func_avalicao(stado, color):
    return None


def poda_alfa_beta():
    '''
    if condicao_parada():
        return avalia()
    '''
    return None

#funçao booleana que checa se a poda alfa beta chegou à profundidade maxima.
def condicao_parada(profundidade):
    return profundidade > PROFUNDIDADE_MAXIMA


def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada com as pretas.
    # Remova-o e coloque a sua implementacao da poda alpha-beta
    return random.choice([(2, 3), (4, 5), (5, 4), (3, 2)])
