import unittest


def legacy_test_function1():
    result = 1 + 2
    a__ result == 3


def legacy_test_function2():
    result = 1 * 2
    a__ result == 2


test_case1 = unittest.FunctionTestCase(testFunc=legacy_test_function1)
test_case2 = unittest.FunctionTestCase(testFunc=legacy_test_function2)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(test_case1)
    test_suite.addTest(test_case2)
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
    # runner.run(test_case1)
