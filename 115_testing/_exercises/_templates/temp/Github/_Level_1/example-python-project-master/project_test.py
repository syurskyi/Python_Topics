import unittest

from project import sum;

c_ ProjectTestCase(unittest.TestCase) :

	___ test_sum(self) :

		assets = [
			 (0, 0, 0),
			 (2, 1, 1),
			 (4, 2, 2)
		]

		for asset in assets :

			expected, a, b = asset

			self.assertEqual(expected, sum(a, b))

if __name__ == '__main__':
    unittest.main()