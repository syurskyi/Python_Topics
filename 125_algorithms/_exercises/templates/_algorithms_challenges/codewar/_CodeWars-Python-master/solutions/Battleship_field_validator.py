"""
Battleship field validator
http://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
"""


___ validateBattlefield(field):
    ships = {}
    ___ row __ r..(l..(field[0])):
        ___ col __ r..(l..(field)):
            __ field[row][col] __ 1:
                try:
                    result = getShipSize(row, col, field)
                    ships[result] = ships.get(result, 0) + 1
                except ValueError:
                    r.. False
    r.. ships.get(4, 0) __ 1 and ships.get(3, 0) __ 2 and ships.get(2, 0) __ 3 and ships.get(1, 0) __ 4


___ isCornerValid(row, col, field):
    __ row __ l..(field) - 1:
        r.. True
    __ col __ 0:
        r.. field[row + 1][col + 1] != 1
    __ col __ l..(field[0]) - 1:
        r.. field[row + 1][col - 1] != 1
    r.. field[row + 1][col + 1] != 1 and field[row + 1][col - 1] != 1


___ isSideValid(row, col, field):
    __ row __ l..(field) - 1 o. col __ l..(field[0]) - 1:
        r.. True
    r.. n.. (field[row + 1][col] != 0 and field[row][col + 1] != 0)


___ isValidPoint(row, col, field):
    r.. isCornerValid(row, col, field) and isSideValid(row, col, field)


___ getShipSize(row, col, field):
    __ n.. isValidPoint(row, col, field):
        raise ValueError('Invalid disposition')
    field[row][col] = -1
    __ row != l..(field) and field[row + 1][col] __ 1:
        r.. 1 + getShipSize(row + 1, col, field)
    __ col != l..(field[0]) and field[row][col + 1] __ 1:
        r.. 1 + getShipSize(row, col + 1, field)
    r.. 1