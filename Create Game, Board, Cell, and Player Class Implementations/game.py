import uuid


class Game:
    def __init__(self, user1: User, user2: User):
        self.id: int = id(self)
        self.board: Board = board
        self.rules: [ARules] = user1.pref.rules
        self.players: Player[2] = Player[Player(user1), Player(user2)]
        self.curr_player: int = 0
        self.save: Bool = True

    # implement another constructor for playing vs AI (one user provided)
    # def __int__(self, user: User):

    def is_game_over(self) -> Bool:
        """
        Check if the board has no empty spaces, no player1 disks, or no player2 disks.
        These are the states in which the game ends.

        :return: true if the game is over (no more turns can be made by one or both players), otherwise false
        """
        return (self.board.get_num_type(0) == 0) | (self.board.get_num_type(1) == 0) | (self.board.get_num_type(2) == 0)

    def place_tile(self, posn: tuple) -> Bool:
        """
        Place a tile on the given position of the board for the currently active player
        if the position is on the board and the move is valid according to the rules.

        :param posn: the position on the board to place a disk
        :raises Exception: Thrown when the given position is not on the board
        :return: True if the move was successfully completed, or false if it was invalid
        """
        if posn[0] < 0 | posn[0] >= self.board.size | posn[1] < 0 | posn[1] >= self.board.size:
            raise Exception("out-of bounds move attempted")
        if not self.rules.isValidMove(self.curr_player, posn, self.board):
            return False
        self.board.cells[posn[0]][posn[1]] = self.board.cells[posn[0]][posn[1]].fill(self.curr_player)
        self.curr_player = 0 if self.curr_player == 1 else 1
        return True

    def get_valid_moves(self) -> Bool[self.board.size][self.board.size]:
        """
        Get a board sized 2-D array of booleans. The boolean values represent whether a move on
        the board at that position is valid for the currently active player.

        :return: a 2-D array of booleans representing the locations of valid moves for the current player
        """
        for i in self.board.size:
            for j in self.board.size:
                validMoves[i][j] = 1 if self.rules.isValidMove(self.curr_player, tuple(i, j), self.board) else 0
        return validMoves

    def get_winner(self) -> int:
        """
        Get the int representing the player who has more disks on the board.
        (0 for player1, 1 for player2)

        :raises Exception: Thrown when the method is called before the game has ended
        :return: the number representing the winning player
        """
        if not Game.is_game_over(self):
            raise Exception("cannot get winner until game is over")
        if self.board.get_num_type(0) > self.board.get_num_type(1):
            return 0
        else:
            return 1

    def get_score(self) -> int[2]:
        """
        Get the scores for each player.

        :return: a tuple containing the scores for the two respective players
        """
        return tuple(self.board.get_num_type(0), self.board.get_num_type(1))

    # def forfeit(self):
