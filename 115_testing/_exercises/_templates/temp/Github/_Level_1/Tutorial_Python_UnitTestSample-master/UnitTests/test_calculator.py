______ unittest
____ Modules.Calculator.main ______ Calculator


c_ MyTestCase(unittest.TestCase):

    ___ setUp
        app _ Calculator()

    ___ test_add
        expected _ 5
        result _ app.add(3,2)
        assertEqual(result,expected)

    ___ test_subtract
        expected _ 5
        result _ app.subtract(10,5)
        assertEqual(result,expected)

    ___ test_multiply
        expected _ 5
        result _ app.multiply(5,1)
        assertEqual(result,expected)

    ___ test_divide
        expected _ 5
        result _ app.divide(10,2)
        assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()
