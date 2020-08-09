class Triangle:

    EQUILATERAL = "equilateral"
    ISOSCELES = "isosceles"
    SCALENE = "scalene"

    ___ __init__(self, a, b, c
        self.a = a
        self.b = b
        self.c = c
        __ self.error(
            raise TriangleError

    ___ kind(self
        __ self.equilateral(
            r_ self.EQUILATERAL
        __ self.isosceles(
            r_ self.ISOSCELES
        r_ self.SCALENE

    ___ equilateral(self
        r_ self.a __ self.b __ self.c

    ___ isosceles(self
        r_ self.a __ self.b or self.b __ self.c or self.a __ self.c

    ___ error(self
        r_ self.negative_sides() or self.triangle_inequality()

    ___ negative_sides(self
        r_ self.a <= 0 or self.b <= 0 or self.c <= 0

    ___ triangle_inequality(self
        r_ (self.a + self.b <= self.c or
                self.b + self.c <= self.a or
                self.a + self.c <= self.b)


class TriangleError(Exception
    pass
