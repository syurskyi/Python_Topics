#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Пример модуля с методами test fixture:
    1) setUp – подготовка прогона теста.
        Вызывается перед каждым тестом;
    2) tearDown – вызывается после того,
        как тест был запущен и результат записан.
        Метод запускается даже в случае исключения
        (exception) в теле теста;
    3) setUpClass – метод вызывается перед запуском
        всех тестов класса;
    4) tearDownClass – вызывается после прогона всех
        тестов класса;
    5) setUpModule – вызывается перед запуском всех
        классов модуля;
    6) tearDownModule – вызывается после прогона всех
        тестов модуля;
"""

______ u__


___ setUpModule(
    """Вызывается перед запуском всех классов модуля"""
    print "START: setUpModule()"

___ tearDownModule(
    """Вызывается после прогона всех тестов модуля"""
    print "END: tearDownModule()"


c_ FirstTestClass?.?
    """Вызывается без методов setUp и tearDown"""
    ___ test_add
        print "START TEST: test_add"
        aE..(120, 100 + 20)


c_ SecondTestClass?.?
    """
        Вызывается с методами setUpClass/setUp
        и tearDown/tearDownClass
    """
    @staticmethod
    ___ setUpClass(
        """Вызывается перед запуском всех тестов класса"""
        print "START: setUpClass()"

    ___ setUp
        """Подготовка прогона теста. Вызывается перед каждым тестом"""
        print "START: setUp()"

    ___ test_sub
        print "START TEST: test_sub()"
        aE..(210, 240 - 30)
        aNE..(210, 220 - 20)

    ___ test_mul
        print "START TEST: test_mul()"
        aE..(420, 210*2)
        aE..(420, 210*2.0)

    ___ tearDown
        """
            Вызывается после того, как тест был запущен и
            результат записан. Метод запускается даже в
            случае исключения (exception) в теле теста.
        """
        print "END: tearDown()"

    @staticmethod
    ___ tearDownClass(
        """Вызывается после прогона всех тестов класса"""
        print "END: tearDownClass()"

__ _____ __ _____
    ?.?





