# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('app/')

def test_all():
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()
    # add tests to the test suite
    suite.addTests(loader.discover(start_dir='.', pattern='*tests.py'))
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)
    
def test_foo():
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()
    # add tests to the test suite
    suite.addTests(loader.discover(start_dir='.', pattern='*foo*tests.py'))
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)

def test_bar():
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()
    # add tests to the test suite
    suite.addTests(loader.discover(start_dir='.', pattern='*bar*tests.py'))
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)