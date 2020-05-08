import unittest


c_ IncrementTest(unittest.TestCase):
    ___ setUp(self):
        self.my_dict = {'one': 1, 'two': 2}

    ___ test_del(self):
        del self.my_dict['one']
        self.assertNotIn('one', self.my_dict)

    ___ test_keys(self):
        self.assertEqual(set(self.my_dict.keys()), {'one', 'two'})
