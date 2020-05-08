#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Пример модуля с классами
"""

import unittest


class FirstTestClass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(120, 100 + 20)


class SecondTestClass(unittest.TestCase):
    def setUp(self):
        """
             Данный метод выполняется перед каждым
             тестом (Test Case) в наборе (Test Suite)
        """
        self.val = 210

    def test_sub(self):
        self.assertEqual(210, self.val)
        self.val -= 40
        self.assertEqual(170, self.val)

    def test_mul(self):
        self.assertEqual(420, self.val * 2)

if __name__ == '__main__':
    unittest.main()

