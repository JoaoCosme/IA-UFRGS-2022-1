from calendar import c
from advsearch.othello.board import Board

coordenadas_cantos = [(0,0),(0,8),(8,0),(8,8)]

inverte_cor = lambda cor: Board.WHITE if cor == Board.BLACK else Board.BLACK

def avaliacao_quantidade_de_pecas(board:Board,cor):
    return board.num_pieces(cor)
    
def avaliacao_menos_espacos_vazios(board:Board,cor):
    return -board.num_pieces(Board.EMPTY)

def avaliacao_diferenca_pecas(board:Board,cor):
    return board.num_pieces(cor) - board.num_pieces(inverte_cor(cor))

def avaliacao_menos_ataques_oponente(board:Board,cor):
    return -board.legal_moves(inverte_cor(cor))

def avaliacao_mais_ataques_jogador(board:Board,cor):
    return board.legal_moves(cor);

def avaliacao_e_vitoria(board:Board,cor):
    return 100 if board.winner() == cor and board.is_terminal_state() else 0;

def avaliacao_mobilidade(board:Board,cor):
    return 100 * (board.legal_moves(cor)-board.legal_moves(inverte_cor(cor))) / (board.legal_moves(cor)+board.legal_moves(inverte_cor(cor)))

def avalia_cantos_capturados(board:Board,cor):
    cantos_capturados = 0
    for canto in coordenadas_cantos:
        cantos_capturados += 1 if board.tiles[canto[0]][canto[1]]==cor else 0
    return cantos_capturados * 100 / 4