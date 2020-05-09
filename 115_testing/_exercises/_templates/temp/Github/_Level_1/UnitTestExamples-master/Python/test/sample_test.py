______ sys
______ unittest

____ sample ______ Calc


c_ TestSample(unittest.TestCase):
    @classmethod
    ___ setUpClass(cls):
        cls.calc _ Calc()

    ___ test_add
        assertEqual(15, calc.add(10, 5))
        assertEqual(5, calc.add(8, -3))

    ___ test_pow
        assertEqual(125, calc.pow(5, 3))
        assertEqual(sys.maxsize, calc.pow(2, 31) - 1)


___ suite():
    suite _ unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestSample))
    r_ suite
