import string
from typing import List

from client.model.cell import Cell
from client.model.game import Game
from client.views.base_page_view import BasePageView


class PlayGamePageView(BasePageView):

    __ABC_ARRAY = list(string.ascii_lowercase)

    def __init__(self, game_obj: Game) -> None:
        """
        Fills in the needed board variables and initializes the current state of the board
        :param game_obj: A specific game object who's attributes will be accessed and displayed.
        """
        super().__init__()
        self._game_obj: Game = game_obj
        self._size: int = game_obj.board.size

    def display(self) -> None:
        self.__display_board()
        self.__display_score()

    def __display_board(self) -> None:
        """
        Prints out the current state of the board.

        In the for loops, row and col loop from 0 to size [0, size] even though the column numbers and row numbers
        go from 0 to 1 - size [0, size). This was done on purpose to make space for the row numbers
        and column letters:
        """
        board: string = ""  # reset board string.
        board_state: List[List[Cell]] = self._game_obj.board.get_state()
        for row in range(0, self._size + 1):
            for col in range(0, self._size + 1):
                if row == 0:
                    if col > 0:
                        board = board + "   " + self.__ABC_ARRAY[col - 1]
                else:  # row > 0
                    if col == 0:
                        board = board + str(row)
                    else:
                        if board_state[row][col].state == "DiskP1":  # [row][col]):
                            board = board + "  P1"
                        elif board_state[row][col].state == "DiskP2":
                            board = board + "  P2"
                        elif board_state[row][col].state == "Invalid":
                            print(
                                "Cell State was Invalid. Error in __constructBoard function of GameView"
                            )
                        elif board_state[row][col].state == "Empty":
                            board = board + "  __"
                if col == self._size - 1:
                    board = board + "\n"
        print(board)

    def __display_score(self) -> None:
        """
        Prints out the game's score.
        """
        temp_tuple: tuple = self._game_obj.get_score()
        temp_string0: string = str(temp_tuple[0])
        temp_string1: string = str(temp_tuple[1])
        print("Player 1's score: " + temp_string0)
        print("Player 2's score: " + temp_string1)

    # TODO: move display_winner into the end game view
    def display_winner(self) -> None:
        """
        Prints out the winner of the game.
        """
        winner_string: string = str(self._game_obj.get_winner())
        print("Player " + winner_string + " won the game!")

    def update_game(self, game: Game):
        self._game_obj = game
        self._size = self._game_obj.board.size