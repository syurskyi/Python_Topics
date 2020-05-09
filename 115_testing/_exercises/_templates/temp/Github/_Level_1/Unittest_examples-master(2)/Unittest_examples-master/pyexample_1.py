#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Простой пример Unittest Framework
"""

______ unittest


c_ BaseTestClass(unittest.TestCase):
    """
        объявление Test Class'а. Для распознавания функций в
        классе и интерпретации их как тесты, необходимо чтобы
        класс наследовался от unittest.TestCase и тесты в
        классе должны начинаться с префикса test
    """

    ___ test_add
        assertEqual(120, 100+20)
        assertFalse(10 > 20)
        assertGreater(120, 100)

    ___ test_sub
        assertEqual(100, 140 - 40)

if __name__ == '__main__':
    # Запуск всех тестов в текущем модуле.
    unittest.main()