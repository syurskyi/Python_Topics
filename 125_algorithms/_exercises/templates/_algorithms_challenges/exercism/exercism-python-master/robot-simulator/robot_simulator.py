# NORTH, EAST, SOUTH, WEST are directions a robot can face
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

class Robot:
    """Robot is a simulation of a robot"""

    # Commands that the robot can be given
    _valid_commdands = {
        'R': 'turn_right',
        'L': 'turn_left',
        'A': 'advance',
    }

    ___ __init__(self, bearing=NORTH, x=0, y=0
        """__init__ creates the robot, defaults to facing north at the origin"""
        self.bearing = bearing
        self.coordinates = (x, y)

    ___ turn_right(self
        """turn_right turns the robot to the right"""
        self.bearing = (self.bearing + 1) % 4

    ___ turn_left(self
        """turn_left turns the robot to the left"""
        for _ in range(3
            self.turn_right()

    ___ advance(self
        """advance moves the robot one spce forward in the direction it's facing"""
        x, y = self.coordinates
        __ self.bearing __ NORTH:
            self.coordinates = (x, y+1)
        ____ self.bearing __ SOUTH:
            self.coordinates = (x, y-1)
        ____ self.bearing __ EAST:
            self.coordinates = (x+1, y)
        ____ self.bearing __ WEST:
            self.coordinates = (x-1, y)

    ___ simulate(self, commands
        """simulate give the robot a set of commands"""
        for c in commands:
            getattr(self, Robot._valid_commdands[c])()

