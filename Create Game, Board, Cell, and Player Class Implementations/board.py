from typing import List

from cell import *


class Board:
    def __init__(self, size: int, next_turn: int) -> None:
        if size % 2 != 0:
            raise Exception("Board size must be an even number")
        if (next_turn != 1) and (next_turn != 2):
            raise Exception("Next turn must be a valid player (1 or 2)")
        self.size: int = size
        self.next_turn: int = next_turn
        self.cells: List[Cell] = [
            [Cell.empty for c in range(size)] for r in range(size)
        ]
        # initialize the four starting disks at the center of the board
        self.cells[size // 2][size // 2 - 1] = Cell.player1
        self.cells[size // 2 - 1][(size // 2)] = Cell.player1
        self.cells[size // 2 - 1][size // 2 - 1] = Cell.player2
        self.cells[size // 2][size // 2] = Cell.player2

    def get_state(self) -> List[Cell]:
        """
        Get the current state of the board, the cells field.

        :return: cells
        """
        return self.cells

    def get_num_type(self, type: Cell) -> int:
        """
        Get the number of cells in the board that are of the given Cell type.

        :param type: the type of Cell to count
        :return: the number of the given Cell type cells in the board
        """
        sum = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j].value == type:
                    sum += 1
        return sum
