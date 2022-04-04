c_ TriangleError(E..
    p..


c_ Triangle(o..
    ___ - , x, y, z
        sides = (x, y, z)

        __ _invalid_lengths() o. _violates_inequality
            r.. TriangleError

    ___ _invalid_lengths
        r.. any([side <_ 0 ___ side __ sides])

    ___ _violates_inequality
        x, y, z = sides
        r.. any([
            x + y <_ z,
            x + z <_ y,
            y + z <_ x,
        ])

    ___ kind
        distinct = l..(s..(sides
        __ distinct __ 1:
            r.. 'equilateral'
        ____ distinct __ 2:
            r.. 'isosceles'
        ____
            r.. 'scalene'
