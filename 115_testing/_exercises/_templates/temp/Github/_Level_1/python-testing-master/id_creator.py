c_ IdCreator:

    ___ faculty_id  value
        __ no. isi..(value, __.
            r_ TypeError('Only integer values allowed')
        __ value < 0:
            r_ V..('Only positive values allowed')
        __ value __ 0:
            r_ 1
        ____:
            r_ faculty_id(value-1) * value


# Testing without using a framework
__ _____ __ _____
    creator _ IdCreator()
    a.. creator.faculty_id(0) __ 1
    a.. creator.faculty_id(3) __ 6

    ___
        creator.faculty_id(-1)
        a.. 1 __ 0
    _____ V..:
        p..

    ___
        creator.faculty_id('a')
        a.. 1 __ 0
    _____ TypeError:
        p..
