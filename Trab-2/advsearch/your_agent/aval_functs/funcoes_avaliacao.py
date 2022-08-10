from advsearch.othello.board import Board

inverte_cor = lambda cor: Board.WHITE if cor == Board.BLACK else Board.BLACK

def avaliacao_quantidade_de_pecas(board:Board,cor):
    return board.num_pieces(cor)
    
def avaliacao_menos_espacos_vazios(board:Board,cor):
    return -board.num_pieces(Board.EMPTY)

def avaliacao_diferenca_pecas(board:Board,cor):
    return board.num_pieces(cor) - board.num_pieces(inverte_cor(cor))

def avaliacao_menos_ataques_oponente(board:Board,cor):
    return 0;

def avaliacao_mais_ataques_jogador(board:Board,cor):
    return 0;

def avaliacao_e_vitoria(board:Board,cor):
    return 100 if board.num_pieces(cor) == 60 else 0;
    