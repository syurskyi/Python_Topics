import unittest


class IncrementTest(unittest.TestCase):
    def setUp(self):
        self.my_dict = {'one': 1, 'two': 2}

    def test_del(self):
        del self.my_dict['one']
        self.assertNotIn('one', self.my_dict)

    def test_keys(self):
        self.assertEqual(set(self.my_dict.keys()), {'one', 'two'})
