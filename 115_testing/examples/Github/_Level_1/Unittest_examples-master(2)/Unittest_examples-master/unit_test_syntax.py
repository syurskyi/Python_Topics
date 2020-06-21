#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Описание всех методов Unittest Framework
"""

import unittest


class TestUnittestMethods(unittest.TestCase):
    def testAssertTrue(self):
        """Вызывает ошибку, если значение аргумента != True"""
        self.assertTrue(True)

    def testFailUnless(self):
        """
            Устаревшее название для assertTrue().
            Вызывает ошибку, если значение аргумента != True
        """
        self.failUnless(True)

    def testFailIf(self):
        """Устаревшая функция, теперь называется assertFalse()"""
        self.assertFalse(False)

    def testAssertFalse(self):
        """Вызывает ошибку, если начение аргумента != False"""
        self.assertFalse(False)

    def testEqual(self):
        """Вызывает ошибку, если значения двух аргументов НЕ равны"""
        self.failUnlessEqual(1, 3 - 2)

    def testNotEqual(self):
        """Вызывает ошибку, если значения двух аргументов равны"""
        self.failIfEqual(2, 3 - 2)

    def testNotAlmostEqual(self):
        """
            Старое название функции.
            Теперь называется assertNotAlmostEqual().
            Сравнивает два аргумента с округлением, можно задать
            это округление. Вызывает ошибку, если значения равны.
        """
        self.failIfAlmostEqual(1.1, 3.5 - 2.0, places=1)

    def testAlmostEqual(self):
        """
            Старое название функции.
            Теперь называется assertAlmostEquals().
            Сравнивается два аргумента с округлением, можно задать
            это округление. Вызывает ошибку, если значения НЕ равны.
        """
        self.failUnlessAlmostEqual(1.1, 3.3 - 2.0, places=0)

if __name__ == '__main__':
    unittest.main()
