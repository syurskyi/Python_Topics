______ u__
____ src.distance ______ Distance

__author__ _ 'randy'


c_ TestDistance?.?
    ___ testDistance2d
        dist _ Distance()

        aE..(5, dist.distance2d([0, 0], [3, 4]))
        aAE..(10.296, dist.distance2d([0, 0], [5, 9]), 3)
        aAE..(2.236, dist.distance2d([0, 0], [1, 2]), 3)

    ___ testDistance3d
        dist _ Distance()

        aAE..(7.071, dist.distance3d([0, 0, 0], [3, 4, 5]), 3)
        aAE..(10.488, dist.distance3d([0, 0, 0], [5, 6, 7]), 3)
        aE..(0, dist.distance3d([0, 0, 0], [0, 0, 0]))


__ _____ __ _____
    ?.?
