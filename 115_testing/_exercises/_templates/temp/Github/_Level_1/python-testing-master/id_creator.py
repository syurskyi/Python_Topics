c_ IdCreator:

    ___ faculty_id  value
        __ not isinstance(value, int
            r_ TypeError('Only integer values allowed')
        __ value < 0:
            r_ V..('Only positive values allowed')
        __ value __ 0:
            r_ 1
        else:
            r_ faculty_id(value-1) * value


# Testing without using a framework
__ __name__ __ '__main__':
    creator _ IdCreator()
    a.. creator.faculty_id(0) __ 1
    a.. creator.faculty_id(3) __ 6

    try:
        creator.faculty_id(-1)
        a.. 1 __ 0
    except V..:
        p..

    try:
        creator.faculty_id('a')
        a.. 1 __ 0
    except TypeError:
        p..
