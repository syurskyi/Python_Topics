c_ Minesweeper:

    MINE "*"
    SPACE " "
    CORNER "+"
    VERTICAL_EDGE "|"
    HORIZONTAL_EDGE "-"

    ??
    ___ board(cls, inp
        __ n..  ?.valid(inp
            r.. V...
        r..  ?.solve(inp)

    # Split rows (String -> List) and operate on board in place
    ??
    ___ solve(cls, inp
        inp l..([l..(row) ___ row __ inp])
        r.. l..(["".j..(row) ___ row __  ?.generate_board(inp)])

    ??
    ___ generate_board(cls, inp
        r.. [[ ?.convert_square(inp, y, x)
                 ___ x, square __ e..(row)]
                ___ y, row __ e..(inp)]

    # Only convert squares that are spaces
    ??
    ___ convert_square(cls, inp, y, x
        __ n..  ?.is_space(inp[y][x]
            r.. inp[y][x]
        r.. s.. ?.output_of_neighbor_mines(inp, y, x

    ??
    ___ output_of_neighbor_mines(cls, inp, y, x
        num_mines  ?.num_of_neighbor_mines(inp, y, x)
        r.. " " __ num_mines __ 0 ____ num_mines

    ??
    ___ num_of_neighbor_mines(cls, inp, y, x
        r.. l..(
            l..([neighbor ___ neighbor __  ?.all_neighbor_coords(
                inp, y, x) __  ?.is_neighbor_a_mine(
                inp, neighbor)]

    # Checks if coords are within bounds then checks for is_mine
    ??
    ___ is_neighbor_a_mine(cls, inp, neighbor
        y, x neighbor[0], neighbor[1]
        r.. (0 < y < l..(inp) a.. 0 < x < l..(inp 0 a..
                 ?.is_mine(inp[y][x]

    # Generates list of tuples for all neighboring coords
    # (excluding current coord)
    ??
    ___ all_neighbor_coords(cls, inp, y, x
        r.. [(y + dy, x + dx) ___ dy __ r..(-1, 2) ___ dx __ r..(-1, 2)
                __ dy !_ 0 o. dx !_ 0]

    ??
    ___ valid(cls, inp
        r..  ?.valid_len(inp) a..
                 ?.valid_border(inp) a..
                 ?.valid_squares(inp

    # Tests if all rows are the same size
    ??
    ___ valid_len(cls, inp
        r.. a..(l..(row) __ l..(inp 0 ___ row __ inp)

    ??
    ___ valid_border(cls, inp
        r..  ?.valid_middle_borders(inp) a..
                 ?.valid_first_and_last_borders(inp

    ??
    ___ valid_middle_borders(cls, inp
        r.. a.. ?.valid_middle_border(row) ___ row __ inp[1:-1])

    ??
    ___ valid_middle_border(cls, row
        r..  ?.is_vertical_edge(row 0 a..
                 ?.is_vertical_edge(row[-1]

    ??
    ___ valid_first_and_last_borders(cls, inp
        r..  ?.valid_first_or_last_border(inp 0 a..
                 ?.valid_first_or_last_border(inp[-1]

    ??
    ___ valid_first_or_last_border(cls, row
        r..  ?.is_corner(row 0 a..  ?.is_corner(row[-1]) a..
                a.. ?.is_horizontal_edge(square) ___ square __ row[1:-1]

    ??
    ___ valid_squares(cls, inp
        r.. a.. ?.valid_square(square) ___ row __ inp ___ square __ row)

    ??
    ___ valid_square(cls, square
        r..  ?.is_mine(square) o.
                 ?.is_space(square) o.
                 ?.is_corner(square) o.
                 ?.is_vertical_edge(square) o.
                 ?.is_horizontal_edge(square

    ??
    ___ valid_non_border(cls, square
        r..  ?.is_mine(square) o.  ?.is_space(square)

    ??
    ___ is_mine(cls, square
        r.. square __  ?.MINE

    ??
    ___ is_space(cls, square
        r.. square __  ?.SPACE

    ??
    ___ is_corner(cls, square
        r.. square __  ?.CORNER

    ??
    ___ is_vertical_edge(cls, square
        r.. square __  ?.VERTICAL_EDGE

    ??
    ___ is_horizontal_edge(cls, square
        r.. square __  ?.HORIZONTAL_EDGE


___ board(inp
    r.. Minesweeper.board(inp)
