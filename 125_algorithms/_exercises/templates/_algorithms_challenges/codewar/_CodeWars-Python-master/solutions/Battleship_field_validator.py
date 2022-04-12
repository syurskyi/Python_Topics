"""
Battleship field validator
http://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
"""


___ validateBattlefield(field
    ships    # dict
    ___ row __ r..(l..(field[0]:
        ___ col __ r..(l..(field:
            __ field[row][col] __ 1:
                ___
                    result getShipSize(row, col, field)
                    ships[result] ships.g.. result, 0) + 1
                ______ V..
                    r.. F..
    r.. ships.g.. 4, 0) __ 1 a.. ships.g.. 3, 0) __ 2 a.. ships.g.. 2, 0) __ 3 a.. ships.g.. 1, 0) __ 4


___ isCornerValid(row, col, field
    __ row __ l..(field) - 1:
        r.. T..
    __ col __ 0:
        r.. field[row + 1][col + 1] !_ 1
    __ col __ l..(field 0 - 1:
        r.. field[row + 1][col - 1] !_ 1
    r.. field[row + 1][col + 1] !_ 1 a.. field[row + 1][col - 1] !_ 1


___ isSideValid(row, col, field
    __ row __ l..(field) - 1 o. col __ l..(field 0 - 1:
        r.. T..
    r.. n.. (field[row + 1][col] !_ 0 a.. field[row][col + 1] !_ 0)


___ isValidPoint(row, col, field
    r.. isCornerValid(row, col, field) a.. isSideValid(row, col, field)


___ getShipSize(row, col, field
    __ n.. isValidPoint(row, col, field
        r.. V...('Invalid disposition')
    field[row][col] -1
    __ row !_ l..(field) a.. field[row + 1][col] __ 1:
        r.. 1 + getShipSize(row + 1, col, field)
    __ col !_ l..(field 0 a.. field[row][col + 1] __ 1:
        r.. 1 + getShipSize(row, col + 1, field)
    r.. 1