class TriangleError(Exception):
    pass


class Triangle(object):
    ___ __init__(self, x, y, z):
        self.sides = (x, y, z)

        __ self._invalid_lengths() or self._violates_inequality():
            raise TriangleError

    ___ _invalid_lengths(self):
        return any([side <= 0 for side in self.sides])

    ___ _violates_inequality(self):
        x, y, z = self.sides
        return any([
            x + y <= z,
            x + z <= y,
            y + z <= x,
        ])

    ___ kind(self):
        distinct = len(set(self.sides))
        __ distinct == 1:
            return 'equilateral'
        elif distinct == 2:
            return 'isosceles'
        else:
            return 'scalene'
