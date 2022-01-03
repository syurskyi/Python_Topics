_______ unittest

_______ two_fer


c_ Two_Fer_test(unittest.TestCase):
    ___ test_empty
        assertEqual(two_fer.two_fer(), 'One for you, one for me.')

    ___ test_eve
        assertEqual(two_fer.two_fer("Eve"), "One for Eve, one for me.")

    ___ test_bob
        assertEqual(two_fer.two_fer("Bob"), "One for Bob, one for me.")


__ __name__ __ '__main__':
    unittest.main()
