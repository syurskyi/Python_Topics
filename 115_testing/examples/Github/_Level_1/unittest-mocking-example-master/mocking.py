import unittest
from unittest.mock import MagicMock
import sample

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.org_summation_method = sample.summation
        sample.summation = MagicMock()
        sample.summation.return_value = 3

    def tearDown(self):
        sample.summation = self.org_summation_method

    def test_add(self):
        result = sample.add(1,5)
        self.assertEqual(result, 3)

    def test_exception(self):
        sample.summation.side_effect = Exception
        self.assertRaises(Exception, sample.add,1,5) 


if __name__ == "__main__":
    unittest.main()
