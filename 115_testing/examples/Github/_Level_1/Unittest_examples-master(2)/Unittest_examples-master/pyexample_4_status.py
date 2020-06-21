#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Обозначение статусов в unittest:

    +----+--------------------+
    | .  | ok                 |
    | F  | FAIL               |
    | E  | ERROR              |
    | x  | expected failure   |
    | s  | skipped 'msg'      |
    | u  | unexpected success |
    +-------------------------+
"""

import unittest


class BaseTestClass(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(210, 110*2 - 10)

    @unittest.skip("not supported")
    def test_skip(self):
        self.assertEqual(1000, 10*10*10)

    def test_fail(self):
        self.assertEqual(1, 2)

    def test_error(self):
        """Вызывает ERROR (E) с запуском по-умолчанию"""
        raise ZeroDivisionError('Error! Division by zero')

    @unittest.expectedFailure
    def test_expected(self):
        """
            Вызывает expected failure (x) с декоратором
            @unittest.expectedFailure
        """
        raise ZeroDivisionError('Error! Division by zero')

    @unittest.expectedFailure
    def test_expected_ok(self):
        """
            Если тестс декоратором @unittest.expectedFailure,
            исключения не кидает и пройден успешно, ему
            присваивается статус - unexpected success (u).
        """
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()