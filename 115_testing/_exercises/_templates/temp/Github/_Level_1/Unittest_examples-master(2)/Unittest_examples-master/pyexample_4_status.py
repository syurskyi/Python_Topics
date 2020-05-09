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

______ unittest


c_ BaseTestClass(unittest.TestCase):

    ___ test_ok
        assertEqual(210, 110*2 - 10)

    @unittest.skip("not supported")
    ___ test_skip
        assertEqual(1000, 10*10*10)

    ___ test_fail
        assertEqual(1, 2)

    ___ test_error
        """Вызывает ERROR (E) с запуском по-умолчанию"""
        raise ZeroDivisionError('Error! Division by zero')

    @unittest.expectedFailure
    ___ test_expected
        """
            Вызывает expected failure (x) с декоратором
            @unittest.expectedFailure
        """
        raise ZeroDivisionError('Error! Division by zero')

    @unittest.expectedFailure
    ___ test_expected_ok
        """
            Если тестс декоратором @unittest.expectedFailure,
            исключения не кидает и пройден успешно, ему
            присваивается статус - unexpected success (u).
        """
        assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()