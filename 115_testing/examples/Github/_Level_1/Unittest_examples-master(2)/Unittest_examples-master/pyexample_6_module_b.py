#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class ClassB(unittest.TestCase):

    def test_add_b(self):
        self.assertEquals(120, 100 + 20)

    def test_sub_b(self):
        self.assertEquals(210, 230 - 20)

    def test_mul_b(self):
        self.assertEquals(420, 105 * 4)


class ClassC(unittest.TestCase):

    def test_add_c(self):
        self.assertEquals(120, 100 + 20)

    def test_sub_c(self):
        self.assertEquals(210, 230 - 20)

    def test_mul_c(self):
        self.assertEquals(420, 105 * 4)


if __name__ == '__main__':
    unittest.main()