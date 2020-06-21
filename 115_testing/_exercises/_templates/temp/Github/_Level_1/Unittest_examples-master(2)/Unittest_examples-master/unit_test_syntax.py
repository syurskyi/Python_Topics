#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Описание всех методов Unittest Framework
"""

______ u__


c_ TestUnittestMethods?.?
    ___ testAssertTrue
        """Вызывает ошибку, если значение аргумента != True"""
        aT..(T..)

    ___ testFailUnless
        """
            Устаревшее название для assertTrue().
            Вызывает ошибку, если значение аргумента != True
        """
        failUnless(T..)

    ___ testFailIf
        """Устаревшая функция, теперь называется assertFalse()"""
        aF..(F..)

    ___ testAssertFalse
        """Вызывает ошибку, если начение аргумента != False"""
        aF..(F..)

    ___ testEqual
        """Вызывает ошибку, если значения двух аргументов НЕ равны"""
        failUnlessEqual(1, 3 - 2)

    ___ testNotEqual
        """Вызывает ошибку, если значения двух аргументов равны"""
        failIfEqual(2, 3 - 2)

    ___ testNotAlmostEqual
        """
            Старое название функции.
            Теперь называется assertNotAlmostEqual().
            Сравнивает два аргумента с округлением, можно задать
            это округление. Вызывает ошибку, если значения равны.
        """
        failIfAlmostEqual(1.1, 3.5 - 2.0, places_1)

    ___ testAlmostEqual
        """
            Старое название функции.
            Теперь называется assertAlmostEquals().
            Сравнивается два аргумента с округлением, можно задать
            это округление. Вызывает ошибку, если значения НЕ равны.
        """
        failUnlessAlmostEqual(1.1, 3.3 - 2.0, places_0)

__ _____ __ _____
    ?.?
