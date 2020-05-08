#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Скрипт для запуска ВСЕХ тестов,
    находящихся в одной директории.
    Для ручного запуска:
    pip install discover - произволится один раз для загрузки модуля
    python -m discover -p "pyexample_*.py",
    где "pyexample_*.py" - шаблон для поиска файлов с тестами
"""

import unittest

loader = unittest.TestLoader()

# Поиск файлов с тестами по шаблону 'pyexample_*.py'
suite = loader.discover(start_dir='.',
                        pattern='pyexample_*.py')

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)