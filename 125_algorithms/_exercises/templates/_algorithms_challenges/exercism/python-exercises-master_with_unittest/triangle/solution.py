c_ TriangleError(E..):
    p..


c_ Triangle(o..):
    ___ - , x, y, z):
        sides = (x, y, z)

        __ _invalid_lengths() o. _violates_inequality
            r.. TriangleError

    ___ _invalid_lengths
        r.. any([side <= 0 ___ side __ sides])

    ___ _violates_inequality
        x, y, z = sides
        r.. any([
            x + y <= z,
            x + z <= y,
            y + z <= x,
        ])

    ___ kind
        distinct = l..(set(sides))
        __ distinct __ 1:
            r.. 'equilateral'
        ____ distinct __ 2:
            r.. 'isosceles'
        ____:
            r.. 'scalene'
