____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc

____ .engine ______ TicTacToeEngine
____ .board ______ TTTBoard


class MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor."""
        super().__init__()
        # Main UI code goes here
        self.board _ TTTBoard()
        self.board_view _ qtw.QGraphicsView()
        self.board_view.setScene(self.board)
        self.setCentralWidget(self.board_view)
        self.start_game()
        self.board.square_clicked.c..(self.try_mark)
        # End main UI code
        self.s..

    ___ start_game(self):
        """Clear the board and begin a new game"""
        self.board.clear_board()
        self.game _ TicTacToeEngine()
        self.game.game_won.c..(self.game_won)
        self.game.game_draw.c..(self.game_draw)

    ___ try_mark(self, square):
        """Attempt to mark a square"""
        if self.game.mark_square(square):
            self.board.set_board(self.game.board)
            self.game.check_board()

    ___ game_won(self, player):
        """Display the winner and start a new game"""
        qtw.QMessageBox.information(
            None, 'Game Won', f'Player {player} Won!')
        self.start_game()

    ___ game_draw(self):
        """Display the lack of a winner and start a new game"""
        qtw.QMessageBox.information(
            None, 'Game Over', 'Game Over.  Nobody Won...')
        self.start_game()
