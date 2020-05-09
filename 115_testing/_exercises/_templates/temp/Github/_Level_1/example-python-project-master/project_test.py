______ unittest

____ project ______ sum;

c_ ProjectTestCase(unittest.TestCase) :

	___ test_sum(self) :

		assets _ [
			 (0, 0, 0),
			 (2, 1, 1),
			 (4, 2, 2)
		]

		for asset in assets :

			expected, a, b _ asset

			assertEqual(expected, sum(a, b))

if __name__ == '__main__':
    unittest.main()