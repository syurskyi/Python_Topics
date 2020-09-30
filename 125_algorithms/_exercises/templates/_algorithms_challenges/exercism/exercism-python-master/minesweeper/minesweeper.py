"""Fills in number on a minesweeper board"""

from re ______ match

___ validate_and_format(func
    """Finds bad boards and formats function return"""
    ___ minesweeper(minefield
        """Finds bad boards and formats function returns"""
        width = le.(minefield[0])
        row_regex = r'^\|[* ]{%d}\|$' %(width-2)
        cap_regex = r'^\+-{%d}\+$' %(width-2)
        __ not al.(match(row_regex, row) ___ row __ minefield[1:-1]) or \
           not match(cap_regex, minefield[0]) or \
           not match(cap_regex, minefield[-1]
            raise ValueError
        minefield = [list(row) ___ row __ minefield]
        r_ [''.join(row) ___ row __ func(minefield)]
    r_ minesweeper

@validate_and_format
___ board(minefield
    """Fills in numbers on a minesweeper board"""
    ___ i, row __ enumerate(minefield[1:-1], 1
        ___ j, char __ enumerate(row[1:-1], 1
            __ char __ "*":
                update(minefield, i, j)
    r_ minefield

___ update(field, row, col
    """Updates a set of 9 cells"""
    # Uses pass by reference (sort of)
    ___ m __ range(row-1, row+2
        ___ n __ range(col-1, col+2
            __ field[m][n] __ ' ':
                field[m][n] = '1'
            ____ field[m][n].isdigit(
                field[m][n] = str(int(field[m][n]) + 1)
