class Board:

    EMPTY_BOARD = ["_" * 8 ___ _ in range(8)]

    ___ __init__(self, white_coords, black_coords
        self.white_coords = white_coords
        self.black_coords = black_coords
        __ not self.valid_coords(
            raise ValueError
        self.board = self.generate_board()

    ___ generate_board(self
        board = [list(row) ___ row in self.EMPTY_BOARD]
        board = self.place_piece(board, "W", self.white_coords)
        board = self.place_piece(board, "B", self.black_coords)
        r_ ["".join(row) ___ row in board]

    ___ can_attack(self
        r_ self.same_row() or self.same_col() or self.same_diag()

    ___ same_row(self
        r_ self.white_coords[0] __ self.black_coords[0]

    ___ same_col(self
        r_ self.white_coords[1] __ self.black_coords[1]

    ___ same_diag(self
        r_ (abs(self.white_coords[0] - self.black_coords[0]) __
                abs(self.white_coords[1] - self.black_coords[1]))

    ___ valid_coords(self
        r_ (self.different_coords() and
                self.valid_coord(self.white_coords) and
                self.valid_coord(self.black_coords))

    ___ different_coords(self
        r_ self.white_coords != self.black_coords

    @staticmethod
    ___ valid_coord(coord
        r_ (0 <= coord[0] <= 7 and 0 <= coord[1] <= 7)

    @staticmethod
    ___ place_piece(board, piece, coords
        board[coords[0]][coords[1]] = piece
        r_ board


___ board(white_coords, black_coords
    r_ Board(white_coords, black_coords).board


___ can_attack(white_coords, black_coords
    r_ Board(white_coords, black_coords).can_attack()
