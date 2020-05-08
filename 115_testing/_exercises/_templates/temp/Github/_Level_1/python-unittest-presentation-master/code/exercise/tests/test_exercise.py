#/usr/bin/env python3


import unittest
import exercise as e


c_ ExampleTest(unittest.TestCase):

    ___ test_foobar(self):

        return_value = e.foobar('barfoo')
        self.assertEqual(True, return_value)


if __name__ == '__main__':
        unittest.main()
