#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Скрипт для запуска нескольких модулей с тестами
"""

______ u__

______ pyexample_6_module_a
______ pyexample_6_module_b

loader _ u__.TestLoader()

# Загрузка всех тестов со всех классов указанного модуля

suite _ loader.loadTestsFromModule(pyexample_6_module_a)
suite.addTests(loader.loadTestsFromModule(pyexample_6_module_b))

# 1) <имя_модуля>, и тогда метод грузит все тесты из каждого
# класса указанного модуля:
# suite.addTests(loader.loadTestsFromName('pyexample_6_module_b'))

# 2) <имя_модуля.имя_класса>, и тогда метод грузит все тесты
# только указанного класса указанного модуля:
# suite.addTests(loader.loadTestsFromName('pyexample_6_module_b.ClassB'))

# 3) <имя_модуля.имя_класса.имя_теста>, и тогда метод грузит
# только указанный тест класса
# suite.addTests(loader.loadTestsFromName('pyexample_6_module_b.ClassC.test_add_c'))

# 4) loadTestsFromNames от loadTestsFromName отличается только тем,
# что принимает на вход последовательность строк:
# suite.addTests(loader.loadTestsFromNames(
#                 ['pyexample_6_module_b.ClassB',
#                  'pyexample_6_module_b.ClassC.test_add_c']))


runner _ u__.TextTestRunner(verbosity_2)
result _ runner.run(suite)
