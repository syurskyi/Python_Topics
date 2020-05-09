______ u__
____ circles ______ circle_area
____ math ______ pi

c_ TestCircleArea?.?
    ___ test_area
        # Test areas when radius >= 0
        assertAlmostEqual(circle_area(1),pi)
        assertAlmostEqual(circle_area(0),0)
        assertAlmostEqual(circle_area(2.1), pi*2.1**2)

    ___ test_values
        assertRaises(ValueError, circle_area, -2)

    ___ test_types
        assertRaises(TypeError, circle_area, 3+5j)
        assertRaises(TypeError, circle_area, True)
        assertRaises(TypeError, circle_area, "radius")