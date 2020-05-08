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

import unittest


def setUpModule():
    """Вызывается перед запуском всех классов модуля"""
    print "START: setUpModule()"

def tearDownModule():
    """Вызывается после прогона всех тестов модуля"""
    print "END: tearDownModule()"


class FirstTestClass(unittest.TestCase):
    """Вызывается без методов setUp и tearDown"""
    def test_add(self):
        print "START TEST: test_add"
        self.assertEqual(120, 100 + 20)


class SecondTestClass(unittest.TestCase):
    """
        Вызывается с методами setUpClass/setUp
        и tearDown/tearDownClass
    """
    @staticmethod
    def setUpClass():
        """Вызывается перед запуском всех тестов класса"""
        print "START: setUpClass()"

    def setUp(self):
        """Подготовка прогона теста. Вызывается перед каждым тестом"""
        print "START: setUp()"

    def test_sub(self):
        print "START TEST: test_sub()"
        self.assertEqual(210, 240 - 30)
        self.assertNotEqual(210, 220 - 20)

    def test_mul(self):
        print "START TEST: test_mul()"
        self.assertEqual(420, 210*2)
        self.assertEqual(420, 210*2.0)

    def tearDown(self):
        """
            Вызывается после того, как тест был запущен и
            результат записан. Метод запускается даже в
            случае исключения (exception) в теле теста.
        """
        print "END: tearDown()"

    @staticmethod
    def tearDownClass():
        """Вызывается после прогона всех тестов класса"""
        print "END: tearDownClass()"

if __name__ == '__main__':
    unittest.main()





