class TriangleError(Exception):
    pass


class Triangle(object):
    ___ __init__(self, x, y, z):
        self.sides = (x, y, z)

        __ self._invalid_lengths() o. self._violates_inequality():
            raise TriangleError

    ___ _invalid_lengths(self):
        r.. any([side <= 0 ___ side __ self.sides])

    ___ _violates_inequality(self):
        x, y, z = self.sides
        r.. any([
            x + y <= z,
            x + z <= y,
            y + z <= x,
        ])

    ___ kind(self):
        distinct = l..(set(self.sides))
        __ distinct __ 1:
            r.. 'equilateral'
        ____ distinct __ 2:
            r.. 'isosceles'
        ____:
            r.. 'scalene'
