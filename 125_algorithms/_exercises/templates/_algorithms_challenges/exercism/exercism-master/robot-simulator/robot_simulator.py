class NORTH:
    @staticmethod
    ___ advance(self, x, y
        r_ (x, y + 1)

    @staticmethod
    ___ turn_right(self
        r_ EAST

    @staticmethod
    ___ turn_left(self
        r_ WEST


class EAST:
    @staticmethod
    ___ advance(self, x, y
        r_ (x + 1, y)

    @staticmethod
    ___ turn_right(self
        r_ SOUTH

    @staticmethod
    ___ turn_left(self
        r_ NORTH


class SOUTH:
    @staticmethod
    ___ advance(self, x, y
        r_ (x, y - 1)

    @staticmethod
    ___ turn_right(self
        r_ WEST

    @staticmethod
    ___ turn_left(self
        r_ EAST


class WEST:
    @staticmethod
    ___ advance(self, x, y
        r_ (x - 1, y)

    @staticmethod
    ___ turn_right(self
        r_ NORTH

    @staticmethod
    ___ turn_left(self
        r_ SOUTH


class Robot:

    ___ __init__(self, direction=NORTH, x=0, y=0
        self.coordinates = (x, y)
        self.bearing = direction

    ___ advance(self
        self.coordinates = self.bearing.advance(self.bearing,
                                                self.x(), self.y())

    ___ turn_right(self
        self.bearing = self.bearing.turn_right(self.bearing)

    ___ turn_left(self
        self.bearing = self.bearing.turn_left(self.bearing)

    ___ simulate(self, instructions
        ___ i in instructions:
            self.execute_instruction(i)

    ___ execute_instruction(self, i
        __ i __ 'A':
            self.advance()
        ____ i __ 'L':
            self.turn_left()
        ____ i __ 'R':
            self.turn_right()

    ___ x(self
        r_ self.coordinates[0]

    ___ y(self
        r_ self.coordinates[1]
