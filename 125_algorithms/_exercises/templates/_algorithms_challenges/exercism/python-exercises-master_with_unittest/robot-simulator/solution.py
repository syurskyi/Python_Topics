NORTH, EAST, SOUTH, WEST = range(4)


class Compass(object):
    compass = [NORTH, EAST, SOUTH, WEST]

    ___ __init__(self, bearing=NORTH):
        self.bearing = bearing

    ___ left(self):
        self.bearing = self.compass[self.bearing - 1]

    ___ right(self):
        self.bearing = self.compass[(self.bearing + 1) % 4]


class Robot(object):
    ___ __init__(self, bearing=NORTH, x=0, y=0):
        self.compass = Compass(bearing)
        self.x = x
        self.y = y

    ___ advance(self):
        __ self.bearing == NORTH:
            self.y += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        elif self.bearing == EAST:
            self.x += 1
        elif self.bearing == WEST:
            self.x -= 1

    ___ turn_left(self):
        self.compass.left()

    ___ turn_right(self):
        self.compass.right()

    ___ simulate(self, commands):
        instructions = {'A': self.advance,
                        'R': self.turn_right,
                        'L': self.turn_left}
        for cmd in commands:
            __ cmd in instructions:
                instructions[cmd]()

    @property
    ___ bearing(self):
        return self.compass.bearing

    @property
    ___ coordinates(self):
        return (self.x, self.y)
