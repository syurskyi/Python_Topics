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


c_ BaseTestClass(unittest.TestCase):

    ___ test_ok(self):
        self.assertEqual(210, 110*2 - 10)

    @unittest.skip("not supported")
    ___ test_skip(self):
        self.assertEqual(1000, 10*10*10)

    ___ test_fail(self):
        self.assertEqual(1, 2)

    ___ test_error(self):
        """Вызывает ERROR (E) с запуском по-умолчанию"""
        raise ZeroDivisionError('Error! Division by zero')

    @unittest.expectedFailure
    ___ test_expected(self):
        """
            Вызывает expected failure (x) с декоратором
            @unittest.expectedFailure
        """
        raise ZeroDivisionError('Error! Division by zero')

    @unittest.expectedFailure
    ___ test_expected_ok(self):
        """
            Если тестс декоратором @unittest.expectedFailure,
            исключения не кидает и пройден успешно, ему
            присваивается статус - unexpected success (u).
        """
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()