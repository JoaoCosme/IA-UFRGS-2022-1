from calendar import c
from advsearch.othello.board import Board

coordenadas_cantos = [(0, 0), (0, 7), (7, 0), (7, 7)]
valor_utilitario = [[4, -3, 2, 2, 2, 2, -3, 4], 
                    [-3, -4, -1, -1, -1, -1, -4, -3],
                    [2, -1, 1, 0, 0, 1, -1, 2], 
                    [2, -1, 1, 0, 0, 1, -1, 2], 
                    [2, -1, 0, 1, 1, 0, -1, 2], 
                    [2, -1, 0, 1, 1, 0, -1, 2], 
                    [2, -1, 1, 0, 0, 1, -1, 2], 
                    [2, -1, 1, 0, 0, 1, -1, 2], 
                    [-3, -4, -1, -1, -1, -1, -4, -3], 
                    [4, -3, 2, 2, 2, 2, -3, 4]]


def inverte_cor(cor): return Board.WHITE if cor == Board.BLACK else Board.BLACK


def avaliacao_quantidade_de_pecas(board: Board, cor):
    return board.num_pieces(cor)


def avaliacao_menos_espacos_vazios(board: Board, cor):
    return -board.num_pieces(Board.EMPTY)


def avaliacao_diferenca_pecas(board: Board, cor):
    return board.num_pieces(cor) - board.num_pieces(inverte_cor(cor))


def avaliacao_menos_ataques_oponente(board: Board, cor):
    return -board.legal_moves(inverte_cor(cor))


def avaliacao_mais_ataques_jogador(board: Board, cor):
    return board.legal_moves(cor)


def avaliacao_e_vitoria(board: Board, cor):
    return 100 if board.winner() == cor and board.is_terminal_state() else 0


def avaliacao_mobilidade(board: Board, cor):
    jogadas_jogador = board.legal_moves(cor)
    jogadas_oponent = board.legal_moves(inverte_cor(cor))
    
    if jogadas_jogador + jogadas_oponent == 0:
        return 0
    
    return 100 * jogadas_jogador - jogadas_oponent / (jogadas_oponent + jogadas_jogador)


def avalia_cantos_capturados(board: Board, cor):
    cantos_capturados = 0
    for canto in coordenadas_cantos:
        cantos_capturados += 1 if board.tiles[canto[0]][canto[1]] == cor else 0
    return cantos_capturados * 100 / 4

def avalia_estabilidade(board:Board,cor):
    estabilidade_jogador = 0
    estabilidade_oponente=0
    for x in range(8):
        for y in range(8):
            if board.tiles[x][y] == cor:
                estabilidade_jogador += valor_utilitario[x][y]
            else:
                estabilidade_oponente += valor_utilitario[x][y]
                
    if estabilidade_oponente+estabilidade_jogador == 0:
        return 0
    
    return 100 * estabilidade_jogador - estabilidade_oponente / (estabilidade_jogador+estabilidade_oponente)