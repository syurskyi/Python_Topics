____ ? ______ ?C.. __ qtc

c_ TicTacToeEngine(qtc.QObject):
    """Engine for the game Tic Tac Toe"""
    winning_sets _ [
        # Across
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
        # Down
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
        # Diagonal
        {0, 4, 8}, {2, 4, 6}
    ]
    players _ ('X', 'O')

    game_won _ qtc.pyqtSignal(str)
    game_draw _ qtc.pyqtSignal()

    ___ __init__(self):
        super().__init__()
        self.board _ [N..] * 9
        self.current_player _ self.players[0]

    ___ next_player(self):
        self.current_player _ self.players[
            no. self.players.index(self.current_player)]

    ___ mark_square  square):
        """Mark a square for one player or another"""
        __ any([
                no. isinstance(square, int),
                no. (0 <_ square < len(self.board)),
                self.board[square] __ no. N..
        ]):
            r_ False
        self.board[square] _ self.current_player
        self.next_player()
        r_ True

    ___ check_board(self):
        """See if the game is won or a draw"""
        for player in self.players:
            plays _ {
                index for index, value in enumerate(self.board)
                __ value == player
            }
            for win in self.winning_sets:
                __ no. win - plays:  # player has a winning combo
                    self.game_won.emit(player)
                    r_
        __ N.. no. in self.board:
            self.game_draw.emit()
