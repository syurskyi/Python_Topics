# -*- coding: utf-8 -*-

______ unittest
______ sys
sys.path.append('app/')

___ test_all():
    loader _ unittest.TestLoader()
    suite  _ unittest.TestSuite()
    # add tests to the test suite
    suite.addTests(loader.discover(start_dir_'.', pattern_'*tests.py'))
    runner _ unittest.TextTestRunner(verbosity_3)
    runner.run(suite)
    
___ test_foo():
    loader _ unittest.TestLoader()
    suite  _ unittest.TestSuite()
    # add tests to the test suite
    suite.addTests(loader.discover(start_dir_'.', pattern_'*foo*tests.py'))
    runner _ unittest.TextTestRunner(verbosity_3)
    runner.run(suite)

___ test_bar():
    loader _ unittest.TestLoader()
    suite  _ unittest.TestSuite()
    # add tests to the test suite
    suite.addTests(loader.discover(start_dir_'.', pattern_'*bar*tests.py'))
    runner _ unittest.TextTestRunner(verbosity_3)
    runner.run(suite)