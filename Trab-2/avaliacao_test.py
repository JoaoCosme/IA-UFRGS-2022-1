import unittest
import advsearch.your_agent.aval_functs.avalicao as avaliacao
import advsearch.othello.board as board
from advsearch.othello.board import Board


class SimpleTest(unittest.TestCase):

    def test(self):
        self.assertEqual(3, avaliacao.avalia(
            criaBoard(1, 0, 1), Board.BLACK), "Avalia corretamente para numero de pecas")


if __name__ == '__main__':
    unittest.main()


def criaBoard(numPretas: int, numBrancas: int, numVazias: int):
    board = Board()
    board.piece_count[Board.BLACK] = numPretas
    board.piece_count[Board.WHITE] = numBrancas
    board.piece_count[Board.EMPTY] = numVazias
    return board
