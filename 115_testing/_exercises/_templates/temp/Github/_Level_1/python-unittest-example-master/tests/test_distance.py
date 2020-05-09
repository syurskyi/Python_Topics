______ unittest
____ src.distance ______ Distance

__author__ _ 'randy'


c_ TestDistance(unittest.TestCase):
    ___ testDistance2d
        dist _ Distance()

        assertEqual(5, dist.distance2d([0, 0], [3, 4]))
        assertAlmostEqual(10.296, dist.distance2d([0, 0], [5, 9]), 3)
        assertAlmostEqual(2.236, dist.distance2d([0, 0], [1, 2]), 3)

    ___ testDistance3d
        dist _ Distance()

        assertAlmostEqual(7.071, dist.distance3d([0, 0, 0], [3, 4, 5]), 3)
        assertAlmostEqual(10.488, dist.distance3d([0, 0, 0], [5, 6, 7]), 3)
        assertEqual(0, dist.distance3d([0, 0, 0], [0, 0, 0]))


if __name__ == '__main__':
    unittest.main()
