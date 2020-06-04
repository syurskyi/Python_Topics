____ ? ______ ?C.. __ qtc

c_ TicTacToeEngine(qtc.?O..):
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

    game_won _ qtc.pS.. st.
    game_draw _ qtc.pS..()

    ___  -
        s_. - ()
        board _ [N..] * 9
        current_player _ players[0]

    ___ next_player
        current_player _ players[
            no. players.index(current_player)]

    ___ mark_square  square):
        """Mark a square for one player or another"""
        __ an.([
                no. isinstance(square, in.),
                no. (0 <_ square < le.(board)),
                board[square] __ no. N..
        ]):
            r_ F..
        board[square] _ current_player
        next_player()
        r_ T..

    ___ check_board
        """See if the game is won or a draw"""
        ___ player __ players:
            plays _ {
                index ___ index, value __ en..(board)
                __ value __ player
            }
            ___ win __ winning_sets:
                __ no. win - plays:  # player has a winning combo
                    game_won.e..(player)
                    r_
        __ N.. no. __ board:
            game_draw.e..()
