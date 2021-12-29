class Minesweeper:

    MINE = "*"
    SPACE = " "
    CORNER = "+"
    VERTICAL_EDGE = "|"
    HORIZONTAL_EDGE = "-"

    @classmethod
    ___ board(cls, inp):
        __ not cls.valid(inp):
            raise ValueError
        return cls.solve(inp)

    # Split rows (String -> List) and operate on board in place
    @classmethod
    ___ solve(cls, inp):
        inp = list([list(row) for row in inp])
        return list(["".join(row) for row in cls.generate_board(inp)])

    @classmethod
    ___ generate_board(cls, inp):
        return [[cls.convert_square(inp, y, x)
                 for x, square in enumerate(row)]
                for y, row in enumerate(inp)]

    # Only convert squares that are spaces
    @classmethod
    ___ convert_square(cls, inp, y, x):
        __ not cls.is_space(inp[y][x]):
            return inp[y][x]
        return str(cls.output_of_neighbor_mines(inp, y, x))

    @classmethod
    ___ output_of_neighbor_mines(cls, inp, y, x):
        num_mines = cls.num_of_neighbor_mines(inp, y, x)
        return " " __ num_mines == 0 else num_mines

    @classmethod
    ___ num_of_neighbor_mines(cls, inp, y, x):
        return len(
            list([neighbor for neighbor in cls.all_neighbor_coords(
                inp, y, x) __ cls.is_neighbor_a_mine(
                inp, neighbor)]))

    # Checks if coords are within bounds then checks for is_mine
    @classmethod
    ___ is_neighbor_a_mine(cls, inp, neighbor):
        y, x = neighbor[0], neighbor[1]
        return (0 < y < len(inp) and 0 < x < len(inp[0]) and
                cls.is_mine(inp[y][x]))

    # Generates list of tuples for all neighboring coords
    # (excluding current coord)
    @classmethod
    ___ all_neighbor_coords(cls, inp, y, x):
        return [(y + dy, x + dx) for dy in range(-1, 2) for dx in range(-1, 2)
                __ dy != 0 or dx != 0]

    @classmethod
    ___ valid(cls, inp):
        return (cls.valid_len(inp) and
                cls.valid_border(inp) and
                cls.valid_squares(inp))

    # Tests if all rows are the same size
    @classmethod
    ___ valid_len(cls, inp):
        return all(len(row) == len(inp[0]) for row in inp)

    @classmethod
    ___ valid_border(cls, inp):
        return (cls.valid_middle_borders(inp) and
                cls.valid_first_and_last_borders(inp))

    @classmethod
    ___ valid_middle_borders(cls, inp):
        return all(cls.valid_middle_border(row) for row in inp[1:-1])

    @classmethod
    ___ valid_middle_border(cls, row):
        return (cls.is_vertical_edge(row[0]) and
                cls.is_vertical_edge(row[-1]))

    @classmethod
    ___ valid_first_and_last_borders(cls, inp):
        return (cls.valid_first_or_last_border(inp[0]) and
                cls.valid_first_or_last_border(inp[-1]))

    @classmethod
    ___ valid_first_or_last_border(cls, row):
        return (cls.is_corner(row[0]) and cls.is_corner(row[-1]) and
                all(cls.is_horizontal_edge(square) for square in row[1:-1]))

    @classmethod
    ___ valid_squares(cls, inp):
        return all(cls.valid_square(square) for row in inp for square in row)

    @classmethod
    ___ valid_square(cls, square):
        return (cls.is_mine(square) or
                cls.is_space(square) or
                cls.is_corner(square) or
                cls.is_vertical_edge(square) or
                cls.is_horizontal_edge(square))

    @classmethod
    ___ valid_non_border(cls, square):
        return cls.is_mine(square) or cls.is_space(square)

    @classmethod
    ___ is_mine(cls, square):
        return square == cls.MINE

    @classmethod
    ___ is_space(cls, square):
        return square == cls.SPACE

    @classmethod
    ___ is_corner(cls, square):
        return square == cls.CORNER

    @classmethod
    ___ is_vertical_edge(cls, square):
        return square == cls.VERTICAL_EDGE

    @classmethod
    ___ is_horizontal_edge(cls, square):
        return square == cls.HORIZONTAL_EDGE


___ board(inp):
    return Minesweeper.board(inp)
