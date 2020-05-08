#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


c_ ClassA(unittest.TestCase):

    ___ test_add_a(self):
        self.assertEquals(120, 100 + 20)

    ___ test_sub_a(self):
        self.assertEquals(210, 230 - 20)

    ___ test_mul_a(self):
        self.assertEquals(420, 105 * 4)


if __name__ == '__main__':
    unittest.main()