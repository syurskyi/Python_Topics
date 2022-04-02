c_ Board:

    EMPTY_BOARD = ["_" * 8 ___ _ __ r..(8)]

    ___ - , white_coords, black_coords
        white_coords = white_coords
        black_coords = black_coords
        __ n.. valid_coords
            r.. ValueError
        board = generate_board()

    ___ generate_board
        board = [l..(row) ___ row __ EMPTY_BOARD]
        board = place_piece(board, "W", white_coords)
        board = place_piece(board, "B", black_coords)
        r.. ["".j..(row) ___ row __ board]

    ___ can_attack
        r.. same_row() o. same_col() o. same_diag()

    ___ same_row
        r.. white_coords[0] __ black_coords[0]

    ___ same_col
        r.. white_coords[1] __ black_coords[1]

    ___ same_diag
        r.. (abs(white_coords[0] - black_coords[0]) __
                abs(white_coords[1] - black_coords[1]))

    ___ valid_coords
        r.. (different_coords() a..
                valid_coord(white_coords) a..
                valid_coord(black_coords))

    ___ different_coords
        r.. white_coords != black_coords

    @staticmethod
    ___ valid_coord(coord
        r.. (0 <= coord[0] <= 7 a.. 0 <= coord[1] <= 7)

    @staticmethod
    ___ place_piece(board, piece, coords
        board[coords[0]][coords[1]] = piece
        r.. board


___ board(white_coords, black_coords
    r.. Board(white_coords, black_coords).board


___ can_attack(white_coords, black_coords
    r.. Board(white_coords, black_coords).can_attack()
