______ u__
____ circles ______ circle_area
____ math ______ pi

c_ TestCircleArea?.?
    ___ test_area
        # Test areas when radius >= 0
        aAE..(circle_area(1),pi)
        aAE..(circle_area(0),0)
        aAE..(circle_area(2.1), pi*2.1**2)

    ___ test_values
        aR..(V.., circle_area, -2)

    ___ test_types
        aR..(TypeError, circle_area, 3+5j)
        aR..(TypeError, circle_area, T..)
        aR..(TypeError, circle_area, "radius")