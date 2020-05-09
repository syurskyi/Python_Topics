
______ unittest


c_ Testing(unittest.TestCase):
    ___ test_string
        a _ 'some'
        b _ 'some'
        assertEqual(a, b)

    ___ test_boolean
        a _ True
        b _ True
        assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
