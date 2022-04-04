c_ Triangle:

    EQUILATERAL = "equilateral"
    ISOSCELES = "isosceles"
    SCALENE = "scalene"

    ___ - , a, b, c
        a = a
        b = b
        c = c
        __ error
            r.. TriangleError

    ___ kind
        __ equilateral
            r.. EQUILATERAL
        __ isosceles
            r.. ISOSCELES
        r.. SCALENE

    ___ equilateral
        r.. a __ b __ c

    ___ isosceles
        r.. a __ b o. b __ c o. a __ c

    ___ error
        r.. negative_sides() o. triangle_inequality()

    ___ negative_sides
        r.. a <_ 0 o. b <_ 0 o. c <_ 0

    ___ triangle_inequality
        r.. (a + b <_ c o.
                b + c <_ a o.
                a + c <_ b)


c_ TriangleError(E..
    p..
