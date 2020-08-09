class Minesweeper:

    MINE = "*"
    SPACE = " "
    CORNER = "+"
    VERTICAL_EDGE = "|"
    HORIZONTAL_EDGE = "-"

    @classmethod
    ___ board(cls, inp
        __ not cls.valid(inp
            raise ValueError
        r_ cls.solve(inp)

    # Split rows (String -> List) and operate on board in place
    @classmethod
    ___ solve(cls, inp
        inp = list([list(row) ___ row in inp])
        r_ list(["".join(row) ___ row in cls.generate_board(inp)])

    @classmethod
    ___ generate_board(cls, inp
        r_ [[cls.convert_square(inp, y, x)
                 ___ x, square in enumerate(row)]
                ___ y, row in enumerate(inp)]

    # Only convert squares that are spaces
    @classmethod
    ___ convert_square(cls, inp, y, x
        __ not cls.is_space(inp[y][x]
            r_ inp[y][x]
        r_ str(cls.output_of_neighbor_mines(inp, y, x))

    @classmethod
    ___ output_of_neighbor_mines(cls, inp, y, x
        num_mines = cls.num_of_neighbor_mines(inp, y, x)
        r_ " " __ num_mines __ 0 else num_mines

    @classmethod
    ___ num_of_neighbor_mines(cls, inp, y, x
        r_ le.(
            list([neighbor ___ neighbor in cls.all_neighbor_coords(
                inp, y, x) __ cls.is_neighbor_a_mine(
                inp, neighbor)]))

    # Checks if coords are within bounds then checks for is_mine
    @classmethod
    ___ is_neighbor_a_mine(cls, inp, neighbor
        y, x = neighbor[0], neighbor[1]
        r_ (0 < y < le.(inp) and 0 < x < le.(inp[0]) and
                cls.is_mine(inp[y][x]))

    # Generates list of tuples for all neighboring coords
    # (excluding current coord)
    @classmethod
    ___ all_neighbor_coords(cls, inp, y, x
        r_ [(y + dy, x + dx) ___ dy in range(-1, 2) ___ dx in range(-1, 2)
                __ dy != 0 or dx != 0]

    @classmethod
    ___ valid(cls, inp
        r_ (cls.valid_len(inp) and
                cls.valid_border(inp) and
                cls.valid_squares(inp))

    # Tests if all rows are the same size
    @classmethod
    ___ valid_len(cls, inp
        r_ all(le.(row) __ le.(inp[0]) ___ row in inp)

    @classmethod
    ___ valid_border(cls, inp
        r_ (cls.valid_middle_borders(inp) and
                cls.valid_first_and_last_borders(inp))

    @classmethod
    ___ valid_middle_borders(cls, inp
        r_ all(cls.valid_middle_border(row) ___ row in inp[1:-1])

    @classmethod
    ___ valid_middle_border(cls, row
        r_ (cls.is_vertical_edge(row[0]) and
                cls.is_vertical_edge(row[-1]))

    @classmethod
    ___ valid_first_and_last_borders(cls, inp
        r_ (cls.valid_first_or_last_border(inp[0]) and
                cls.valid_first_or_last_border(inp[-1]))

    @classmethod
    ___ valid_first_or_last_border(cls, row
        r_ (cls.is_corner(row[0]) and cls.is_corner(row[-1]) and
                all(cls.is_horizontal_edge(square) ___ square in row[1:-1]))

    @classmethod
    ___ valid_squares(cls, inp
        r_ all(cls.valid_square(square) ___ row in inp ___ square in row)

    @classmethod
    ___ valid_square(cls, square
        r_ (cls.is_mine(square) or
                cls.is_space(square) or
                cls.is_corner(square) or
                cls.is_vertical_edge(square) or
                cls.is_horizontal_edge(square))

    @classmethod
    ___ valid_non_border(cls, square
        r_ cls.is_mine(square) or cls.is_space(square)

    @classmethod
    ___ is_mine(cls, square
        r_ square __ cls.MINE

    @classmethod
    ___ is_space(cls, square
        r_ square __ cls.SPACE

    @classmethod
    ___ is_corner(cls, square
        r_ square __ cls.CORNER

    @classmethod
    ___ is_vertical_edge(cls, square
        r_ square __ cls.VERTICAL_EDGE

    @classmethod
    ___ is_horizontal_edge(cls, square
        r_ square __ cls.HORIZONTAL_EDGE


___ board(inp
    r_ Minesweeper.board(inp)
