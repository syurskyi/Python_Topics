______ u__
____ circle ______ circle_area
____ circle ______ circle_circumfrence
____ math ______ pi

# https://www.youtube.com/watch?v=1Lfv5tUGsn8

c_ TestCircleArea?.?
    ___ test_area
        # Tests to confirm that it calculates the area as expected
        aAE..(circle_area(0),0)
        aAE..(circle_area(2), pi*(2**2))
        aAE..(circle_area(3.145),pi*(3.145**2))
    
    ___ test_area_types
        # Test to make sure the correct type is entered into the function
        aR..(T.., circle_area, "Text")
        aR..(T.., circle_area, T..)
        aR..(T.., circle_area, 5+3j)

    ___ test_area_values
        # Test to make sure the incorrect value hasnt been entered
        aR..(V.., circle_area, -3)

    ___ test_circumfrence
        # Tests circumfrence to expected val
        aAE..(circle_circumfrence(0), 0)
        aAE..(circle_circumfrence(2), 2*pi*2)
        aAE..(circle_circumfrence(3.14556445), 3.14556445*pi*2)

    ___ test_circumfrence_types
        # Test circumfrence input to make sure errors handled
        aR..(T.., circle_circumfrence, "Text")
        aR..(T.., circle_circumfrence, T..)
        aR..(T.., circle_circumfrence, 3+4j)

    ___ test_circumfrence_values
        # Test to insure proper type is entered into value
        aR..(V.., circle_circumfrence, -3)
        aR..(V.., circle_circumfrence, -99.23545)







