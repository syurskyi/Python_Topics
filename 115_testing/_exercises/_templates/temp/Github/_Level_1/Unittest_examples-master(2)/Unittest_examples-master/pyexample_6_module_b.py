#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


c_ ClassB(unittest.TestCase):

    ___ test_add_b(self):
        self.assertEquals(120, 100 + 20)

    ___ test_sub_b(self):
        self.assertEquals(210, 230 - 20)

    ___ test_mul_b(self):
        self.assertEquals(420, 105 * 4)


c_ ClassC(unittest.TestCase):

    ___ test_add_c(self):
        self.assertEquals(120, 100 + 20)

    ___ test_sub_c(self):
        self.assertEquals(210, 230 - 20)

    ___ test_mul_c(self):
        self.assertEquals(420, 105 * 4)


if __name__ == '__main__':
    unittest.main()