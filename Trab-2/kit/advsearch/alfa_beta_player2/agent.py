from ftplib import error_reply
import random
import sys
from advsearch.alfa_beta_player2.aval_functs2.avalicao import avalia
from advsearch.othello.board import Board
import pickle # biblioteca para fazer a cópia do estado do tabuleiro


# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

NULL_MOVE = (-1,-1) # variavel para representar um movimento nulo
DEPTH_START = 0 # inicializa a profundidade com 0
DEPTH_LIM = 6 # representa a profundidade máxima
VAL_MAX =  10000 #valor máximo inicial
VAL_MIN = -10000 #valor mínimo inicial

# funçao booleana que checa se a poda alfa beta chegou à profundidade maxima.
def condicao_parada(profundidade):
    return profundidade > DEPTH_LIM


def avalia_board(the_board: Board, color):
    posicoes = the_board.legal_moves(color)
    max_aval = -99999999999999
    melhor_pos = None

    copia_board = the_board

    for posicao in posicoes:
        copia_board.process_move(posicao, color)
        avaliacao = avalia(copia_board, color)
        if avaliacao > max_aval:
            max_aval = avaliacao
            melhor_pos = posicao
        copia_board = the_board

    return melhor_pos

def player_max(tabuleiro, color, alpha, beta, depth): #Função que representa o jogador MAX

    if condicao_parada(depth): #Testa condição de parada 
        return avalia(tabuleiro, color), NULL_MOVE #Caso ela retorne algo, devolve a função de avaliação com movimento nulo
    
    # inicialização das variaveis
    val = VAL_MIN
    move = NULL_MOVE
    legal_moves = tabuleiro.legal_moves(color)

    if len(legal_moves) == 0: 
        legal_moves = [NULL_MOVE] #Se jogador atual não possui jogadas válidas, devolve movimeto vazio

    # loop que descobre o melhor movimento no estado atual
    for move_prox in legal_moves:
        state = pickle.loads(pickle.dumps(tabuleiro))
        state.process_move(move_prox, color)
        temp_val, temp_move = player_min(state, tabuleiro.opponent(color), alpha, beta, depth + 1) #Define se deve atualizar ou não o novo movimento
        val, move = (temp_val, move_prox) if temp_val > val else (val, move)
        alpha = max(alpha, val)
        
        if alpha >= beta: # Para se MIN possui uma jogada melhor
            break
    return val, move

def player_min(tabuleiro, color, alpha, beta, depth): #Função que representa o jogador MIN

    if condicao_parada(depth): #Testa condição de parada 
        return avalia(tabuleiro, color), NULL_MOVE #Caso ela retorne algo, devolve a função de avaliação com movimento nulo
    
    # inicialização das variaveis
    val = VAL_MAX
    move = NULL_MOVE
    legal_moves = tabuleiro.legal_moves(color)

    if len(legal_moves) == 0: 
        legal_moves = [NULL_MOVE] #Se jogador atual não possui jogadas válidas, devolve movimeto vazio

    # loop que descobre o melhor movimento no estado atual
    for new_move in legal_moves:
        state = pickle.loads(pickle.dumps(tabuleiro))
        state.process_move(new_move, color)
        temp_val, temp_move = player_max(state, tabuleiro.opponent(color), alpha, beta, depth + 1) #Define se deve atualizar ou não o novo movimento
        val, move = (temp_val, new_move) if temp_val < val else (val, move)
        beta = min(beta, val)
        
        if beta <= alpha: # Para se MAX possui uma jogada melhor
            break
    return val, move

def make_move(the_board: Board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada com as pretas.
    # Remova-o e coloque a sua implementacao da poda alpha-beta
    val, move = player_max(the_board, color, VAL_MIN, VAL_MAX, DEPTH_START) #começa o MINMAX chamando a função MAX para jogar
    #return avalia_board(the_board, color)
    return move