class NORTH:
    @staticmethod
    ___ advance(self, x, y):
        return (x, y + 1)

    @staticmethod
    ___ turn_right(self):
        return EAST

    @staticmethod
    ___ turn_left(self):
        return WEST


class EAST:
    @staticmethod
    ___ advance(self, x, y):
        return (x + 1, y)

    @staticmethod
    ___ turn_right(self):
        return SOUTH

    @staticmethod
    ___ turn_left(self):
        return NORTH


class SOUTH:
    @staticmethod
    ___ advance(self, x, y):
        return (x, y - 1)

    @staticmethod
    ___ turn_right(self):
        return WEST

    @staticmethod
    ___ turn_left(self):
        return EAST


class WEST:
    @staticmethod
    ___ advance(self, x, y):
        return (x - 1, y)

    @staticmethod
    ___ turn_right(self):
        return NORTH

    @staticmethod
    ___ turn_left(self):
        return SOUTH


class Robot:

    ___ __init__(self, direction=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = direction

    ___ advance(self):
        self.coordinates = self.bearing.advance(self.bearing,
                                                self.x(), self.y())

    ___ turn_right(self):
        self.bearing = self.bearing.turn_right(self.bearing)

    ___ turn_left(self):
        self.bearing = self.bearing.turn_left(self.bearing)

    ___ simulate(self, instructions):
        for i in instructions:
            self.execute_instruction(i)

    ___ execute_instruction(self, i):
        __ i == 'A':
            self.advance()
        elif i == 'L':
            self.turn_left()
        elif i == 'R':
            self.turn_right()

    ___ x(self):
        return self.coordinates[0]

    ___ y(self):
        return self.coordinates[1]
