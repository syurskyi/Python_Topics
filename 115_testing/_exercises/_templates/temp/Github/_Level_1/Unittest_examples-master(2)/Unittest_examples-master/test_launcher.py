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

______ u__

loader _ u__.TestLoader()

# Поиск файлов с тестами по шаблону 'pyexample_*.py'
suite _ loader.discover(start_dir_'.',
                        pattern_'pyexample_*.py')

runner _ u__.TextTestRunner(verbosity_2)
result _ runner.run(suite)