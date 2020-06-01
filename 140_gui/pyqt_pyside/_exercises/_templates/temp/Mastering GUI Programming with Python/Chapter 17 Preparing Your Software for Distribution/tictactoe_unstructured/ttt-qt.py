"""
PyQt tic-tac-to

"""
______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc
____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc


class TicTacToeEngine(qtc.QObject):
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
        self.board _ [None] * 9
        self.current_player _ self.players[0]

    ___ next_player(self):
        self.current_player _ self.players[
            not self.players.index(self.current_player)]

    ___ mark_square(self, square):
        """Mark a square for one player or another"""
        if any([
                not isinstance(square, int),
                not (0 <_ square < len(self.board)),
                self.board[square] is not None
        ]):
            return False
        self.board[square] _ self.current_player
        self.next_player()
        return True

    ___ check_board(self):
        """See if the game is won or a draw"""
        for player in self.players:
            plays _ {
                index for index, value in enumerate(self.board)
                if value == player
            }
            for win in self.winning_sets:
                if not win - plays:  # player has a winning combo
                    self.game_won.emit(player)
                    return
        if None not in self.board:
            self.game_draw.emit()


class TTTBoard(qtw.QGraphicsScene):

    square_rects _ (
        qtc.QRectF(5, 5, 190, 190),
        qtc.QRectF(205, 5, 190, 190),
        qtc.QRectF(405, 5, 190, 190),
        qtc.QRectF(5, 205, 190, 190),
        qtc.QRectF(205, 205, 190, 190),
        qtc.QRectF(405, 205, 190, 190),
        qtc.QRectF(5, 405, 190, 190),
        qtc.QRectF(205, 405, 190, 190),
        qtc.QRectF(405, 405, 190, 190)
    )

    square_clicked _ qtc.pyqtSignal(int)

    ___ __init__(self):
        super().__init__()
        self.setSceneRect(0, 0, 600, 600)
        self.setBackgroundBrush(qtg.QBrush(qtc.Qt.cyan))
        for square in self.square_rects:
            self.addRect(square, brush_qtg.QBrush(qtc.Qt.white))
        self.mark_pngs _ {
            'X': qtg.QPixmap('X.png'),
            'O': qtg.QPixmap('O.png')
        }
        self.marks _ []

    ___ set_board(self, marks):
        for i, square in enumerate(marks):
            if square in self.mark_pngs:
                mark _ self.addPixmap(self.mark_pngs[square])
                mark.setPos(self.square_rects[i].topLeft())
                self.marks.append(mark)

    ___ clear_board(self):
        for mark in self.marks:
            self.removeItem(mark)

    ___ mousePressEvent(self, mouse_event):
        """Handle mouse clicks on the board"""
        position _ mouse_event.buttonDownScenePos(qtc.Qt.LeftButton)
        for square, qrect in enumerate(self.square_rects):
            if qrect.contains(position):
                self.square_clicked.emit(square)
                break

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

if __name__ == '__main__':
    app _ qtw.QApplication(sys.argv)
    mw _ MainWindow()
    sys.exit(app.exec())
