______ u__
____ circle ______ circle_area
____ circle ______ circle_circumfrence
____ math ______ pi

# https://www.youtube.com/watch?v=1Lfv5tUGsn8

c_ TestCircleArea?.?
    ___ test_area
        # Tests to confirm that it calculates the area as expected
        assertAlmostEqual(circle_area(0),0)
        assertAlmostEqual(circle_area(2), pi*(2**2))
        assertAlmostEqual(circle_area(3.145),pi*(3.145**2))
    
    ___ test_area_types
        # Test to make sure the correct type is entered into the function
        assertRaises(TypeError, circle_area, "Text")
        assertRaises(TypeError, circle_area, T..)
        assertRaises(TypeError, circle_area, 5+3j)

    ___ test_area_values
        # Test to make sure the incorrect value hasnt been entered
        assertRaises(V.., circle_area, -3)

    ___ test_circumfrence
        # Tests circumfrence to expected val
        assertAlmostEqual(circle_circumfrence(0), 0)      
        assertAlmostEqual(circle_circumfrence(2), 2*pi*2)
        assertAlmostEqual(circle_circumfrence(3.14556445), 3.14556445*pi*2)

    ___ test_circumfrence_types
        # Test circumfrence input to make sure errors handled
        assertRaises(TypeError, circle_circumfrence, "Text")
        assertRaises(TypeError, circle_circumfrence, T..)
        assertRaises(TypeError, circle_circumfrence, 3+4j)

    ___ test_circumfrence_values
        # Test to insure proper type is entered into value
        assertRaises(V.., circle_circumfrence, -3)
        assertRaises(V.., circle_circumfrence, -99.23545)







