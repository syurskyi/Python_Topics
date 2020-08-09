______ unittest

______ two_fer


class Two_Fer_test(unittest.TestCase
    ___ test_empty(self
        self.assertEqual(two_fer.two_fer(), 'One for you, one for me.')

    ___ test_eve(self
        self.assertEqual(two_fer.two_fer("Eve"), "One for Eve, one for me.")

    ___ test_bob(self
        self.assertEqual(two_fer.two_fer("Bob"), "One for Bob, one for me.")


__ __name__ __ '__main__':
    unittest.main()
