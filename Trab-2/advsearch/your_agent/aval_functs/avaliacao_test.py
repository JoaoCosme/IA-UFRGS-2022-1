import imp
import numbers
import unittest
import avalicao
import advsearch.othello.board as board
from advsearch.othello.board import Board


class SimpleTest(unittest.TestCase):

	# Returns True or False.
	def test(self):		
		self.assertEqual(1,avalicao.avalia(criaBoard(1,0),Board.BLACK),"Avalia corretamente para numero de pecas")

if __name__ == '__main__':
	unittest.main()


def criaBoard(numPretas:int,numBrancas:int):
    board = Board()
    board.piece_count[Board.BLACK] = numPretas
    board.piece_count[Board.WHITE] = numBrancas