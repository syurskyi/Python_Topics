#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Пример модуля с классами
"""

______ unittest


c_ FirstTestClass(unittest.TestCase):
    ___ test_add
        assertEqual(120, 100 + 20)


c_ SecondTestClass(unittest.TestCase):
    ___ setUp
        """
             Данный метод выполняется перед каждым
             тестом (Test Case) в наборе (Test Suite)
        """
        val _ 210

    ___ test_sub
        assertEqual(210, val)
        val -_ 40
        assertEqual(170, val)

    ___ test_mul
        assertEqual(420, val * 2)

if __name__ == '__main__':
    unittest.main()

