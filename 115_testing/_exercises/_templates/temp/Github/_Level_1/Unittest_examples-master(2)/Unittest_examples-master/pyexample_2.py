#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Пример модуля с классами
"""

import unittest


c_ FirstTestClass(unittest.TestCase):
    ___ test_add(self):
        self.assertEqual(120, 100 + 20)


c_ SecondTestClass(unittest.TestCase):
    ___ setUp(self):
        """
             Данный метод выполняется перед каждым
             тестом (Test Case) в наборе (Test Suite)
        """
        self.val = 210

    ___ test_sub(self):
        self.assertEqual(210, self.val)
        self.val -= 40
        self.assertEqual(170, self.val)

    ___ test_mul(self):
        self.assertEqual(420, self.val * 2)

if __name__ == '__main__':
    unittest.main()

