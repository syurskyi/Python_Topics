class Triangle:

    EQUILATERAL = "equilateral"
    ISOSCELES = "isosceles"
    SCALENE = "scalene"

    ___ __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        __ self.error():
            raise TriangleError

    ___ kind(self):
        __ self.equilateral():
            return self.EQUILATERAL
        __ self.isosceles():
            return self.ISOSCELES
        return self.SCALENE

    ___ equilateral(self):
        return self.a == self.b == self.c

    ___ isosceles(self):
        return self.a == self.b or self.b == self.c or self.a == self.c

    ___ error(self):
        return self.negative_sides() or self.triangle_inequality()

    ___ negative_sides(self):
        return self.a <= 0 or self.b <= 0 or self.c <= 0

    ___ triangle_inequality(self):
        return (self.a + self.b <= self.c or
                self.b + self.c <= self.a or
                self.a + self.c <= self.b)


class TriangleError(Exception):
    pass
