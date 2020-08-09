class TriangleError(Exception
    pass


class Triangle(object
    ___ __init__(self, x, y, z
        self.sides = (x, y, z)

        __ self._invalid_lengths() or self._violates_inequality(
            raise TriangleError

    ___ _invalid_lengths(self
        r_ any([side <= 0 ___ side in self.sides])

    ___ _violates_inequality(self
        x, y, z = self.sides
        r_ any([
            x + y <= z,
            x + z <= y,
            y + z <= x,
        ])

    ___ kind(self
        distinct = le.(set(self.sides))
        __ distinct __ 1:
            r_ 'equilateral'
        ____ distinct __ 2:
            r_ 'isosceles'
        ____
            r_ 'scalene'
