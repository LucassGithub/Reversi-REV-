import unittest

from client.model.board import Board
from client.model.cell import CellState


class TestBoard(unittest.TestCase):
    def test_init_cells(self):
        board_2 = Board(2)
        self.assertEqual(board_2.cells[0][0].state, CellState.player2)
        self.assertEqual(board_2.cells[1][0].state, CellState.player1)
        self.assertEqual(board_2.cells[0][1].state, CellState.player1)
        self.assertEqual(board_2.cells[1][1].state, CellState.player2)
        board_4 = Board(4)
        self.assertEqual(board_4.cells[0][0].state, CellState.empty)
        self.assertEqual(board_4.cells[0][3].state, CellState.empty)
        self.assertEqual(board_4.cells[3][0].state, CellState.empty)
        self.assertEqual(board_4.cells[3][3].state, CellState.empty)
        self.assertEqual(board_4.cells[1][1].state, CellState.player2)
        self.assertEqual(board_4.cells[1][2].state, CellState.player1)
        self.assertEqual(board_4.cells[2][1].state, CellState.player1)
        self.assertEqual(board_4.cells[2][2].state, CellState.player2)

    def test_get_state(self):
        cells_2 = [
            [CellState.player2, CellState.player1],
            [CellState.player1, CellState.player2],
        ]
        board_2 = Board(2)
        self.assertEqual(board_2.get_state(), cells_2)
        cells_4 = [
            [CellState.empty, CellState.empty, CellState.empty, CellState.empty],
            [
                CellState.empty,
                CellState.player2,
                CellState.player1,
                CellState.empty,
            ],
            [
                CellState.empty,
                CellState.player1,
                CellState.player2,
                CellState.empty,
            ],
            [CellState.empty, CellState.empty, CellState.empty, CellState.empty],
        ]
        board_4 = Board(4)
        self.assertEqual(board_4.get_state(), cells_4)

    def test_get_num_type(self):
        board_4 = Board(4)  # has 16 cells: 2 - player1, 2 - player2, 12 - empty
        self.assertEqual(board_4.get_num_type(CellState.empty), 12)
        self.assertEqual(board_4.get_num_type(CellState.player1), 2)
        self.assertEqual(board_4.get_num_type(CellState.player2), 2)
        board_2 = Board(2)  # has 4 cells: 2 - player1, 2 - player2, 0 - empty
        self.assertEqual(board_2.get_num_type(CellState.empty), 0)
        self.assertEqual(board_2.get_num_type(CellState.player1), 2)
        self.assertEqual(board_2.get_num_type(CellState.player2), 2)


if __name__ == "__main__":
    unittest.main()
