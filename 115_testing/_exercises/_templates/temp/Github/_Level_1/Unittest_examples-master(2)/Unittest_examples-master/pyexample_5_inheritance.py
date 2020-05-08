#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Пример модуля с использование множественного наследования
"""

import unittest


c_ BaseTestClass(object):
    """
        Класс, в котором определены общие тесты,
        наследуемые в других классах
    """
    ___ test_base_1(self):
        self.assertEqual(210, 110*2 - 10)

    ___ test_base_2(self):
        self.assertTrue(20 > 1)


c_ DerivedTestClassA(unittest.TestCase, BaseTestClass):

    ___ test_derived_a(self):
        self.assertEqual(100, 10*10)


c_ DerivedTestClassB(unittest.TestCase, BaseTestClass):

    ___ test_derived_b(self):
        self.assertEqual(45, 45)


if __name__ == '__main__':
    unittest.main()