____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc

____ .engine ______ TicTacToeEngine
____ .board ______ TTTBoard


c_ MainWindow(qtw.?MW..):

    ___  -
        """MainWindow constructor."""
        s_. - ()
        # Main UI code goes here
        board _ TTTBoard()
        board_view _ qtw.QGraphicsView()
        board_view.setScene(board)
        sCW..(board_view)
        start_game()
        board.square_clicked.c..(try_mark)
        # End main UI code
        s..

    ___ start_game
        """Clear the board and begin a new game"""
        board.clear_board()
        game _ TicTacToeEngine()
        game.game_won.c..(game_won)
        game.game_draw.c..(game_draw)

    ___ try_mark  square):
        """Attempt to mark a square"""
        __ game.mark_square(square):
            board.set_board(game.board)
            game.check_board()

    ___ game_won  player):
        """Display the winner and start a new game"""
        qtw.?MB...i..(
            N.., 'Game Won', f'Player {player} Won!')
        start_game()

    ___ game_draw
        """Display the lack of a winner and start a new game"""
        qtw.?MB...i..(
            N.., 'Game Over', 'Game Over.  Nobody Won...')
        start_game()
