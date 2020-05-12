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

______ u__


c_ BaseTestClass?.?

    ___ test_ok
        aE..(210, 110*2 - 10)

    @u__.skip("not supported")
    ___ test_skip
        aE..(1000, 10*10*10)

    ___ test_fail
        aE..(1, 2)

    ___ test_error
        """Вызывает ERROR (E) с запуском по-умолчанию"""
        r_ Z..('Error! Division by zero')

    @u__.expectedFailure
    ___ test_expected
        """
            Вызывает expected failure (x) с декоратором
            @unittest.expectedFailure
        """
        r_ Z..('Error! Division by zero')

    @u__.expectedFailure
    ___ test_expected_ok
        """
            Если тестс декоратором @unittest.expectedFailure,
            исключения не кидает и пройден успешно, ему
            присваивается статус - unexpected success (u).
        """
        aE..(1, 1)


__ _____ __ _____
    ?.?