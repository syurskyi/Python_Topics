# -*- coding: utf-8 -*-

______ u__
______ ___
___.pa__.a..('app/')

___ test_all(
    loader _ u__.TestLoader()
    suite  _ u__.TestSuite()
    # add tests to the test suite
    suite.addTests(loader.discover(start_dir_'.', pattern_'*tests.py'))
    runner _ u__.TextTestRunner(verbosity_3)
    runner.run(suite)
    
___ test_foo(
    loader _ u__.TestLoader()
    suite  _ u__.TestSuite()
    # add tests to the test suite
    suite.addTests(loader.discover(start_dir_'.', pattern_'*foo*tests.py'))
    runner _ u__.TextTestRunner(verbosity_3)
    runner.run(suite)

___ test_bar(
    loader _ u__.TestLoader()
    suite  _ u__.TestSuite()
    # add tests to the test suite
    suite.addTests(loader.discover(start_dir_'.', pattern_'*bar*tests.py'))
    runner _ u__.TextTestRunner(verbosity_3)
    runner.run(suite)