#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Простой пример Unittest Framework
"""

import unittest


class BaseTestClass(unittest.TestCase):
    """
        объявление Test Class'а. Для распознавания функций в
        классе и интерпретации их как тесты, необходимо чтобы
        класс наследовался от unittest.TestCase и тесты в
        классе должны начинаться с префикса test
    """

    def test_add(self):
        self.assertEqual(120, 100+20)
        self.assertFalse(10 > 20)
        self.assertGreater(120, 100)

    def test_sub(self):
        self.assertEqual(100, 140 - 40)

if __name__ == '__main__':
    # Запуск всех тестов в текущем модуле.
    unittest.main()