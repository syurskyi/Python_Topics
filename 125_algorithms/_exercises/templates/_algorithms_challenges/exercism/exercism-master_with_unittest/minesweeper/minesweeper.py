c_ Minesweeper:

    MINE "*"
    SPACE " "
    CORNER "+"
    VERTICAL_EDGE "|"
    HORIZONTAL_EDGE "-"

    @classmethod
    ___ board(cls, inp
        __ n.. cls.valid(inp
            r.. V...
        r.. cls.solve(inp)

    # Split rows (String -> List) and operate on board in place
    @classmethod
    ___ solve(cls, inp
        inp l..([l..(row) ___ row __ inp])
        r.. l..(["".j..(row) ___ row __ cls.generate_board(inp)])

    @classmethod
    ___ generate_board(cls, inp
        r.. [[cls.convert_square(inp, y, x)
                 ___ x, square __ e..(row)]
                ___ y, row __ e..(inp)]

    # Only convert squares that are spaces
    @classmethod
    ___ convert_square(cls, inp, y, x
        __ n.. cls.is_space(inp[y][x]
            r.. inp[y][x]
        r.. s..(cls.output_of_neighbor_mines(inp, y, x

    @classmethod
    ___ output_of_neighbor_mines(cls, inp, y, x
        num_mines cls.num_of_neighbor_mines(inp, y, x)
        r.. " " __ num_mines __ 0 ____ num_mines

    @classmethod
    ___ num_of_neighbor_mines(cls, inp, y, x
        r.. l..(
            l..([neighbor ___ neighbor __ cls.all_neighbor_coords(
                inp, y, x) __ cls.is_neighbor_a_mine(
                inp, neighbor)]

    # Checks if coords are within bounds then checks for is_mine
    @classmethod
    ___ is_neighbor_a_mine(cls, inp, neighbor
        y, x neighbor[0], neighbor[1]
        r.. (0 < y < l..(inp) a.. 0 < x < l..(inp[0]) a..
                cls.is_mine(inp[y][x]

    # Generates list of tuples for all neighboring coords
    # (excluding current coord)
    @classmethod
    ___ all_neighbor_coords(cls, inp, y, x
        r.. [(y + dy, x + dx) ___ dy __ r..(-1, 2) ___ dx __ r..(-1, 2)
                __ dy !_ 0 o. dx !_ 0]

    @classmethod
    ___ valid(cls, inp
        r.. (cls.valid_len(inp) a..
                cls.valid_border(inp) a..
                cls.valid_squares(inp

    # Tests if all rows are the same size
    @classmethod
    ___ valid_len(cls, inp
        r.. a..(l..(row) __ l..(inp[0]) ___ row __ inp)

    @classmethod
    ___ valid_border(cls, inp
        r.. (cls.valid_middle_borders(inp) a..
                cls.valid_first_and_last_borders(inp

    @classmethod
    ___ valid_middle_borders(cls, inp
        r.. a..(cls.valid_middle_border(row) ___ row __ inp[1:-1])

    @classmethod
    ___ valid_middle_border(cls, row
        r.. (cls.is_vertical_edge(row[0]) a..
                cls.is_vertical_edge(row[-1]

    @classmethod
    ___ valid_first_and_last_borders(cls, inp
        r.. (cls.valid_first_or_last_border(inp[0]) a..
                cls.valid_first_or_last_border(inp[-1]

    @classmethod
    ___ valid_first_or_last_border(cls, row
        r.. (cls.is_corner(row[0]) a.. cls.is_corner(row[-1]) a..
                a..(cls.is_horizontal_edge(square) ___ square __ row[1:-1]

    @classmethod
    ___ valid_squares(cls, inp
        r.. a..(cls.valid_square(square) ___ row __ inp ___ square __ row)

    @classmethod
    ___ valid_square(cls, square
        r.. (cls.is_mine(square) o.
                cls.is_space(square) o.
                cls.is_corner(square) o.
                cls.is_vertical_edge(square) o.
                cls.is_horizontal_edge(square

    @classmethod
    ___ valid_non_border(cls, square
        r.. cls.is_mine(square) o. cls.is_space(square)

    @classmethod
    ___ is_mine(cls, square
        r.. square __ cls.MINE

    @classmethod
    ___ is_space(cls, square
        r.. square __ cls.SPACE

    @classmethod
    ___ is_corner(cls, square
        r.. square __ cls.CORNER

    @classmethod
    ___ is_vertical_edge(cls, square
        r.. square __ cls.VERTICAL_EDGE

    @classmethod
    ___ is_horizontal_edge(cls, square
        r.. square __ cls.HORIZONTAL_EDGE


___ board(inp
    r.. Minesweeper.board(inp)
