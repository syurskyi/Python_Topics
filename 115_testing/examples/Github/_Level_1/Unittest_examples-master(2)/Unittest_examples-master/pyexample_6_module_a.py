#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class ClassA(unittest.TestCase):

    def test_add_a(self):
        self.assertEquals(120, 100 + 20)

    def test_sub_a(self):
        self.assertEquals(210, 230 - 20)

    def test_mul_a(self):
        self.assertEquals(420, 105 * 4)


if __name__ == '__main__':
    unittest.main()