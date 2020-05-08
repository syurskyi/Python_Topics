
import unittest


c_ Testing(unittest.TestCase):
    ___ test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    ___ test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
