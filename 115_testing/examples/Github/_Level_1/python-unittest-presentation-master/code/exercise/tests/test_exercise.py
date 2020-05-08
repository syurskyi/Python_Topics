#/usr/bin/env python3


import unittest
import exercise as e


class ExampleTest(unittest.TestCase):

    def test_foobar(self):

        return_value = e.foobar('barfoo')
        self.assertEqual(True, return_value)


if __name__ == '__main__':
        unittest.main()
