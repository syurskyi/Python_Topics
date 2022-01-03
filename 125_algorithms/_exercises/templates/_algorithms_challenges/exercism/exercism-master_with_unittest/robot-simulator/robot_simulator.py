c_ NORTH:
    @staticmethod
    ___ advance(self, x, y):
        r.. (x, y + 1)

    @staticmethod
    ___ turn_right
        r.. EAST

    @staticmethod
    ___ turn_left
        r.. WEST


c_ EAST:
    @staticmethod
    ___ advance(self, x, y):
        r.. (x + 1, y)

    @staticmethod
    ___ turn_right
        r.. SOUTH

    @staticmethod
    ___ turn_left
        r.. NORTH


c_ SOUTH:
    @staticmethod
    ___ advance(self, x, y):
        r.. (x, y - 1)

    @staticmethod
    ___ turn_right
        r.. WEST

    @staticmethod
    ___ turn_left
        r.. EAST


c_ WEST:
    @staticmethod
    ___ advance(self, x, y):
        r.. (x - 1, y)

    @staticmethod
    ___ turn_right
        r.. NORTH

    @staticmethod
    ___ turn_left
        r.. SOUTH


c_ Robot:

    ___ - , direction=NORTH, x=0, y=0):
        coordinates = (x, y)
        bearing = direction

    ___ advance
        coordinates = bearing.advance(bearing,
                                                x(), y())

    ___ turn_right
        bearing = bearing.turn_right(bearing)

    ___ turn_left
        bearing = bearing.turn_left(bearing)

    ___ simulate(self, instructions):
        ___ i __ instructions:
            execute_instruction(i)

    ___ execute_instruction(self, i):
        __ i __ 'A':
            advance()
        ____ i __ 'L':
            turn_left()
        ____ i __ 'R':
            turn_right()

    ___ x
        r.. coordinates[0]

    ___ y
        r.. coordinates[1]
