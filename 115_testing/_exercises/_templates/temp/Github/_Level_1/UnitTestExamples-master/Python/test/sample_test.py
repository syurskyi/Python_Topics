______ ___
______ u__

____ sample ______ Calc


c_ TestSample?.?
    ??
    ___ setUpClass ___
        cls.calc _ Calc()

    ___ test_add
        aE..(15, calc.add(10, 5))
        aE..(5, calc.add(8, -3))

    ___ test_pow
        aE..(125, calc.pow(5, 3))
        aE..(___.maxsize, calc.pow(2, 31) - 1)


___ suite(
    suite _ u__.TestSuite()
    suite.addTests(u__.makeSuite(TestSample))
    r_ suite
