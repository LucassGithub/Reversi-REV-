from typing import List, Optional

from client.model.cell import Cell, CellState


class Board:
    def __init__(
        self, size: int, saved_state: Optional[List[List[int]]] = None
    ) -> None:
        self.size: int = size
        if saved_state is None:
            self.cells: List[List[Cell]] = [
                [Cell(CellState.empty) for _ in range(size)] for _ in range(size)
            ]
            # initialize the four starting disks at the center of the board
            self.cells[size // 2][size // 2 - 1].state = CellState.player1
            self.cells[size // 2 - 1][size // 2].state = CellState.player1
            self.cells[size // 2 - 1][size // 2 - 1].state = CellState.player2
            self.cells[size // 2][size // 2].state = CellState.player2
        else:
            self.cells = [
                [Cell(CellState(saved_state[j][i])) for i in range(self.size)]
                for j in range(self.size)
            ]

    def get_state(self) -> List[List[CellState]]:
        """
        Get the current state of the board, the cells field.

        :return: cells
        """
        return [[cell.state for cell in row] for row in self.cells]

    def get_num_type(self, cell_state: CellState) -> int:
        """
        Get the number of cells in the board that are of the given Cell type.

        :param cell_state: the type of CellState to count
        :return: the number of the given Cell type cells in the board
        """
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j].state == cell_state:
                    count += 1
        return count

    def is_valid_posn(self, x: int, y: int) -> bool:
        """
        Checks if the given x,y coordinate is within the board of Cells.

        :param x: the x coordinate
        :param y: the y coordinate
        :return: True if the x,y coordinate is on the board, else False
        """
        return (x in range(self.size)) and (y in range(self.size))
