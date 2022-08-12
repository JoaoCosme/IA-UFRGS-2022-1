import imp
import random
import sys
import pickle # biblioteca para fazer a copia do estado do tabuleiro
from advsearch.othello.board import Board
from advsearch.your_agent.aval_functs.avalicao import avalia

NULL_MOVE = (-1,-1) # variavel para representar um movimento nulo
DEPTH_START = 0 # inicializa a profundidade com 0
DEPTH_LIM = 3 # representa a profundidade maxima
VAL_MAX =  10000 #valor maximo inicial
VAL_MIN = -10000 #valor minimo inicial

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

def player_max(tabuleiro, color, alpha, beta, depth): #Funcao que representa o jogador MAX

    if condicao_parada(tabuleiro, depth, color): #Testa condicao de parada 
        return avalia_pos(tabuleiro, color), NULL_MOVE #Caso ela retorne algo, devolve a funcao de avaliacao com movimento nulo
    
    # inicializacao das variaveis
    val = VAL_MIN
    move = NULL_MOVE
    legal_moves = tabuleiro.legal_moves(color)

    if len(legal_moves) == 0: 
        legal_moves = [NULL_MOVE] #Se jogador atual nao possui jogadas validas, devolve movimeto vazio

    # loop que descobre o melhor movimento no estado atual
    for move_prox in legal_moves:
        state = pickle.loads(pickle.dumps(tabuleiro))
        state.process_move(move_prox, color)
        temp_val, temp_move = player_min(state, tabuleiro.opponent(color), alpha, beta, depth + 1) #Define se deve atualizar ou nao o novo movimento
        val, move = (temp_val, move_prox) if temp_val > val else (val, move)
        alpha = max(alpha, val)
        
        if alpha >= beta: # Para se MIN possui uma jogada melhor
            break
    return val, move

def player_min(tabuleiro, color, alpha, beta, depth): #Funcao que representa o jogador MAX

    if condicao_parada(tabuleiro, depth, color): #Testa condicao de parada 
        return avalia_pos(tabuleiro, color), NULL_MOVE #Caso ela retorne algo, devolve a funcao de avaliacao com movimento nulo
    
    # inicializacao das variaveis
    val = VAL_MAX
    move = NULL_MOVE
    legal_moves = tabuleiro.legal_moves(color)

    if len(legal_moves) == 0: 
        legal_moves = [NULL_MOVE] #Se jogador atual nÃ£o possui jogadas validas, devolve movimeto vazio

    # loop que descobre o melhor movimento no estado atual
    for new_move in legal_moves:
        state = pickle.loads(pickle.dumps(tabuleiro))
        state.process_move(new_move, color)
        temp_val, temp_move = player_max(state, tabuleiro.opponent(color), alpha, beta, depth + 1) #Define se deve atualizar ou nao o novo movimento
        val, move = (temp_val, new_move) if temp_val < val else (val, move)
        beta = min(beta, val)
        
        if beta <= alpha: # Para se MAX possui uma jogada melhor
            break
    return val, move

