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
            r.. self.EQUILATERAL
        __ self.isosceles():
            r.. self.ISOSCELES
        r.. self.SCALENE

    ___ equilateral(self):
        r.. self.a __ self.b __ self.c

    ___ isosceles(self):
        r.. self.a __ self.b o. self.b __ self.c o. self.a __ self.c

    ___ error(self):
        r.. self.negative_sides() o. self.triangle_inequality()

    ___ negative_sides(self):
        r.. self.a <= 0 o. self.b <= 0 o. self.c <= 0

    ___ triangle_inequality(self):
        r.. (self.a + self.b <= self.c o.
                self.b + self.c <= self.a o.
                self.a + self.c <= self.b)


class TriangleError(Exception):
    pass
