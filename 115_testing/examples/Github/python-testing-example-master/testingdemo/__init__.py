"""
 https://github.com/lathama/python-testing-example
"""

import datetime
import os
import sys
import unittest

if __debug__:

    import_dir = "./libraries/"
    for d in os.listdir(import_dir):
        if os.path.isdir(import_dir + d):
            sys.path.insert(1, import_dir + d)

    try:
        import coverage
        COVERAGE = True
    except ImportError:
        COVERAGE = False
    try:
        import pycodestyle
        STYLECHECK = True
    except ImportError:
        STYLECHECK = False

    if COVERAGE:
        codecoverage = coverage.Coverage(omit='*unittests/*')
        # Unittests skew results
        codecoverage.start()
    else:
        print("Code Coverage Disabled")

    __version__ = '1.0.1'
    TESTING = True

    from testingdemo.howto import *

    unittesting_log = open('unittesting.log', 'a')
    file_pos = unittesting_log.tell()
    timestamp = str(datetime.datetime.now().isoformat(' ')) + "\n"
    unittesting_log.write("Testing Example - " + timestamp)
    suite = unittest.TestLoader().discover('./testingdemo/unittests')
    unittest.TextTestRunner(stream=unittesting_log, descriptions=True,
                            verbosity=3).run(suite)
    unittesting_log.close()

    unittesting_log = open('unittesting.log')
    unittesting_log.seek(file_pos)
    print(unittesting_log.read())
    unittesting_log.close()

    somethinguseful = AnExample()
    somethinguseful.make_something()
    print(somethinguseful.report_something())

    if COVERAGE:
        codecoverage.stop()
        codecoverage.save()
        codecoverage.html_report(directory="coverage")
        print("Code coverage report done. See the index.html in: ")
        print("\t" + '/coverage')

    if STYLECHECK:
        print('Style Check Start')
        checker = pycodestyle.StyleGuide(exclude=['libraries'], quiet=False)
        result = checker.check_files('.')
        print('Style Check End')
    else:
        print("Code Style Checking is disabled")
