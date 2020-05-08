import unittest
from src.distance import Distance

__author__ = 'randy'


class TestDistance(unittest.TestCase):
    def testDistance2d(self):
        dist = Distance()

        self.assertEqual(5, dist.distance2d([0, 0], [3, 4]))
        self.assertAlmostEqual(10.296, dist.distance2d([0, 0], [5, 9]), 3)
        self.assertAlmostEqual(2.236, dist.distance2d([0, 0], [1, 2]), 3)

    def testDistance3d(self):
        dist = Distance()

        self.assertAlmostEqual(7.071, dist.distance3d([0, 0, 0], [3, 4, 5]), 3)
        self.assertAlmostEqual(10.488, dist.distance3d([0, 0, 0], [5, 6, 7]), 3)
        self.assertEqual(0, dist.distance3d([0, 0, 0], [0, 0, 0]))


if __name__ == '__main__':
    unittest.main()
