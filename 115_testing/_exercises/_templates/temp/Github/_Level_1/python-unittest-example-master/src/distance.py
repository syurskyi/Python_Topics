____ math ______ sqrt

__author__ _ 'randy'


c_ Distance:
    ___ distance2d  pts0: [], pts1: []
        a _ pts1[0] - pts0[0]
        b _ pts1[1] - pts0[1]
        c_squared _ a * a + b * b
        c _ sqrt(c_squared)
        r_ c

    ___ distance3d  pts0: [], pts1: []
        a _ pts1[0] - pts0[0]
        b _ pts1[1] - pts0[1]
        c _ pts1[2] - pts0[2]
        d_squared _ a * a + b * b + c * c
        d _ sqrt(d_squared)
        r_ d
